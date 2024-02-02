from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.models import User
from src.auth.repositories import UserRepository
from src.auth.schemas import (
    DeleteResponse,
    EmailChangeResponse,
    EmailChangeSchema,
    PasswordChangeResponse,
    UserPasswordChangeSchema,
)
from src.auth.services import UserService
from src.core.database import get_db
from src.core.interceptors.auth_interceptor import get_current_user

router = APIRouter()
user_repository = UserRepository()
user_service = UserService(repository=user_repository)


@router.post("change-email/", response_model=EmailChangeResponse)
def change_email_view(
    request: EmailChangeSchema,
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_email(
        user=user,
        new_email=request.new_email,
        old_email=request.old_email,
        db=db,
    )


@router.post(
    "change-password/",
    response_model=PasswordChangeResponse,
)
def change_password_view(
    request: UserPasswordChangeSchema,
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.change_password(
        user=user,
        old_password=request.old_password,
        new_password=request.new_password,
        rewrite_password=request.rewrite_password,
        db=db,
    )


@router.post("delete/", response_model=DeleteResponse)
def delete_view(
    user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    return user_service.delete_user(user=user, db=db)
