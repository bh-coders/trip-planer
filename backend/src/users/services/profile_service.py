import inspect
import threading
import time
import uuid
from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.utils import start_listening
from src.db.cache_storage import CacheHandler
from src.db.cloudstorage import CloudStorage
from src.db.database import get_db
from src.users.repositories import ProfileRepository
from src.users.schemas.profile import CreateProfileModel
from src.users.utils import prepare_profile_image


class ProfileService:
    def __init__(
        self,
        repository: ProfileRepository,
        cache_handler: CacheHandler,
        cloud_storage: CloudStorage,
    ):
        self.repository = repository
        self.cache_handler = cache_handler
        self.cloud_storage = cloud_storage
        self.db = None

    def get_sqlalchemy_session(
        self,
        db: Annotated[Session, Depends(get_db)],
    ):
        self.db = db

    @start_listening
    def event_handler(self):
        self.cache_handler.subscribe_event("user_created")
        while True:
            time.sleep(0.1)
            data = self.cache_handler.get_event()
            if data:
                user_id = uuid.UUID(data["id"])
                profile = data["profile"]
                if self.create_related_profile(
                    user_id=user_id,
                    profile=profile,
                ):
                    self.cache_handler.unsubscribe_event("user_created")

    def create_related_profile(
        self,
        user_id: uuid.UUID,
        profile: CreateProfileModel,
    ):
        is_created = False
        try:
            self.repository.create_profile(
                user_id=user_id,
                name=profile.get("name"),
                surname=profile.get("surname"),
                db=self.db,
            )
            image = prepare_profile_image(
                image_url=profile.get("image_url"),
                user_id=user_id,
            )
            self.cloud_storage.upload_file(
                **image,
            )
            is_created = True
        except Exception:
            raise HTTPException(status_code=400, detail="Profile already exists")
        return is_created
