import uuid

import magic
from fastapi import HTTPException, Response

from src.core.cloudstorage import CloudStorage


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


def _load_file_from_cloud(filename: str, bucket: str, id_object:  int | str | uuid.UUID | None = None) -> Response:
    try:
        cloud_storage = CloudStorage()
        full_filename = f"{filename}"
        if id_object:
            full_filename = f"{id_object}/{full_filename}"
        data = cloud_storage.retrieve_file(
            bucket, full_filename
        )
        mime = guess_media_type(data)
        return Response(content=data, media_type=mime)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error") from e
