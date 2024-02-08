import json
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
from src.db.cache_storage import CacheStorage
from src.db.cloudstorage import CloudStorage
from src.users.exceptions import (
    EmailTaken,
    InvalidPassword,
    InvalidProfileData,
    InvalidUserData,
    RegisterFailed,
    TokenDoesNotExist,
    UserDoesNotExist,
    UsernameTaken,
)
from src.users.models.user_model import User
from src.users.repositories import ProfileRepository, UserRepository
from src.users.utils import prepare_profile_image

cache = CacheStorage()
cloud_storage = CloudStorage()


class AuthService:
    def __init__(
        self,
        user_repository: UserRepository,
        profile_repository: ProfileRepository,
    ):
        self.user_repository = user_repository
        self.profile_repository = profile_repository

    def authenticate_user(
        self, username: str, password: str, db: Session
    ) -> Optional[User]:
        user = self.user_repository.get_by_username(username=username, db=db)
        if not user:
            raise UserDoesNotExist
        if not verify_passwords(password, user.password):
            raise InvalidPassword
        return user

    def register(
        self, user_data: RegisterUserModel, db: Session
    ) -> Optional[JSONResponse]:
        user_data.password = hash_password(user_data.password)
        if self.user_repository.get_by_username(user_data.username, db):
            raise UsernameTaken
        elif self.user_repository.get_by_email(user_data.email, db):
            raise EmailTaken
        try:
            user = self.user_repository.create_model(user=user_data, db=db)
            if not user:
                db.rollback()
                raise InvalidUserData

            if not user_data.profile.image_url:
                raise HTTPException(status_code=400, detail="Profile image is required")
            image = prepare_profile_image(
                image_url=user_data.profile.image_url,
                user_id=user.id,
            )
            cloud_storage.upload_file(
                **image,
            )

            profile = self.profile_repository.create_model(
                name=user_data.profile.name,
                surname=user_data.profile.surname,
                user_id=user.id,
                db=db,
            )
            if not profile:
                db.rollback()
                raise InvalidProfileData
            return JSONResponse(
                content=RegisterEndpoint(
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

        self.user_repository.set_is_active(auth_user, db)
        cache.set_value(
            key=f"user:{str(auth_user.id)}",
            value=json.dumps(
                auth_user.as_dict()
            ),  # TODO .encode("utf-8"), bytes or not for me better json
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
        user = self.user_repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        token = encode_jwt_token(username=user.username, user_id=user.id)
        return JSONResponse(
            content=RefreshTokenEndpoint(**token).model_dump(),
            status_code=200,
        )
