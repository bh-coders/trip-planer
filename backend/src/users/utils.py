import base64
import io
import urllib.request
import uuid
from mimetypes import guess_type
from typing import Optional

from src.db.cloudstorage import CloudStorage

cloud_storage = CloudStorage()


def prepare_profile_image(
    image_url: str,
    user_id: uuid.UUID,
    bucket_name: str = "users",
):
    image_type = "jpeg"
    with urllib.request.urlopen(image_url) as response:
        contents = response.read()
        file = io.BytesIO(contents)
        filename = f"{user_id}/avatar.{image_type}"
        file_size = len(contents)
        content_type = guess_type(image_url)[0] or "application/octet-stream"
    return {
        "bucket_name": bucket_name,
        "file": file,
        "filename": filename,
        "file_size": file_size,
        "content_type": content_type,
    }


def get_profile_image(
    user_id: uuid.UUID,
    bucket_name: str = "users",
) -> Optional[str]:
    image_type = "jpeg"
    filename = f"{user_id}/avatar.{image_type}"
    image = cloud_storage.retrieve_file(
        bucket_name=bucket_name,
        filename=filename,
    )
    if image:
        return f"data:image/{image_type};base64," + base64.b64encode(image).decode(
            "utf-8"
        )
    return None


def delete_profile_image(
    user_id: uuid.UUID,
    bucket_name: str = "users",
):
    image_type = "jpeg"
    filename = f"{user_id}/avatar.{image_type}"
    cloud_storage.delete_file(
        bucket_name=bucket_name,
        filename=filename,
    )
