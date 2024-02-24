import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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
    "/{user_id}/change-email",
    response_model=EmailChangeUserModel,
)
def change_email_view(
    model: EmailChangeUserModel,
    user_id: str,
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_email(
        user_id=uuid.UUID(user_id),
        new_email=model.new_email,
        old_email=model.old_email,
        db=db,
    )


@router.post(
    "/{user_id}/change-password",
    response_model=PasswordChangeUserModel,
)
def change_password_view(
    model: PasswordChangeUserModel,
    user_id: str,
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_password(
        user_id=uuid.UUID(user_id),
        old_password=model.old_password,
        new_password=model.new_password,
        rewrite_password=model.rewrite_password,
        db=db,
    )


@router.post(
    "/{user_id}/delete",
    response_model=DeleteEndpoint,
)
def delete_view(
    user_id: str,
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.delete_user(user_id=uuid.UUID(user_id), db=db)
