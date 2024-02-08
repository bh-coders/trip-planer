from pydantic import BaseModel, ConfigDict

from src.core.schemas import Message


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "access_token": "test_token_access",
                "refresh_token": "test_token_refresh",
                "token_type": "Bearer",
            },
        }
    )


# register_view
class RegisterEndpoint(Message):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "message": "User registered successfully",
            },
        }
    )


# login_view
class LoginEndpoint(Token):
    pass


# refresh_view
class RefreshTokenEndpoint(Token):
    pass
