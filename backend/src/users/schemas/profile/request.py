from typing import Annotated

from pydantic import BaseModel, BeforeValidator, ConfigDict

from src.users.validations import (
    validate_name,
    validate_surname,
)


class CreateProfileSchema(BaseModel):
    name: Annotated[str, BeforeValidator(validate_name)]
    surname: Annotated[str, BeforeValidator(validate_surname)]


class ProfileUpdateSchema(CreateProfileSchema):
    model_config = ConfigDict(
        json_schema_extra={
            "title": "Profile update model",
            "description": "Updated profile model",
            "example": {
                "name": "basic_new",
                "surname": "basic_new",
            },
        }
    )
