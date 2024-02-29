from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from src.core.interceptors.auth_interceptor import verify_user_id
from src.db.cloud_storage import CloudStorage
from src.db.database import engine, get_db
from src.users.repositories import ProfileRepository
from src.users.schemas.profile import (
    ProfileDetailResponse,
    ProfileUpdateResponse,
    UpdateProfileModel,
)
from src.users.services import ProfileService

router = APIRouter()
profile_repository = ProfileRepository()
cloud_storage = CloudStorage()
session = Session(bind=engine)


profile_service = ProfileService(
    repository=profile_repository,
    cloud_storage=cloud_storage,
    db=session,
)


@router.get(
    "/",
    response_model=ProfileDetailResponse,
    response_class=JSONResponse,
)
def detail_view(
    user_id: Annotated[UUID, Depends(verify_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return profile_service.get_profile(user_id=user_id, db=db)


@router.put(
    "/update",
    response_model=ProfileUpdateResponse,
    response_class=JSONResponse,
)
def update_view(
    profile: UpdateProfileModel,
    user_id: Annotated[UUID, Depends(verify_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return profile_service.edit_profile(profile=profile, user_id=user_id, db=db)
