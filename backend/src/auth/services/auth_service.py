from typing import Optional

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.schemas import (
    LoginSchema,
    LoginUserModel,
    RefreshTokenSchema,
    RegisterSuccessSchema,
    RegisterUserModel,
)
from src.auth.utils import (
    encode_jwt_token,
    hash_password,
    verify_passwords,
)
from src.common.exceptions import (
    NotAuthenticated,
)
from src.common.multithreading_utils import (
    publish_handler_event,
    publish_handler_thread,
)
from src.core.interceptors.auth_interceptor import get_user_id
from src.db.interfaces import ICacheHandler
from src.users.exceptions import (
    EmailTaken,
    InvalidPassword,
    InvalidUserData,
    RegisterFailed,
    TokenDoesNotExist,
    UserDoesNotExist,
    UsernameTaken,
)
from src.users.interfaces import IUserRepository
from src.users.models.user_model import User
from src.users.schemas.user import CreateUserModel


class AuthService:
    def __init__(
        self,
        repository: IUserRepository,
    ):
        self.repository = repository

    def authenticate_user(
        self, username: str, password: str, db: Session
    ) -> Optional[User]:
        user = self.repository.get_by_username(username=username, db=db)
        if not user:
            raise UserDoesNotExist
        if not verify_passwords(password, user.password):
            raise InvalidPassword
        return user

    def create_user(self, user: CreateUserModel, db: Session):
        user.password = hash_password(user.password)
        try:
            user = self.repository.create_user(user_create_model=user, db=db)
        except Exception:
            raise HTTPException(status_code=400, detail="User already exists")

        return user

    def register(
        self,
        user_register_model: RegisterUserModel,
        db: Session,
        cache_handler: ICacheHandler,
    ) -> Optional[JSONResponse]:
        if self.repository.get_by_username(user_register_model.username, db):
            raise UsernameTaken
        elif self.repository.get_by_email(user_register_model.email, db):
            raise EmailTaken
        try:
            user_obj_db = self.create_user(user=user_register_model, db=db)
            if not user_obj_db:
                raise InvalidUserData
            if publish_handler_thread(
                event_type="user_created",
                data={
                    "id": str(user_obj_db.id),
                    **user_register_model.model_dump(
                        include={"username", "email", "profile"}
                    ),
                },
                cache_handler=cache_handler,
            ):
                return JSONResponse(
                    content=RegisterSuccessSchema(
                        message="User registered successfully"
                    ).model_dump(),
                    status_code=201,
                )
        except Exception:
            raise RegisterFailed

    def login(self, user: LoginUserModel, db: Session) -> Optional[JSONResponse]:
        auth_user = self.authenticate_user(
            username=user.username,
            password=user.password,
            db=db,
        )
        if not auth_user:
            raise NotAuthenticated
        self.repository.set_is_active(
            user_obj=auth_user,
            db=db,
        )
        token = encode_jwt_token(username=auth_user.username, user_id=auth_user.id)
        return JSONResponse(
            content=LoginSchema(**token).model_dump(),
            status_code=200,
        )

    def refresh_credentials(self, token: str, db: Session) -> Optional[JSONResponse]:
        if not token:
            raise TokenDoesNotExist
        user_id = get_user_id(get_token=token)
        user = self.repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        token = encode_jwt_token(username=user.username, user_id=user.id)
        return JSONResponse(
            content=RefreshTokenSchema(**token).model_dump(),
            status_code=200,
        )
