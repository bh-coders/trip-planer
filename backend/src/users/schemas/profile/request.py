import io
import urllib.request
import uuid
from typing import Annotated, Any, Optional, Tuple

from fastapi import File, UploadFile
from pydantic import BaseModel, BeforeValidator, Field, model_validator

from src.users.validations import (
    validate_image_url,
    validate_name,
    validate_surname,
)


class CreateProfileModel(BaseModel):
    name: Annotated[str, BeforeValidator(validate_name)]
    surname: Annotated[str, BeforeValidator(validate_surname)]
    image_url: Annotated[str, BeforeValidator(validate_image_url)]
