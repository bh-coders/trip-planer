from typing import Optional

from sqlalchemy.orm import Session

from src.auth.exceptions import (
    EmailTaken,
    InvalidPassword,
    TokenDoesNotExist,
    UserDoesNotExist,
    UsernameTaken,
)
from src.auth.models import User
from src.auth.repositories import AuthRepository
from src.auth.schemas import (
    GetUser,
    LoginResponse,
    RefreshTokenResponse,
    RegisterResponse,
    UserCreate,
)
from src.auth.utils import (
    decode_jwt_token,
    encode_jwt_token,
    hash_password,
    verify_passwords,
)
from src.core.exceptions import (
    DetailedHTTPException,
    NotAuthenticated,
)


class AuthService:
    def __init__(self, repository: AuthRepository):
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

    def register(self, user: UserCreate, db: Session) -> Optional[RegisterResponse]:
        user.password = hash_password(user.password)
        if self.repository.get_by_username(user.username, db):
            raise UsernameTaken
        elif self.repository.get_by_email(user.email, db):
            raise EmailTaken
        try:
            self.repository.create_user(user, db)
            return RegisterResponse(
                message="User registered successfully",
            )
        except Exception:
            raise DetailedHTTPException

    def login(self, user: GetUser, db) -> Optional[LoginResponse]:
        auth_user = self.authenticate_user(
            username=user.username,
            password=user.password,
            db=db,
        )
        if not auth_user:
            raise NotAuthenticated
        self.repository.set_is_active(auth_user, db)
        token = encode_jwt_token(username=auth_user.username, user_id=auth_user.id)
        return LoginResponse(**token)

    def refresh_credentials(self, token: str, db):
        if not token:
            raise TokenDoesNotExist
        user_payload = decode_jwt_token(token)
        user_id = user_payload.get("user_id")
        user = self.repository.get_by_id(user_id=user_id, db=db)
        if not user:
            raise UserDoesNotExist
        token = encode_jwt_token(username=user.username, user_id=user.id)
        return RefreshTokenResponse(**token)
