import logging

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.auth.utils import decode_jwt_token
from src.users.exceptions import (
    InvalidCredentials,
    InvalidToken,
    TokenExpired,
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
