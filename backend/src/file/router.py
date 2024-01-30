from fastapi import APIRouter, Depends

from src.core.interceptors.auth_interceptor import verify_jwt
from src.file.services import _load_file_from_cloud

file_router = APIRouter()


@file_router.get("/{bucket_name}/{object_id}/{filename}")
def open_file_from_cloud_storage(
    bucket_name: str,
    object_id: int,
    filename: str,
    is_token_valid: bool = Depends(verify_jwt),
):
    return _load_file_from_cloud(filename, bucket_name, object_id)


@file_router.get("/{bucket_name}/{filename}")
def open_default_file_from_cloud_storage(
    bucket_name: str, filename: str, is_token_valid: bool = Depends(verify_jwt)
):
    return _load_file_from_cloud(filename, bucket_name)
