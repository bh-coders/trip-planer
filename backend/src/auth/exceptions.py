from src.auth.constants import ErrorCode
from src.core.exceptions import BadRequest, NotAuthenticated, PermissionDenied


class InvalidPassword(BadRequest):
    DETAIL = ErrorCode.INVALID_PASSWORD


class UsernameTaken(BadRequest):
    DETAIL = ErrorCode.USERNAME_TAKEN


class EmailTaken(BadRequest):
    DETAIL = ErrorCode.EMAIL_TAKEN


class UsernameDoesNotExist(NotAuthenticated):
    DETAIL = ErrorCode.USERNAME_DOES_NOT_EXIST


class UserDoesNotExist(NotAuthenticated):
    DETAIL = ErrorCode.USER_DOES_NOT_EXIST


class TokenDoesNotExist(NotAuthenticated):
    DETAIL = ErrorCode.TOKEN_DOES_NOT_EXIST


class AuthRequired(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class AuthorizationFailed(PermissionDenied):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class RefreshTokenNotValid(NotAuthenticated):
    DETAIL = ErrorCode.REFRESH_TOKEN_NOT_VALID
