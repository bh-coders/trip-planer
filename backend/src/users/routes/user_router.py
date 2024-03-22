from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.core.interceptors.auth_interceptor import get_user_id
from src.db.cache_storage import CacheHandler
from src.db.database import get_db, get_redis
from src.users.repositories import UserRepository
from src.users.schemas.user import (
    DeleteSuccessSchema,
    EmailChangeSuccessSchema,
    PasswordChangeSuccessSchema,
    PasswordsMatchUpdateSchema,
    UserEmailChangeSchema,
)
from src.users.services import UserService

router = APIRouter()
user_repository = UserRepository()
user_service = UserService(
    repository=user_repository,
)


@router.patch(
    "/change-email",
    response_model=EmailChangeSuccessSchema,
    response_class=JSONResponse,
)
def change_email_view(
    user_email_change_schema: UserEmailChangeSchema,
    user_id: Annotated[UUID, Depends(get_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_email(
        user_id=user_id,
        new_email=user_email_change_schema.new_email,
        old_email=user_email_change_schema.old_email,
        password=user_email_change_schema.password,
        db=db,
    )


@router.patch(
    "/change-password",
    response_model=PasswordChangeSuccessSchema,
    response_class=JSONResponse,
)
def change_password_view(
    passwords_match_update_schema: PasswordsMatchUpdateSchema,
    user_id: Annotated[UUID, Depends(get_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_password(
        user_id=user_id,
        old_password=passwords_match_update_schema.old_password,
        new_password=passwords_match_update_schema.new_password,
        rewrite_password=passwords_match_update_schema.rewrite_password,
        db=db,
    )


@router.delete(
    "/delete",
    response_model=DeleteSuccessSchema,
    response_class=JSONResponse,
)
def delete_view(
    user_id: Annotated[UUID, Depends(get_user_id)],
    db: Annotated[Session, Depends(get_db)],
    cache_handler: Annotated[CacheHandler, Depends(get_redis)],
):
    return user_service.delete_user(
        user_id=user_id,
        db=db,
        cache_handler=cache_handler,
    )
