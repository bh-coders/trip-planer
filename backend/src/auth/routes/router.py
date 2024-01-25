from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import ValidationError
from sqlalchemy.orm import Session

from src.auth.repositories.auth_repo import AuthRepository
from src.auth.schemas import (
    RegisterRequest,
    RegisterResponse,
    SignInRequest,
    SignInResponse,
)
from src.auth.services import AuthService
from src.core.database import get_db
from src.core.interceptors.auth_interceptor import verify_jwt
from src.route.schemas import Message, Response404, Response500

router = APIRouter()
_auth_service = AuthService(AuthRepository())


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=201,
    responses={
        400: {"model": Message, "example": {"detail": "User already exists"}},
        404: {"model": Response404},
        500: {"model": Response500},
    },
)
def register_user(
    user: RegisterRequest,
    db: Session = Depends(get_db),
):
    try:
        return _auth_service.register_user(user, db)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())


@router.post("/sign-in", response_model=SignInResponse)
def sign_in_user(
    signin_user: SignInRequest,
    db: Session = Depends(get_db),
):
    return _auth_service.sign_in_user(signin_user, db)


@router.post("/refresh", response_model=SignInResponse)
def refresh_token(user: SignInRequest, token: Request, db: Session = Depends(get_db)):
    _refresh_token = token.cookies.get("refresh_token")
    if _refresh_token:
        try:
            verify_jwt(_refresh_token)
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid token")
        return _auth_service.renew_token(user=user, db=db)
    raise HTTPException(status_code=401, detail="Need login again")
