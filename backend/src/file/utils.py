import io

import magic
from fastapi import UploadFile

from src.db.cloud_storage import BucketNames
from src.file.models.schemas import MediaCreate


def guess_media_type(data: bytes) -> str:
    """
    Determine the MIME type of the given byte data.

    This function uses the `magic` library to analyze the bytes of the input data and
    returns the corresponding MIME type as a string. The MIME type can be used to identify
    the format of the data (e.g., 'image/jpeg', 'text/plain').

    Parameters:
    - data (bytes): The data whose MIME type needs to be determined.

    Returns:
    - str: The MIME type of the input data.
    """
    mime = magic.Magic(mime=True)
    return mime.from_buffer(data)


def get_bucket_name(media_create: MediaCreate) -> str:
    if media_create.attraction_id:
        return BucketNames.ATTRACTIONS.value
    elif media_create.comment_id:
        return BucketNames.COMMENTS.value
    elif media_create.review_id:
        return BucketNames.REVIEWS.value
    else:
        raise ValueError("No valid reference ID provided for bucket selection.")


def get_file_name(media_create: MediaCreate) -> str:
    object_attrs = [
        media_create.attraction_id,
        media_create.comment_id,
        media_create.review_id,
    ]
    for object_id in object_attrs:
        if object_id is not None:
            return f"{object_id}/{media_create.file_name}"
    return media_create.file_name


def read_upload_file(file: UploadFile) -> (io.BytesIO, int):
    file_io = io.BytesIO()

    contents = file.file.read()
    file_io.write(contents)
    file_size = len(contents)

    file_io.seek(0)

    return file_io, file_size
