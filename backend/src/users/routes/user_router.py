import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.interceptors.auth_interceptor import get_current_user_id
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
user_service = UserService(repository=user_repository)


@router.post(
    "/change-email",
    response_model=EmailChangeUserModel,
)
def change_email_view(
    model: EmailChangeUserModel,
    user_id: Annotated[uuid.UUID, Depends(get_current_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_email(
        user_id=user_id,
        new_email=model.new_email,
        old_email=model.old_email,
        db=db,
    )


@router.post(
    "/change-password",
    response_model=PasswordChangeUserModel,
)
def change_password_view(
    model: PasswordChangeUserModel,
    user_id: Annotated[uuid.UUID, Depends(get_current_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_password(
        user_id=user_id,
        old_password=model.old_password,
        new_password=model.new_password,
        rewrite_password=model.rewrite_password,
        db=db,
    )


@router.post(
    "/delete",
    response_model=DeleteEndpoint,
)
def delete_view(
    user_id: Annotated[uuid.UUID, Depends(get_current_user_id)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.delete_user(user_id=user_id, db=db)
