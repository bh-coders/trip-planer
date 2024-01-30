from pydantic import BaseModel


class RegisterRequest(BaseModel):
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
        }
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


class LoginRequest(BaseModel):
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


class RefreshTokenRequest(BaseModel):
    model_config = {
        "json_schema_extra": {
            "title": "Token",
            "description": "Token model",
            "example": {
                "refresh_token": "some_refresh_token",
            },
        },
    }


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

    model_config = {
        "json_schema_extra": {
            "title": "User",
            "description": "User model",
            "example": {
                "access_token": "test_token_access",
                "refresh_token": "test_token_refresh",
                "token_type": "Bearer",
            },
        },
    }


class LoginResponse(TokenResponse):
    pass


class RefreshTokenResponse(TokenResponse):
    pass
