from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.schemas import (
    GetRefreshTokenModel,
    LoginSchema,
    LoginUserModel,
    RefreshTokenSchema,
    RegisterSuccessSchema,
    RegisterUserModel,
)
from src.auth.services import AuthService
from src.db.cache_storage import CacheHandler
from src.db.database import get_db, get_redis
from src.users.repositories import ProfileRepository, UserRepository

router = APIRouter()
user_repository = UserRepository()
profile_repository = ProfileRepository()
auth_service = AuthService(
    repository=user_repository,
)


@router.post(
    "/register",
    response_model=RegisterSuccessSchema,
    response_class=JSONResponse,
)
def register_view(
    user_register_model: RegisterUserModel,
    db: Annotated[Session, Depends(get_db)],
    cache_handler: Annotated[CacheHandler, Depends(get_redis)],
):
    return auth_service.register(
        user_register_model=user_register_model,
        db=db,
        cache_handler=cache_handler,
    )


@router.post(
    "/login",
    response_model=LoginSchema,
    response_class=JSONResponse,
)
def login_view(
    user: LoginUserModel,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.login(user=user, db=db)


@router.post(
    "/refresh",
    response_model=RefreshTokenSchema,
    response_class=JSONResponse,
)
def refresh_view(
    credentials: GetRefreshTokenModel,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.refresh_credentials(token=credentials.refresh_token, db=db)