import logging
from typing import Optional
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.users.interfaces import IProfileRepository
from src.users.models import Profile
from src.users.schemas.profile import UpdateProfileModel

logger = logging.getLogger(__name__)


class ProfileRepository(IProfileRepository):
    def get_by_id(
        self,
        profile_id: UUID,
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
        user_id: UUID,
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
        user_id: UUID,
        db: Session,
    ) -> Optional[Profile]:
        try:
            profile = db.query(Profile).filter(Profile.user_id == user_id).first()
            return profile
        except SQLAlchemyError as error:
            logger.error("Error getting profile: %s", error)
            return None

    def update_profile(
        self,
        profile_obj: Profile,
        profile_update_model: UpdateProfileModel,
        db: Session,
    ) -> Optional[Profile]:
        try:
            with db.begin_nested():
                update_data = profile_update_model.model_dump(exclude_unset=True)
                if "image_url" in update_data:
                    update_data.pop("image_url")
                for key, value in update_data.items():
                    setattr(profile_obj, key, value)
            db.add(profile_obj)
            db.commit()
            return profile_obj
        except SQLAlchemyError as error:
            db.rollback()
            logger.error("Error updating profile: %s", error)
            return None

    def delete_profile(
        self,
        profile_id: UUID,
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
