import logging
import uuid
from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.auth.utils import decode_jwt_token
from src.users.exceptions import (
    InvalidCredentials,
    InvalidToken,
    TokenExpired,
    UserDoesNotExist,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

logger = logging.getLogger(__name__)


def verify_jwt(
    token: str = Depends(oauth2_scheme),
) -> bool:
    try:
        payload = decode_jwt_token(token=token)
        logger.info(payload)
        return True
    except jwt.ExpiredSignatureError:
        raise TokenExpired
    except jwt.InvalidTokenError:
        raise InvalidToken
    except jwt.PyJWTError:
        raise InvalidCredentials


def get_current_user_id(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> uuid.UUID:
    try:
        payload = decode_jwt_token(token=token)
        logger.info(payload)
        user_id = payload.get("user_id")
        if not user_id:
            raise UserDoesNotExist
        return user_id
    except jwt.ExpiredSignatureError:
        raise TokenExpired
    except jwt.InvalidTokenError:
        raise InvalidToken
    except jwt.PyJWTError:
        raise InvalidCredentials
