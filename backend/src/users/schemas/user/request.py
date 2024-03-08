from typing import Annotated

from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    model_validator,
)

from src.users.validations import (
    check_passwords_match,
    validate_email,
    validate_password,
    validate_username,
)


class PasswordsMatchModel(BaseModel):
    password: Annotated[str, BeforeValidator(validate_password)]
    rewrite_password: Annotated[str, BeforeValidator(validate_password)]

    @model_validator(mode="after")
    def passwords_match(self) -> "PasswordsMatchModel":
        if check_passwords_match(self.password, self.rewrite_password):
            return self


class PasswordsMatchUpdateSchema(BaseModel):
    old_password: Annotated[str, BeforeValidator(validate_password)]
    new_password: Annotated[str, BeforeValidator(validate_password)]
    rewrite_password: Annotated[str, BeforeValidator(validate_password)]

    @model_validator(mode="after")
    def passwords_match(self) -> "PasswordsMatchUpdateSchema":
        if check_passwords_match(self.new_password, self.rewrite_password):
            return self

    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "old_password": "basic@basic.com",
                "new_password": "Password123!",
                "rewrite_password": "Password123!",
            },
        }
    )


class CreateUserSchema(PasswordsMatchModel):
    username: Annotated[str, BeforeValidator(validate_username)]
    email: Annotated[str, BeforeValidator(validate_email)]
    password: Annotated[str, BeforeValidator(validate_password)]
    rewrite_password: Annotated[str, BeforeValidator(validate_password)]

    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "username": "basic",
                "email": "basic@basic.com",
                "password": "Password123!",
                "rewrite_password": "Password123!",
            },
        }
    )


# change_email_view
class UserEmailChangeSchema(BaseModel):
    new_email: Annotated[str, BeforeValidator(validate_email)]
    old_email: Annotated[str, BeforeValidator(validate_email)]
    password: Annotated[str, BeforeValidator(validate_password)]

    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "new_email": "basic@basic.com",
                "old_email": "basic@basic.com",
                "password": "Password123!",
            },
        },
    )


# change_password_view
class PasswordChangeUserModel(PasswordsMatchModel):
    old_password: Annotated[str, BeforeValidator(validate_password)]
    new_password: Annotated[str, BeforeValidator(validate_password)]
    rewrite_password: Annotated[str, BeforeValidator(validate_password)]

    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "old_password": "Password123!",
                "new_password": "Password123!",
                "rewrite_password": "Password123!",
            },
        },
    )
