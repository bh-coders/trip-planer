from typing import Optional

from sqlalchemy.orm import Session

from src.auth.exceptions import (
    EmailTaken,
    InvalidPassword,
    RegisterFailed,
    TokenDoesNotExist,
    UserDoesNotExist,
    UsernameTaken,
)
from src.auth.models import User
from src.auth.repositories import UserRepository
from src.auth.schemas import (
    CreateUserSchema,
    LoginResponse,
    LoginUserSchema,
    RefreshTokenResponse,
    RegisterResponse,
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


class AuthService:
    def __init__(self, repository: UserRepository):
        self.user_repository = repository

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
        self, user: CreateUserSchema, db: Session
    ) -> Optional[RegisterResponse]:
        user.password = hash_password(user.password)
        if self.user_repository.get_by_username(user.username, db):
            raise UsernameTaken
        elif self.user_repository.get_by_email(user.email, db):
            raise EmailTaken
        try:
            self.user_repository.create_model(user, db)
            return RegisterResponse(
                message="User registered successfully",
            )
        except Exception:
            raise RegisterFailed

    def login(self, user: LoginUserSchema, db: Session) -> Optional[LoginResponse]:
        auth_user = self.authenticate_user(
            username=user.username,
            password=user.password,
            db=db,
        )
        if not auth_user:
            raise NotAuthenticated
        self.user_repository.set_is_active(auth_user, db)
        token = encode_jwt_token(username=auth_user.username, user_id=auth_user.id)
        return LoginResponse(**token)

    def refresh_credentials(self, token: str, db: Session):
        if not token:
            raise TokenDoesNotExist
        user_payload = decode_jwt_token(token)
        user_id = user_payload.get("user_id")
        user = self.user_repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        token = encode_jwt_token(username=user.username, user_id=user.id)
        return RefreshTokenResponse(**token)
