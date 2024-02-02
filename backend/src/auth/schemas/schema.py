from pydantic import BaseModel, Field

from src.auth.schemas.model import (
    EmailModel,
    PasswordModel,
    PasswordsModel,
    UsernameModel,
)


# register_view
class CreateUserSchema(UsernameModel, EmailModel, PasswordsModel):
    username: str = Field(..., alias="username")
    email: str = Field(..., alias="email")
    password: str = Field(..., alias="password")
    rewrite_password: str = Field(..., alias="rewrite_password")

    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "username": "basic",
                "email": "basic@basic.com",
                "password": "Password123!",
                "rewrite_password": "Password123!",
            },
        },
    }


# login_view
class LoginUserSchema(UsernameModel, PasswordModel):
    username: str = Field(..., alias="username")
    password: str = Field(..., alias="password")

    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "username": "basic",
                "password": "Password123!",
            },
        },
    }


# refresh_view
class GetRefreshTokenSchema(BaseModel):
    refresh_token: str

    model_config = {
        "json_schema_extra": {
            "title": "Token",
            "description": "Token model",
            "example": {
                "refresh_token": "some_refresh_token",
            },
        },
    }


# change_email_view
class EmailChangeSchema(EmailModel):
    new_email: str = Field(..., alias="email")
    old_email: str

    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "new_email": "basic@basic.com",
                "old_email": "basic@basic.com",
            },
        },
    }


# change_password_view
class UserPasswordChangeSchema(PasswordsModel):
    old_password: str = Field(..., alias="password")
    new_password: str = Field(..., alias="password")
    rewrite_password: str = Field(..., alias="rewrite_password")

    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "old_password": "Password123!",
                "new_password": "Password123!",
                "rewrite_password": "Password123!",
            },
        },
    }
