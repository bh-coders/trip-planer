from pydantic import BaseModel, ConfigDict

from src.common.schemas.message_schemas import Message


# edit_view
class ProfileUpdateResponse(Message):
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
class ProfileDetailResponse(BaseModel):
    name: str
    surname: str
    image_base64: str

    model_config = ConfigDict(
        json_schema_extra={
            "title": "Profile model",
            "description": "Get profile model",
            "example": {
                "name": "basic",
                "surname": "basic",
                "image_base64": "some_base64_string",
            },
        }
    )
