from fastapi import status

from src.auth.constants import ErrorCode
from src.core.exceptions import (
    BadRequest,
    Conflict,
    DetailedHTTPException,
    NotAuthenticated,
    NotFound,
    PermissionDenied,
)


class InvalidPassword(BadRequest):
    DETAIL = ErrorCode.INVALID_PASSWORD


class UsernameTaken(Conflict):
    DETAIL = ErrorCode.USERNAME_TAKEN


class EmailTaken(Conflict):
    DETAIL = ErrorCode.EMAIL_TAKEN


class InvalidNewOldEmail(BadRequest):
    DETAIL = ErrorCode.INVALID_NEW_OLD_EMAIL


class InvalidOldEmail(BadRequest):
    DETAIL = ErrorCode.INVALID_OLD_EMAIL


class InvalidNewEmail(BadRequest):
    DETAIL = ErrorCode.INVALID_NEW_EMAIL


class UsernameDoesNotExist(NotFound):
    DETAIL = ErrorCode.USERNAME_DOES_NOT_EXIST


class UserDoesNotExist(NotFound):
    DETAIL = ErrorCode.USER_DOES_NOT_EXIST


class TokenDoesNotExist(NotFound):
    DETAIL = ErrorCode.TOKEN_DOES_NOT_EXIST


class AuthRequired(NotAuthenticated):
    DETAIL = ErrorCode.AUTHENTICATION_REQUIRED


class AuthorizationFailed(PermissionDenied):
    DETAIL = ErrorCode.AUTHORIZATION_FAILED


class InvalidToken(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_TOKEN


class InvalidCredentials(NotAuthenticated):
    DETAIL = ErrorCode.INVALID_CREDENTIALS


class TokenExpired(NotAuthenticated):
    DETAIL = ErrorCode.TOKEN_EXPIRED


class RefreshTokenNotValid(NotAuthenticated):
    DETAIL = ErrorCode.REFRESH_TOKEN_NOT_VALID


class InvalidNewOrRewritePassword(BadRequest):
    DETAIL = ErrorCode.INVALID_NEW_OR_REWRITE_PASSWORD


class InvalidOldPassword(BadRequest):
    DETAIL = ErrorCode.INVALID_OLD_PASSWORD


class EmailChangeFailed(DetailedHTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorCode.EMAIL_CHANGE_FAILED


class PasswordChangeFailed(DetailedHTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorCode.PASSWORD_CHANGE_FAILED


class DeleteFailed(DetailedHTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorCode.DELETE_FAILED


class RegisterFailed(DetailedHTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = ErrorCode.REGISTER_FAILED
