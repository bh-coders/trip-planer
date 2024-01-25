import logging
import uuid
from datetime import timedelta
from typing import Optional

from fastapi import Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.auth.interfaces import Repository
from src.auth.models import User
from src.auth.schemas import (
    RegisterRequest,
    RegisterResponse,
    SignInRequest,
    SignInResponse,
    UserResponse,
)
from src.auth.utils import check_password, hash_password, return_token

logger = logging.getLogger(__name__)


class AuthRepository(Repository):
    def get_user_by_id(self, user_id: uuid.UUID, db: Session) -> Optional[UserResponse]:
        try:
            user = db.query(User).filter_by(id=user_id).first()
            return user
        except Exception as e:
            logger.error(f"Failed to get user: {e}")

    def get_user(self, username: str, db: Session) -> Optional[UserResponse]:
        try:
            user = db.query(User).filter_by(username=username).first()
            return user
        except Exception as e:
            logger.error(f"Failed to get user: {e}")

    def authenticate(self, username: str, password: str, db: Session) -> bool:
        user = self.get_user(username, db)
        if not user:
            return False
        if not check_password(password, user.password):
            return False
        return True

    def register(self, user: RegisterRequest, db: Session) -> bool:
        try:
            with db.begin_nested():
                new_user = User(
                    username=user.username,
                    email=user.email,
                    password=hash_password(user.password),
                )
                db.add(new_user)
            db.commit()
            return True

        except Exception as e:
            db.rollback()
            logger.error(f"Registration failed with error: {e}")
            return False
