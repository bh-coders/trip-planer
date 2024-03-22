import logging
import time
from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.common.multithreading_utils import run_handler_thread
from src.db.interfaces.cache_handler import ICacheHandler
from src.users.exceptions import (
    InvalidProfileData,
    ProfileCreationFailed,
    UserAlreadyExists,
)
from src.users.interfaces import IProfileRepository
from src.users.schemas.profile import (
    CreateProfileSchema,
    ProfileDetailSchema,
    ProfileUpdateSchema,
    ProfileUpdateSuccessSchema,
)

logger = logging.getLogger(__name__)


class ProfileService:
    def __init__(
        self,
        repository: IProfileRepository,
    ):
        self.repository = repository

    def start_handler_user_created(
        self,
        cache_handler: ICacheHandler,
        db: Session,
    ):
        run_handler_thread(
            method=self.event_handler_user_created,
            event_type="user_created",
            cache_handler=cache_handler,
            db=db,
        )

    def event_handler_user_created(
        self,
        event_type: str,
        cache_handler: ICacheHandler,
        db: Session,
    ):
        cache_handler.subscribe_event(event_type)
        while True:
            time.sleep(0.2)
            data = cache_handler.get_event()
            if data:
                user_id = UUID(data["id"])
                profile = data["profile"]
                self.create_profile(
                    user_id=user_id,
                    profile=profile,
                    db=db,
                )
                cache_handler.unsubscribe_event(event_type)

    def create_profile(
        self,
        user_id: UUID,
        profile: CreateProfileSchema,
        db: Session,
    ):
        if self.repository.get_profile_by_user_id(user_id=user_id, db=db):
            raise UserAlreadyExists
        try:
            self.repository.create_profile(
                user_id=user_id,
                name=profile.get("name"),
                surname=profile.get("surname"),
                db=db,
            )
        except Exception:
            raise ProfileCreationFailed

    def get_profile(
        self,
        user_id: UUID,
        db: Session,
    ) -> Optional[JSONResponse]:
        try:
            profile_obj_db = self.repository.get_profile_by_user_id(
                user_id=user_id, db=db
            )
            if not profile_obj_db:
                raise InvalidProfileData
            return JSONResponse(
                content=ProfileDetailSchema(
                    name=profile_obj_db.name,
                    surname=profile_obj_db.surname,
                ).model_dump(),
                status_code=200,
            )
        except Exception:
            raise HTTPException(status_code=404, detail="Profile not found")

    def edit_profile(
        self,
        profile_update_schema: ProfileUpdateSchema,
        user_id: UUID,
        db: Session,
    ) -> Optional[JSONResponse]:
        try:
            profile_obj_db = self.repository.get_profile_by_user_id(
                user_id=user_id, db=db
            )
            if profile_obj_db:
                if self.repository.update_profile(
                    profile_obj=profile_obj_db,
                    profile_update_schema=profile_update_schema,
                    db=db,
                ):
                    return JSONResponse(
                        content=ProfileUpdateSuccessSchema(
                            message="Profile updated successfully"
                        ).model_dump(),
                        status_code=201,
                    )
            else:
                raise InvalidProfileData
        except Exception:
            raise ProfileCreationFailed
