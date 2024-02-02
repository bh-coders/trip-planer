from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Token(BaseModel):
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
