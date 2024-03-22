from pydantic import ConfigDict

from src.common.schemas.message_schemas import MessageSchema


# email_change_view
class EmailChangeSuccessSchema(MessageSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model change email",
            "example": {
                "message": "Email changed successfully",
            },
        }
    )


# password_change_view
class PasswordChangeSuccessSchema(MessageSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "Password success model",
            "example": {
                "message": "Password changed successfully",
            },
        }
    )


# delete_view
class DeleteSuccessSchema(MessageSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "User",
            "description": "User model",
            "example": {
                "message": "User deleted successfully",
            },
        }
    )
