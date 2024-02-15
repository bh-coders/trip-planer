import io
import urllib.request
import uuid
from mimetypes import guess_type


def prepare_profile_image(
    image_url: str,
    user_id: uuid.UUID,
    bucket_name: str = "users",
):
    with urllib.request.urlopen(image_url) as response:
        contents = response.read()
        file = io.BytesIO(contents)
        filename = f"{user_id}/avatar.{image_url.split('.')[-1]}"
        file_size = len(contents)
        content_type = guess_type(image_url)[0] or "application/octet-stream"
    return {
        "bucket_name": bucket_name,
        "file": file,
        "filename": filename,
        "file_size": file_size,
        "content_type": content_type,
    }
