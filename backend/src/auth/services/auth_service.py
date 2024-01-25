import uuid
from datetime import timedelta
from typing import Optional

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.auth.interfaces import Repository
from src.auth.schemas import (
    RegisterRequest,
    RegisterResponse,
    SignInRequest,
)
from src.auth.utils import return_token


class AuthService:
    def __init__(self, repository: Repository):
        self._repository = repository

    @staticmethod
    def generate_token_response(
        username: str, user_id: uuid.UUID
    ) -> Optional[JSONResponse]:
        try:
            token = return_token(username, user_id)
            refresh_token = token.pop("refresh_token")
            response = JSONResponse(content=token)
            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                expires=int(timedelta(days=365).total_seconds()),
            )
            return response

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def register_user(
        self, user: RegisterRequest, db: Session
    ) -> Optional[RegisterResponse]:
        if self._repository.authenticate(user.username, user.password, db):
            raise HTTPException(status_code=400, detail="User already exists")
        if self._repository.register(user, db):
            return RegisterResponse(message="User registered successfully")
        else:
            raise HTTPException(status_code=500, detail="Failed to register user")

    def sign_in_user(
        self, sign_in_user: SignInRequest, db: Session
    ) -> Optional[JSONResponse]:
        if self._repository.authenticate(
            sign_in_user.username, sign_in_user.password, db
        ):
            user = self._repository.get_user(sign_in_user.username, db)
            return self.generate_token_response(user.username, user.id)
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")

    def renew_token(self, user: SignInRequest, db: Session) -> JSONResponse:
        if self._repository.authenticate(user.username, user.password, db):
            _user = self._repository.get_user(user.username, db)
            return self.generate_token_response(_user.username, _user.id)
        else:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
