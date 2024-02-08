from pydantic import ConfigDict

from src.core.schemas import Message


# email_change_view
class EmailChangeEndpoint(Message):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "message": "Email changed successfully",
            },
        }
    )


# password_change_view
class PasswordChangeEndpoint(Message):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "message": "Password changed successfully",
            },
        }
    )


# delete_view
class DeleteEndpoint(Message):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "message": "User deleted successfully",
            },
        }
    )
