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

    # TODO preload file (maybe) will change to utils
    bucket_name: Optional[str] = Field(default="users")
    image_file_data: Tuple[Any, str, int] = Field(default=None)

    @model_validator(mode="after")
    def set_image_file_data(self):
        with urllib.request.urlopen(self.image_url) as response:
            contents = response.read()
            file_io = io.BytesIO(contents)
            filename = self.image_url.split("/")[-1]
            file_size = len(contents)
        self.image_file_data = file_io, filename, file_size
        return self
