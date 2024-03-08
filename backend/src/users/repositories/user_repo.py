import logging
from typing import Optional
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.users.interfaces import IUserRepository
from src.users.models.user_model import User
from src.users.schemas.user import CreateUserSchema

logger = logging.getLogger(__name__)


class UserRepository(IUserRepository):
    def get_by_id(
        self,
        user_id: UUID,
        db: Session,
    ) -> Optional[User]:
        try:
            user = db.query(User).filter(User.id == user_id).first()
            return user
        except SQLAlchemyError as error:
            logger.error("Error getting user: %s", error)
            return None

    def get_by_username(
        self,
        username: str,
        db: Session,
    ) -> Optional[User]:
        try:
            user = db.query(User).filter(User.username == username).first()
            return user
        except SQLAlchemyError as error:
            logger.error("Error getting user: %s", error)
            return None

    def get_by_email(
        self,
        email: str,
        db: Session,
    ) -> Optional[User]:
        try:
            user = db.query(User).filter(User.email == email).first()
            return user
        except SQLAlchemyError as error:
            logger.error("Error getting user: %s", error)
            return None

    def create_user(
        self,
        user_schema: CreateUserSchema,
        db: Session,
    ) -> Optional[User]:
        try:
            with db.begin_nested():
                new_user = User(
                    username=user_schema.username,
                    email=user_schema.email,
                    password=user_schema.password,
                )
                db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error registering user: %s", error)
            return None

    def set_is_active(
        self,
        user_obj: User,
        db: Session,
    ) -> bool:
        try:
            with db.begin_nested():
                setattr(user_obj, "is_active", True)
                db.add(user_obj)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error setting user as active: %s", error)
            return False

    def update_email(
        self,
        new_email: str,
        user_obj: User,
        db: Session,
    ) -> bool:
        try:
            with db.begin_nested():
                setattr(user_obj, "email", new_email)
                db.add(user_obj)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error updating user email: %s", error)
            return False

    def update_password(
        self,
        new_password: str,
        user_obj: User,
        db: Session,
    ) -> bool:
        try:
            with db.begin_nested():
                setattr(user_obj, "password", new_password)
                db.add(user_obj)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error updating user password: %s", error)
            return False

    def delete_user(
        self,
        user_obj: User,
        db: Session,
    ) -> bool:
        try:
            with db.begin_nested():
                db.delete(user_obj)
            db.commit()
            return True
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error deleting user: %s", error)
            return False
