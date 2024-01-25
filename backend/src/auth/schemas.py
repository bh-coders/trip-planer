from pydantic import BaseModel, field_validator

from src.auth.validators import email_validator, password_validator, username_validator


class UserResponse(BaseModel):
    username: str
    email: str
    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "username": "basic",
                "email": "basic@basic.com",
            },
        },
    }


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

    @field_validator(__field="username", mode="before")
    @classmethod
    def validate_username(cls, username: str) -> str:
        return username_validator(username)

    @field_validator(__field="email", mode="before")
    @classmethod
    def validate_email(cls, email: str) -> str:
        return email_validator(email)

    @field_validator(__field="password", mode="before")
    @classmethod
    def validate_password(cls, password: str) -> str:
        return password_validator(password)

    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "username": "basic",
                "email": "basic@basic.com",
                "password": "Password123!",
            },
        },
    }


class RegisterResponse(BaseModel):
    message: str
    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "message": "User registered successfully",
            },
        },
    }


class SignInRequest(BaseModel):
    username: str
    password: str

    @field_validator(__field="username", mode="before")
    @classmethod
    def validate_username(cls, username: str) -> str:
        return username_validator(username)

    @field_validator(__field="password", mode="before")
    @classmethod
    def validate_password(cls, password: str) -> str:
        return password_validator(password)

    model_config = {
        "json_schema_extra": {
            "title": "JWT",
            "description": "Token JWT request",
            "example": {
                "username": "basic",
                "password": "password123!",
            },
        },
    }


class SignInResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    model_config = {
        "json_schema_extra": {
            "title": "JWT",
            "description": "Token JWT response",
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
                "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
                "token_type": "bearer",
            },
        },
    }
