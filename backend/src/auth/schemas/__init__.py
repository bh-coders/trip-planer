from src.auth.schemas.response import (
    DeleteResponse,
    EmailChangeResponse,
    LoginResponse,
    PasswordChangeResponse,
    RefreshTokenResponse,
    RegisterResponse,
)
from src.auth.schemas.schema import (
    CreateUserSchema,
    EmailChangeSchema,
    GetRefreshTokenSchema,
    LoginUserSchema,
    UserPasswordChangeSchema,
)

__all__ = [
    # register_view
    "CreateUserSchema",
    "RegisterResponse",
    # login_view
    "LoginUserSchema",
    "LoginResponse",
    # refresh_view
    "GetRefreshTokenSchema",
    "RefreshTokenResponse",
    # change_email_view
    "EmailChangeSchema",
    "EmailChangeResponse",
    # change_password_view
    "UserPasswordChangeSchema",
    "PasswordChangeResponse",
    # delete_view
    "DeleteResponse",
]
