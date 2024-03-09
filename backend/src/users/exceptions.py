from src.common.exceptions import (
    BadRequest,
    NotAuthenticated,
    PermissionDenied,
)
from src.users.constants import ErrorCode


class InvalidPassword(BadRequest):
    DETAIL = ErrorCode.INVALID_PASSWORD


class AuthorizationFailed(PermissionDenied):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class TokenExpired(NotAuthenticated):
    DETAIL = ErrorCode.TOKEN_EXPIRED
