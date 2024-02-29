from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict

from src.users.validations import (
    validate_image_url,
    validate_name,
    validate_surname,
)


class CreateProfileModel(BaseModel):
    name: Annotated[str, BeforeValidator(validate_name)]
    surname: Annotated[str, BeforeValidator(validate_surname)]
    image_url: Annotated[str, BeforeValidator(validate_image_url)]


class UpdateProfileModel(CreateProfileModel):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "Profile update model",
            "description": "Updated profile model",
            "example": {
                "name": "basic_new",
                "surname": "basic_new",
                "image_url": (
                    "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffreepngimg.com%2Fthumb"
                    "%2Fdog%2F7-dog-png-image-thumb.png"
                ),
            },
        }
    )
