
from pydantic import BaseModel


class Message(BaseModel):
    detail: str


class Response500(BaseModel):
    model_config = {
        "json_schema_extra": {
            "title": "Server error",
            "description": "Server error",
            "example": {
                "detail": "Server error",
            },
        },
    }


class Response404(BaseModel):
    model_config = {
        "json_schema_extra": {
            "title": "Not found",
            "description": "Not found",
            "example": {
                "detail": "Not found",
            },
        },
    }
