import logging
import uuid
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.users.interfaces import AbstractProfileRepository
from src.users.models import Profile

logger = logging.getLogger(__name__)


class ProfileRepository(AbstractProfileRepository):
    def get_by_id(
        self,
        profile_id: uuid.UUID,
        db: Session,
    ) -> Optional[Profile]:
        try:
            profile = db.query(Profile).filter(Profile.id == profile_id).first()
            return profile
        except SQLAlchemyError as error:
            logger.error("Error getting profile: %s", error)
            return None

    def create_profile(
        self,
        name: str,
        surname: str,
        user_id: uuid.UUID,
        db: Session,
    ) -> Optional[Profile]:
        try:
            with db.begin_nested():
                new_profile = Profile(
                    name=name,
                    surname=surname,
                    user_id=user_id,
                )
                db.add(new_profile)
            db.commit()
            db.refresh(new_profile)
            return new_profile
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error creating profile: %s", error)
            return None

    def get_profile_by_user_id(
        self,
        user_id: uuid.UUID,
        db: Session,
    ) -> Optional[Profile]:
        try:
            profile = db.query(Profile).filter(Profile.user_id == user_id).first()
            return profile
        except SQLAlchemyError as error:
            logger.error("Error getting profile: %s", error)
            return None

    def update_model(
        self,
        profile: Profile,
        db: Session,
    ) -> Optional[Profile]:
        try:
            with db.begin_nested():
                for attr, value in vars(profile).items():
                    setattr(profile, attr, value)
                db.add(profile)
            db.commit()
            return profile
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error updating profile: %s", error)
            return None

    def delete_model(
        self,
        profile_id: uuid.UUID,
        db: Session,
    ) -> None:
        try:
            with db.begin_nested():
                db.query(Profile).filter(Profile.id == profile_id).delete()
            db.commit()
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error deleting profile: %s", error)
            return None
