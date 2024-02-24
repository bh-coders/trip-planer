import json
import uuid
from typing import Optional

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.schemas import (
    LoginEndpoint,
    LoginUserModel,
    RefreshTokenEndpoint,
    RegisterEndpoint,
    RegisterUserModel,
)
from src.auth.utils import (
    decode_jwt_token,
    encode_jwt_token,
    hash_password,
    verify_passwords,
)
from src.core.exceptions import (
    NotAuthenticated,
)
from src.db.cache_storage import CacheHandler, RedisStorage
from src.users.exceptions import (
    EmailTaken,
    InvalidPassword,
    InvalidUserData,
    RegisterFailed,
    TokenDoesNotExist,
    UserDoesNotExist,
    UsernameTaken,
)
from src.users.models.user_model import User
from src.users.repositories import UserRepository
from src.users.schemas.profile import CreateProfileModel
from src.users.schemas.user import CreateUserModel

cache = RedisStorage()


class AuthService:
    def __init__(
        self,
        repository: UserRepository,
        cache_handler: CacheHandler,
    ):
        self.repository = repository
        self.cache_handler = cache_handler

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
            user = self.repository.create_model(user=user, db=db)
        except Exception:
            raise HTTPException(status_code=400, detail="User already exists")
        return user

    def publish_user_created_event(
        self, user_id: str, user: CreateUserModel, profile: CreateProfileModel
    ) -> None:
        self.cache_handler.publish_event(
            pattern="user_created",
            data={
                "id": user_id,
                "email": user.email,
                "username": user.username,
                "profile": {
                    "name": profile.name,
                    "surname": profile.surname,
                    "image_url": profile.image_url,
                },
            },
        )

    def register(self, user: RegisterUserModel, db: Session) -> Optional[JSONResponse]:
        if self.repository.get_by_username(user.username, db):
            raise UsernameTaken
        elif self.repository.get_by_email(user.email, db):
            raise EmailTaken
        try:
            user_db = self.create_user(user=user, db=db)
            if not user_db:
                raise InvalidUserData

            self.publish_user_created_event(
                user_id=str(user_db.id), user=user, profile=user.profile
            )

            return JSONResponse(
                content=RegisterEndpoint(
                    message="User registered successfully"
                ).model_dump(),
                status_code=201,
            )
        except Exception:
            raise RegisterFailed

            # if not user_data.profile.image_url:
            #     raise HTTPException(status_code=400, detail="Profile image is required")
        #     image = prepare_profile_image(
        #         image_url=user_data.profile.image_url,
        #         user_id=user.id,
        #     )
        #     cloud_storage.upload_file(
        #         **image,
        #     )
        #
        #     profile = self.profile_repository.create_model(
        #         name=user_data.profile.name,
        #         surname=user_data.profile.surname,
        #         user_id=user.id,
        #         db=db,
        #     )
        #     if not profile:
        #         db.rollback()
        #         raise InvalidProfileData
        #     return JSONResponse(
        #         content=RegisterEndpoint(
        #             message="User registered successfully"
        #         ).model_dump(),
        #         status_code=201,
        #     )
        # except Exception:
        #     raise RegisterFailed

    def login(self, user: LoginUserModel, db: Session) -> Optional[JSONResponse]:
        auth_user = self.authenticate_user(
            username=user.username,
            password=user.password,
            db=db,
        )
        if not auth_user:
            raise NotAuthenticated

        self.repository.set_is_active(auth_user, db)
        cache.set_value(
            key=f"user:{str(auth_user.id)}",
            value=json.dumps(auth_user.as_dict()),
            expiration=None,
        )
        token = encode_jwt_token(username=auth_user.username, user_id=auth_user.id)
        return JSONResponse(
            content=LoginEndpoint(**token).model_dump(),
            status_code=200,
        )

    def refresh_credentials(self, token: str, db: Session) -> Optional[JSONResponse]:
        if not token:
            raise TokenDoesNotExist
        user_payload = decode_jwt_token(token)
        user_id = user_payload.get("user_id")
        user = self.repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        token = encode_jwt_token(username=user.username, user_id=user.id)
        return JSONResponse(
            content=RefreshTokenEndpoint(**token).model_dump(),
            status_code=200,
        )
