from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.core.interceptors.auth_interceptor import get_user_id
from src.db.database import get_db, get_redis, get_session
from src.users.repositories import ProfileRepository
from src.users.schemas.profile import (
    ProfileDetailSchema,
    ProfileUpdateSchema,
    ProfileUpdateSuccessSchema,
)
from src.users.services import ProfileService

router = APIRouter()
profile_repository = ProfileRepository()


profile_service = ProfileService(
    repository=profile_repository,
)
profile_service.start_handler_user_created(
    cache_handler=get_redis(),
    db=get_session(),
)


@router.get(
    "/",
    response_model=ProfileDetailSchema,
    response_class=JSONResponse,
)
def detail_view(
    user_id: Annotated[UUID, Depends(get_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return profile_service.get_profile(user_id=user_id, db=db)


@router.put(
    "/update",
    response_model=ProfileUpdateSuccessSchema,
    response_class=JSONResponse,
)
def update_view(
    profile_update_schema: ProfileUpdateSchema,
    user_id: Annotated[UUID, Depends(get_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return profile_service.edit_profile(
        profile_update_schema=profile_update_schema, user_id=user_id, db=db
    )
