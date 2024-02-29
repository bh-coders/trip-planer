import logging
import time
from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.common.utils import run_handler_thread
from src.db.cache_storage import CacheHandler
from src.db.cloud_storage import CloudStorage
from src.users.exceptions import DeleteFailed, InvalidProfileData, ProfileCreationFailed
from src.users.repositories import ProfileRepository
from src.users.schemas.profile import (
    CreateProfileModel,
    ProfileDetailResponse,
    ProfileUpdateResponse,
    UpdateProfileModel,
)
from src.users.utils import (
    delete_profile_image,
    get_profile_image,
    prepare_profile_image,
)

logger = logging.getLogger(__name__)


class ProfileService:
    def __init__(
        self,
        repository: ProfileRepository,
        cloud_storage: CloudStorage,
        db: Session,
    ):
        self.repository = repository
        self.cloud_storage = cloud_storage
        self.db = db
        self.start_listening_threads()

    def start_listening_threads(self):
        run_handler_thread(
            cls=self,
            subscribe_name="user_created",
            handler_name="event_handler_user_created",
        )
        run_handler_thread(
            cls=self,
            subscribe_name="user_deleted",
            handler_name="event_handler_user_deleted",
        )

    def event_handler_user_created(
        self,
        cache_handler: Optional[CacheHandler],
        subscribe_name: Optional[str],
    ):
        cache_handler.subscribe_event(subscribe_name)
        while True:
            time.sleep(0.2)
            data = cache_handler.get_event()
            if data:
                print(data)
                user_id = UUID(data["id"])
                profile = data["profile"]
                self.create_related_profile(
                    user_id=user_id,
                    profile=profile,
                    db=self.db,
                )
                cache_handler.unsubscribe_event("user_created")

    def event_handler_user_deleted(
        self,
        cache_handler: Optional[CacheHandler],
        subscribe_name: Optional[str],
    ):
        cache_handler.subscribe_event(subscribe_name)
        while True:
            time.sleep(0.2)
            data = cache_handler.get_event()
            if data:
                print(data)
                user_id = UUID(data["id"])
                self.delete_related_profile(
                    user_id=user_id,
                )
                cache_handler.unsubscribe_event("user_deleted")

    def create_related_profile(
        self,
        user_id: UUID,
        profile: CreateProfileModel,
        db: Session,
    ):
        try:
            # Create profile in the repository
            profile_db = self.repository.create_profile(
                user_id=user_id,
                name=profile.get("name"),
                surname=profile.get("surname"),
                db=db,
            )
            if profile_db:
                # Prepare and upload profile image to cloud storage
                image = prepare_profile_image(
                    image_url=profile.get("image_url"),
                    user_id=user_id,
                )

                # Upload profile image to cloud storage
                self.cloud_storage.upload_file(
                    **image,
                )
            else:
                raise InvalidProfileData

        except Exception:
            raise ProfileCreationFailed

    @staticmethod
    def delete_related_profile(user_id: UUID):
        try:
            delete_profile_image(user_id=user_id)
            return True
        except Exception:
            raise DeleteFailed

    def get_profile(
        self,
        user_id: UUID,
        db: Session,
    ) -> Optional[JSONResponse]:
        try:
            profile_db = self.repository.get_profile_by_user_id(user_id=user_id, db=db)
            if not profile_db:
                raise InvalidProfileData
            image_base64 = get_profile_image(
                user_id=user_id,
            )

            if not image_base64:
                raise HTTPException(
                    status_code=404,
                    detail="Profile image not found",
                )
            return JSONResponse(
                content=ProfileDetailResponse(
                    name=profile_db.name,
                    surname=profile_db.surname,
                    image_base64=image_base64,
                ).model_dump(),
                status_code=200,
            )

        except Exception:
            raise HTTPException(status_code=404, detail="Profile not found")

    def edit_profile(
        self,
        profile: UpdateProfileModel,
        user_id: UUID,
        db: Session,
    ) -> Optional[JSONResponse]:
        try:
            profile_db = self.repository.get_profile_by_user_id(user_id=user_id, db=db)
            if profile_db:
                if self.repository.update_profile(
                    profile_db=profile_db,
                    profile_update=profile,
                    db=db,
                ):
                    # Prepare and upload profile image to cloud storage
                    image = prepare_profile_image(
                        image_url=profile.image_url,
                        user_id=user_id,
                    )

                    # Upload profile image to cloud storage
                    self.cloud_storage.upload_file(
                        **image,
                    )
                    # Return successful registration message
                    return JSONResponse(
                        content=ProfileUpdateResponse(
                            message="Profile updated successfully"
                        ).model_dump(),
                        status_code=201,
                    )
            else:
                raise InvalidProfileData
        except Exception:
            raise ProfileCreationFailed
