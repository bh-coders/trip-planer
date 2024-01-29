import re

from email_validator import EmailNotValidError
from email_validator import validate_email as _validate_email
from fastapi import HTTPException
from pydantic import BaseModel, field_validator, model_validator

from src.auth.schemas.endpoint_schema import (
    LoginRequest,
    RefreshTokenRequest,
    RegisterRequest,
)


class PasswordModel(BaseModel):
    password: str

    @field_validator("password", mode="before")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if len(password) < 8:
            raise HTTPException(
                status_code=400,
                detail="Password must be at least 8 characters long",
            )
        if not any(char.isdigit() for char in password):
            raise HTTPException(
                status_code=400,
                detail="Password must contain at least one number",
            )
        if not any(char.isupper() for char in password):
            raise HTTPException(
                status_code=400,
                detail="Password must contain at least one uppercase letter",
            )
        if not any(char.islower() for char in password):
            raise HTTPException(
                status_code=400,
                detail="Password must contain at least one lowercase letter",
            )
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>/?~" for char in password):
            raise HTTPException(
                status_code=400,
                detail="Password must contain at least one special character",
            )
        return password


class UserModel(BaseModel):
    username: str
    email: str

    @field_validator("username", mode="before")
    @classmethod
    def validate_username(cls, username: str) -> str:
        pattern = r"^[a-zA-Z0-9_-]{3,16}$"
        if not re.match(pattern, username):
            raise HTTPException(status_code=400, detail="Invalid username")
        return username

    @field_validator("email", mode="before")
    @classmethod
    def validate_email(cls, email: str) -> str:
        try:
            _validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            raise HTTPException(status_code=400, detail="Invalid email address")
        return email


class UserCreate(UserModel, PasswordModel, RegisterRequest):
    username: str
    email: str
    password: str
    rewrite_password: str

    @model_validator(mode="after")
    def check_passwords_match(self) -> "UserCreate":
        if self.password != self.rewrite_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")
        return self


class GetUser(LoginRequest):
    username: str
    password: str


class GetToken(RefreshTokenRequest):
    refresh_token: str
