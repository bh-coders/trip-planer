from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.schemas import (
    LoginSchema,
    LoginUserSchema,
    RefreshTokenSuccessSchema,
    RegisterSuccessSchema,
    RegisterUserSchema,
    TokenSchema,
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
    user_register_schema: RegisterUserSchema,
    db: Annotated[Session, Depends(get_db)],
    cache_handler: Annotated[CacheHandler, Depends(get_redis)],
):
    return auth_service.register(
        user_register_schema=user_register_schema,
        db=db,
        cache_handler=cache_handler,
    )


@router.post(
    "/login",
    response_model=LoginSchema,
    response_class=JSONResponse,
)
def login_view(
    user_login_schema: LoginUserSchema,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.login(user_login_schema=user_login_schema, db=db)


@router.post(
    "/refresh",
    response_model=RefreshTokenSuccessSchema,
    response_class=JSONResponse,
)
def refresh_view(
    credentials: TokenSchema,
    db: Annotated[Session, Depends(get_db)],
):
    return auth_service.refresh_credentials(token=credentials.refresh_token, db=db)
