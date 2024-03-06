from pydantic import ConfigDict

from src.common.schemas.message_schemas import Message


# email_change_view
class EmailChangeSuccessSchema(Message):
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
class PasswordChangeSuccessSchema(Message):
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
class DeleteSuccessSchema(Message):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "message": "User deleted successfully",
            },
        }
    )
