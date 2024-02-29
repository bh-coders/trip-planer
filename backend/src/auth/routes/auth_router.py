from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.schemas import (
    GetRefreshTokenModel,
    LoginEndpoint,
    LoginUserModel,
    RefreshTokenEndpoint,
    RegisterEndpoint,
    RegisterUserModel,
)
from src.auth.services import AuthService
from src.db.database import get_db
from src.users.repositories import ProfileRepository, UserRepository

router = APIRouter()
user_repository = UserRepository()
profile_repository = ProfileRepository()
auth_service = AuthService(
    repository=user_repository,
)


@router.post(
    "/register",
    response_model=RegisterEndpoint,
    response_class=JSONResponse,
)
def register_view(
    user: RegisterUserModel,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.register(user=user, db=db)


@router.post(
    "/login",
    response_model=LoginEndpoint,
    response_class=JSONResponse,
)
def login_view(
    user: LoginUserModel,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.login(user=user, db=db)


@router.post(
    "/refresh",
    response_model=RefreshTokenEndpoint,
    response_class=JSONResponse,
)
def refresh_view(
    credentials: GetRefreshTokenModel,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.refresh_credentials(token=credentials.refresh_token, db=db)
