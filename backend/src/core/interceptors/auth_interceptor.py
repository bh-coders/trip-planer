import logging
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status

from src.auth.repositories.user_repo import UserRepository
from src.auth.utils import decode_jwt_token
from src.core.configs import ALGORITHM, SECRET_KEY
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
        raise HTTPException(status_code=403, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)],
) -> bool:
    try:
        payload = decode_jwt_token(token=token)
        logger.info(payload)
        user_id = payload.get("user_id")
        if auth_repository.get_by_id(user_id=user_id, db=db):
            return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
