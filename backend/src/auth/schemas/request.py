from typing import Annotated

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
)

from src.users.schemas.profile import (
    CreateProfileSchema,
)
from src.users.schemas.user import (
    CreateUserSchema,
)
from src.users.validations import (
    validate_password,
    validate_username,
)


# register_view
class RegisterUserSchema(CreateUserSchema):
    profile: CreateProfileSchema

    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "username": "basic",
                "email": "basic@basic.com",
                "password": "Password123!",
                "rewrite_password": "Password123!",
                "profile": {
                    "name": "basic",
                    "surname": "basic",
                },
            },
        }
    )


# change_email_view


# login_view
class LoginUserSchema(BaseModel):
    username: Annotated[str, BeforeValidator(validate_username)]
    password: Annotated[str, BeforeValidator(validate_password)]

    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "username": "basic",
                "password": "Password123!",
            },
        }
    )


# refresh_view
class RefreshTokenSchema(BaseModel):
    refresh_token: str

    model_config = ConfigDict(
        json_schema_extra={
            "title": "Token",
            "description": "Token model",
            "example": {
                "refresh_token": "some_refresh_token",
            },
        },
    )
