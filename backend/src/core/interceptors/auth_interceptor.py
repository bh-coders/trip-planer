import logging
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from src.auth.repositories.auth_repo import AuthRepository
from src.core.configs import ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
auth_repository = AuthRepository()

logger = logging.getLogger(__name__)


def verify_jwt(token: str = Depends(oauth2_scheme)) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
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


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        logger.info(payload)
        username = payload.get("username")
        if auth_repository.get_user_by_username(username):
            return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
