import logging
import uuid
from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext

from src.core.configs import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    REFRESH_TOKEN_EXPIRE_DAYS,
    SECRET_KEY,
)

password_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")

logger = logging.getLogger(__name__)


def check_password(plain_password: str, hashed_password: str) -> bool:
    return password_hashing.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return password_hashing.hash(password)


def authenticate_password(password_to_check: str, password: str):
    if not check_password(password_to_check, password):
        raise HTTPException(
            status_code=401,
            detail="Invalid password",
        )
    return True


def create_jwt_token(data: dict, expires_delta: timedelta) -> dict:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def return_token(username: str, user_id: uuid.UUID) -> dict:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(
        data={"username": username, "id": str(user_id)},
        expires_delta=access_token_expires,
    )
    refresh_token = create_jwt_token(
        data={"username": username, "id": str(user_id)},
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
    )
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
