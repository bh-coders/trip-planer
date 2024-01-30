import magic
from fastapi import HTTPException, Response

from src.core.cloudstorage import CloudStorage


def guess_media_type(data: bytes) -> str:
    mime = magic.Magic(mime=True)
    return mime.from_buffer(data)


def _load_file_from_cloud(filename: str, bucket: str, id_object: int | str | None = None) -> Response:
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
