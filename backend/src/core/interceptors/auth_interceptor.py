import logging
from typing import Annotated, Optional
from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.auth.utils import (
    decode_jwt_token,
    get_token_from_request,
)

logger = logging.getLogger(__name__)

security = HTTPBearer()


def verify_jwt(
    auth: Annotated[HTTPAuthorizationCredentials, Depends(security)]
) -> None:
    decode_jwt_token(token=auth.credentials)


def get_user_id(
    get_token: str = Depends(get_token_from_request),
) -> Optional[UUID]:
    token = decode_jwt_token(token=get_token)
    if token:
        user_id = token.get("user_id")
        return user_id
    return None
