import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, File, Form, Response, UploadFile
from sqlalchemy.orm import Session

from src.core.interceptors.auth_interceptor import verify_jwt
from src.db.cloud_storage import CloudStorage
from src.db.database import get_db
from src.file.models.schemas import (
    MediaCreate,
    MediaFile,
    MediaRead,
    MediaReference,
    MediaUpdate,
)
from src.file.repositories.media_repository import MediaRepository
from src.file.services.media_service import MediaService

media_router = APIRouter()

media_repository = MediaRepository()
cloud_storage = CloudStorage()
media_service = MediaService(repository=media_repository, storage=cloud_storage)


@media_router.post("/create", dependencies=[Depends(verify_jwt)])
def create_media(
    file: UploadFile = File(...),
    attraction_id: Optional[int] = Form(None),
    review_id: Optional[uuid.UUID] = Form(None),
    comment_id: Optional[uuid.UUID] = Form(None),
    db: Session = Depends(get_db)
) -> Response:
    media_create = MediaCreate(
        attraction_id=attraction_id,
        review_id=review_id,
        comment_id=comment_id,
        file_name=file.filename,
        file_type=file.content_type,
    )
    return media_service.create_media(db, media_create, file)


@media_router.get("/{media_id}", dependencies=[Depends(verify_jwt)])
def get_media(
    media_id: str,
    db: Session = Depends(get_db)
) -> List[MediaRead]:
    return media_service.get_media_obj(media_id, db)


@media_router.get("/by-attraction/{attraction_id}", dependencies=[Depends(verify_jwt)])
def get_media_by_attraction(
    attraction_id: int,
    db: Session = Depends(get_db)
) -> List[MediaRead]:
    return media_service.get_media_by_reference(
        db, MediaReference(attraction_id=attraction_id)
    )


@media_router.get("/by-comment/{comment_id}", dependencies=[Depends(verify_jwt)])
def get_media_by_comment(
    comment_id: str,
    db: Session = Depends(get_db)
) -> List[MediaRead]:
    return media_service.get_media_by_reference(
        db, MediaReference(comment_id=comment_id)
    )


@media_router.get("/by-review/{review_id}", dependencies=[Depends(verify_jwt)])
def get_media_by_review(
    review_id: str,
    db: Session = Depends(get_db)
) -> List[MediaRead]:
    return media_service.get_media_by_reference(db, MediaReference(review_id=review_id))


@media_router.patch("/{media_id}/update", dependencies=[Depends(verify_jwt)])
def update_media(
    media_id: str,
    media_update: MediaUpdate,
    db: Session = Depends(get_db)
) -> MediaRead:
    return media_service.update_media(db, media_id, media_update)


@media_router.delete("/{media_id}/delete", dependencies=[Depends(verify_jwt)])
def delete_media(
    media_id: str,
    db: Session = Depends(get_db)
) -> Response:
    return media_service.delete_media(db, media_id)


@media_router.get("/{bucket_name}/{object_id}/{filename}", dependencies=[Depends(verify_jwt)])
def open_media_from_cloud_storage(
    bucket_name: str,
    object_id: int | str | uuid.UUID,
    filename: str
):
    return media_service.get_media_file(
        MediaFile(
            bucket_name=bucket_name,
            file_name=filename,
            id_object=object_id,
        )
    )


@media_router.get("/{bucket_name}/{filename}", dependencies=[Depends(verify_jwt)])
def open_default_media_from_cloud_storage(
    bucket_name: str, filename: str
):
    return media_service.get_media_file(
        MediaFile(bucket_name=bucket_name, file_name=filename)
    )
