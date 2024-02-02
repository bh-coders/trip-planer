from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.repositories import UserRepository
from src.auth.schemas import (
    CreateUserSchema,
    GetRefreshTokenSchema,
    LoginResponse,
    LoginUserSchema,
    RefreshTokenResponse,
    RegisterResponse,
)
from src.auth.services import AuthService
from src.core.database import get_db

router = APIRouter()
user_repository = UserRepository()
auth_service = AuthService(repository=user_repository)


@router.post(
    "/register",
    response_model=RegisterResponse,
)
def register_view(
    user: CreateUserSchema,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.register(user=user, db=db)


@router.post("/login", response_model=LoginResponse)
def login_view(
    user: LoginUserSchema,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.login(user=user, db=db)


@router.post("/refresh/", response_model=RefreshTokenResponse)
def refresh_view(
    request: GetRefreshTokenSchema,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.refresh_credentials(token=request.refresh_token, db=db)
