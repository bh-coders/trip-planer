import logging
import uuid
from datetime import timedelta
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.auth.interfaces import Repository
from src.auth.models import User
from src.auth.schemas import UserCreate
from src.auth.schemas.model_schema import UserModel

logger = logging.getLogger(__name__)


class AuthRepository(Repository):
    def get_by_id(self, user_id: uuid.UUID, db: Session) -> Optional[User]:
        try:
            user = db.query(User).filter_by(id=user_id).first()
            return user
        except SQLAlchemyError as error:
            logger.error("Error getting user: %s", error)
            return None

    def get_by_username(self, username: str, db: Session) -> Optional[User]:
        try:
            user = db.query(User).filter_by(username=username).first()
            return user
        except SQLAlchemyError as error:
            logger.error("Error getting user: %s", error)
            return None

    def get_by_email(self, email: str, db: Session) -> Optional[User]:
        try:
            user = db.query(User).filter_by(email=email).first()
            return user
        except SQLAlchemyError as error:
            logger.error("Error getting user: %s", error)
            return None

    def create_user(self, user: UserCreate, db: Session) -> bool:
        try:
            with db.begin_nested():
                new_user = User(
                    username=user.username,
                    email=user.email,
                    password=user.password,
                )
                db.add(new_user)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error registering user: %s", error)
            return False

    def set_is_active(self, user: UserModel, db: Session) -> bool:
        user = self.get_by_email(email=user.email, db=db)
        try:
            setattr(user, "is_active", True)
            db.add(user)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error setting user as active: %s", error)
            return False
