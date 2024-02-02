import logging
import uuid
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.auth.interfaces import AbstractUserRepository
from src.auth.models import User
from src.auth.schemas import CreateUserSchema

logger = logging.getLogger(__name__)


class UserRepository(AbstractUserRepository):
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

    def create_model(self, user: CreateUserSchema, db: Session) -> bool:
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

    def set_is_active(self, user: User, db: Session) -> bool:
        try:
            setattr(user, "is_active", True)
            db.add(user)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error setting user as active: %s", error)
            return False

    def update_email(self, new_email: str, user: User, db: Session) -> bool:
        try:
            setattr(user, "email", new_email)
            db.add(user)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error updating user email: %s", error)
            return False

    def update_password(self, new_password: str, user: User, db: Session) -> bool:
        try:
            setattr(user, "password", new_password)
            db.add(user)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error updating user password: %s", error)
            return False

    def delete_model(self, user: User, db: Session) -> bool:
        try:
            db.delete(user)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error deleting user: %s", error)
            return False
