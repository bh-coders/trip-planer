import logging
import uuid
from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from passlib.context import CryptContext

from src.core.configs import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    REFRESH_TOKEN_EXPIRE_DAYS,
    SECRET_KEY,
)
from src.users.exceptions import (
    AuthorizationFailed,
    InvalidCredentials,
    InvalidPassword,
    InvalidToken,
    TokenExpired,
)

password_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")

logger = logging.getLogger(__name__)


def check_password(plain_password: str, hashed_password: str) -> bool:
    return password_hashing.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return password_hashing.hash(password)


def verify_passwords(plain_password: str, hashed_password: str):
    if not check_password(plain_password, hashed_password):
        raise InvalidPassword
    return True


def create_jwt_token(data: dict, expires_delta: timedelta) -> dict:
    to_encode = data.copy()

    to_encode.update(
        {
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + expires_delta,
            "jti": str(uuid.uuid4()),
        }
    )
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    logger.info("Token created: %s", encoded_jwt)
    return encoded_jwt


def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logger.info("Token decoded: %s", payload)
        return payload
    except jwt.ExpiredSignatureError:
        raise TokenExpired
    except jwt.InvalidTokenError:
        raise InvalidToken
    except jwt.PyJWTError:
        raise InvalidCredentials


def get_access_token(
    username: str,
    user_id: uuid.UUID,
    token_type: str = "access",
) -> dict:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(
        data={
            "username": username,
            "user_id": str(user_id),
            "token_type": token_type,
        },
        expires_delta=access_token_expires,
    )
    logger.info("Access token created: %s", access_token)
    return access_token


def get_refresh_token(
    username: str,
    user_id: uuid.UUID,
    token_type: str = "refresh",
) -> dict:
    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_token = create_jwt_token(
        data={
            "username": username,
            "user_id": str(user_id),
            "token_type": token_type,
        },
        expires_delta=refresh_token_expires,
    )
    logger.info("Refresh token created: %s", refresh_token)
    return refresh_token


def token_is_valid(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except jwt.exceptions.DecodeError:
        logger.error("Invalid token")
        return False


def encode_jwt_token(username: str, user_id: uuid.UUID) -> dict:
    access_token = get_access_token(username, user_id)
    refresh_token = get_refresh_token(username, user_id)
    data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
    logger.info("Tokens set: %s", data)
    return data


def get_token_from_request(request: Request) -> Optional[str]:
    authorization = request.headers.get("Authorization")
    scheme, token = get_authorization_scheme_param(authorization)
    if not authorization or scheme.lower() != "bearer":
        raise AuthorizationFailed
    return token
