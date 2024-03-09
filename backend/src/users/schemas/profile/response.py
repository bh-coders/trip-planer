from pydantic import BaseModel, ConfigDict

from src.common.schemas.message_schemas import MessageSchema


# edit_view
class ProfileUpdateSuccessSchema(MessageSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "Profile update",
            "description": "Profile model update",
            "example": {
                "message": "Profile updated successfully",
            },
        }
    )


# get_view
class ProfileDetailSchema(BaseModel):
    name: str
    surname: str

    model_config = ConfigDict(
        json_schema_extra={
            "title": "Profile model",
            "description": "Get profile model",
            "example": {
                "name": "basic",
                "surname": "basic",
            },
        }
    )
