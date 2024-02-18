from typing import List

from fastapi import HTTPException, Response, UploadFile
from sqlalchemy.orm import Session

from src.db.interfaces.cloud_storage import ICloudStorage
from src.file.interfaces.repository import IRepository
from src.file.models.schemas import (
    MediaCreate,
    MediaFile,
    MediaRead,
    MediaReference,
    MediaUpdate,
)
from src.file.utils import (
    get_bucket_name,
    get_file_name,
    guess_media_type,
    read_upload_file,
)


class MediaService:
    def __init__(self, repository: IRepository, storage: ICloudStorage):
        self.repository = repository
        self.cloud_storage = storage

    def get_media_by_reference(
        self, db: Session, reference: MediaReference
    ) -> List[MediaRead]:
        reference_methods = {
            "attraction_id": lambda id: self.repository.get_by_attraction_id(db, id),
            "comment_id": lambda id: self.repository.get_by_comment_id(db, id),
            "review_id": lambda id: self.repository.get_by_review_id(db, id),
        }

        for field_name, method in reference_methods.items():
            reference_id = getattr(reference, field_name)
            if reference_id is not None:
                media_objs = method(reference_id)
                break

        if not media_objs:
            raise HTTPException(status_code=404, detail="Media not found")
        return [MediaRead(**media.as_dict()) for media in media_objs]

    def get_media_obj(self, file_id: str, db: Session) -> MediaRead:
        media_obj = self.repository.get_by_id(db, file_id)
        if not media_obj:
            raise HTTPException(status_code=404, detail="Media not found")
        return media_obj.as_dict()

    def create_media(self, db: Session, media: MediaCreate, file: UploadFile):
        try:
            bucket_name = get_bucket_name(media)
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail="Cannot provide correct reference to object: " + str(e),
            )

        try:
            content, file_size = read_upload_file(file)
            file_name = get_file_name(media)
            self.cloud_storage.upload_file(
                bucket_name, filename=file_name, file=content, file_size=file_size
            )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to upload file: {str(e)}"
            )

        media.bucket_name = bucket_name
        new_media = self.repository.create(db, media)
        if not new_media:
            raise HTTPException(status_code=400, detail="Media could not be created.")
        return Response(status_code=200, content="Media successfully created.")

    def update_media(self, db: Session, media_id: str, media: MediaUpdate) -> MediaRead:
        existing_media = self.repository.get_by_id(db, media_id)
        if not existing_media:
            raise HTTPException(status_code=404, detail="Media not found.")
        updated_media = self.repository.update(db, existing_media, media)
        if not updated_media:
            raise HTTPException(status_code=400, detail="Media could not be updated.")
        return MediaRead(**updated_media.as_dict())

    def delete_media(self, db: Session, media_id: str) -> Response:
        media_to_delete = self.repository.get_by_id(db, media_id)
        if not media_to_delete:
            raise HTTPException(status_code=404, detail="Media not found.")
        if not self.repository.delete(db, media_to_delete):
            raise HTTPException(status_code=400, detail="Media could not be deleted.")
        return Response(status_code=200, content="Media successfully deleted.")

    def get_media_file(self, media_file: MediaFile) -> Response:
        try:
            filename = media_file.file_name
            if media_file.id_object:
                filename = f"{media_file.id_object}/{media_file.file_name}"
            data = self.cloud_storage.retrieve_file(media_file.bucket_name, filename)
            mime = guess_media_type(data)
            return Response(content=data, media_type=mime)
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="File not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error") from e
