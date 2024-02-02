import logging
from typing import Annotated, Optional

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.auth.exceptions import (
    InvalidCredentials,
    InvalidToken,
    TokenExpired,
    UserDoesNotExist,
)
from src.auth.models import User
from src.auth.repositories.user_repo import UserRepository
from src.auth.utils import decode_jwt_token
from src.core.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
auth_repository = UserRepository()

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


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> Optional[User]:
    try:
        payload = decode_jwt_token(token=token)
        logger.info(payload)
        user_id = payload.get("user_id")
        if user := auth_repository.get_by_id(user_id=user_id, db=db):
            return user
        raise UserDoesNotExist
    except jwt.ExpiredSignatureError:
        raise TokenExpired
    except jwt.InvalidTokenError:
        raise InvalidToken
    except jwt.PyJWTError:
        raise InvalidCredentials
