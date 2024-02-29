from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.core.interceptors.auth_interceptor import verify_user_id
from src.db.cache_storage import CacheHandler, RedisStorage
from src.db.database import get_db
from src.users.repositories import UserRepository
from src.users.schemas.user import (
    DeleteEndpoint,
    EmailChangeUserModel,
    PasswordChangeUserModel,
)
from src.users.services import UserService

router = APIRouter()
user_repository = UserRepository()
redis_storage = RedisStorage()
cache_handler = CacheHandler(redis=redis_storage)
user_service = UserService(
    repository=user_repository,
    cache_handler=cache_handler,
)


@router.patch(
    "/change-email",
    response_model=EmailChangeUserModel,
    response_class=JSONResponse,
)
def change_email_view(
    model: EmailChangeUserModel,
    user_id: Annotated[UUID, Depends(verify_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_email(
        user_id=user_id,
        new_email=model.new_email,
        old_email=model.old_email,
        password=model.password,
        db=db,
    )


@router.patch(
    "/change-password",
    response_model=PasswordChangeUserModel,
    response_class=JSONResponse,
)
def change_password_view(
    model: PasswordChangeUserModel,
    user_id: Annotated[UUID, Depends(verify_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_password(
        user_id=user_id,
        old_password=model.old_password,
        new_password=model.new_password,
        rewrite_password=model.rewrite_password,
        db=db,
    )


@router.delete(
    "/delete",
    response_model=DeleteEndpoint,
    response_class=JSONResponse,
)
def delete_view(
    user_id: Annotated[UUID, Depends(verify_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.delete_user(user_id=user_id, db=db)
