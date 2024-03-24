from typing import Optional

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.schemas import (
    LoginSchema,
    LoginUserSchema,
    RefreshTokenSuccessSchema,
    RegisterSuccessSchema,
    RegisterUserSchema,
)
from src.auth.utils import encode_jwt_token, hash_password, verify_passwords
from src.common.exceptions import NotAuthenticated
from src.common.multithreading_utils import publish_handler_event
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
from src.users.schemas.profile import CreateProfileSchema
from src.users.schemas.user import CreateUserSchema


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

    def create_user(self, user_schema: CreateUserSchema, db: Session):
        user_schema.password = hash_password(user_schema.password)
        try:
            user = self.repository.create_user(user_schema=user_schema, db=db)
        except Exception:
            raise HTTPException(status_code=400, detail="User already exists")

        return user

    @staticmethod
    def split_user_and_profile(user_register_schema: RegisterUserSchema):
        user_schema = CreateUserSchema(
            **user_register_schema.model_dump(exclude={"profile"}),
        )
        profile_schema = CreateProfileSchema(
            **user_register_schema.model_dump().get("profile"),
        )
        return user_schema, profile_schema

    def register(
        self,
        user_register_schema: RegisterUserSchema,
        db: Session,
        cache_handler: ICacheHandler,
    ) -> Optional[JSONResponse]:
        user_schema, profile_schema = self.split_user_and_profile(
            user_register_schema=user_register_schema,
        )
        if self.repository.get_by_username(user_schema.username, db):
            raise UsernameTaken
        elif self.repository.get_by_email(user_schema.email, db):
            raise EmailTaken
        try:
            user_obj_db = self.create_user(user_schema=user_schema, db=db)
            if not user_obj_db:
                raise InvalidUserData
            publish_handler_event(
                event_type="user_created",
                data={
                    "id": str(user_obj_db.id),
                    **user_schema.model_dump(),
                    "profile": {
                        **profile_schema.model_dump(),
                    },
                },
                cache_handler=cache_handler,
            )
            return JSONResponse(
                content=RegisterSuccessSchema(
                    message="User registered successfully"
                ).model_dump(),
                status_code=201,
            )
        except Exception:
            raise RegisterFailed

    def login(
        self, user_login_schema: LoginUserSchema, db: Session
    ) -> Optional[JSONResponse]:
        user_obj_db = self.authenticate_user(
            username=user_login_schema.username,
            password=user_login_schema.password,
            db=db,
        )
        if not user_obj_db:
            raise NotAuthenticated
        self.repository.set_is_active(
            user_obj=user_obj_db,
            db=db,
        )
        token = encode_jwt_token(username=user_obj_db.username, user_id=user_obj_db.id)
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
            content=RefreshTokenSuccessSchema(**token).model_dump(),
            status_code=200,
        )
