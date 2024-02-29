import uuid

from fastapi import APIRouter

from src.file.services import _load_file_from_cloud

file_router = APIRouter()


@file_router.get("/{bucket_name}/{object_id}/{filename}")
def open_file_from_cloud_storage(
    bucket_name: str,
    object_id: int | str | uuid.UUID,
    filename: str,
):
    return _load_file_from_cloud(filename, bucket_name, object_id)


@file_router.get("/{bucket_name}/{filename}")
def open_default_file_from_cloud_storage(
    bucket_name: str,
    filename: str,
):
    return _load_file_from_cloud(filename, bucket_name)
