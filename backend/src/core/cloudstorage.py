import io
import logging
import os
from mimetypes import guess_type
from typing import BinaryIO, Union

from minio import Minio, S3Error
from minio.datatypes import Bucket, Object

logger = logging.getLogger(__name__)


class CloudStorage:
    def __init__(
        self,
        api_url: str = None,
        access_key: str = None,
        secret_key: str = None,
        secure: bool = None,
    ):
        self.url = api_url or os.getenv("MINIO_HOST_URL")
        self.access_key = access_key or os.getenv("MINIO_ACCESS_KEY")
        self.secret_key = secret_key or os.getenv("MINIO_SECRET_KEY")
        self.secure: bool = secure or os.getenv("MINIO_SECURE", False) == "True"
        self.client = self._connect_to_cloudstorage()

    def _connect_to_cloudstorage(self) -> Minio:
        try:
            client = Minio(
                endpoint=self.url,
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=self.secure,
            )
            self._check_connection(client)
            return client
        except Exception as e:
            logger.error(f"Failed to connect to MinIO server: {e}")
            raise ConnectionError(f"Unable to connect to MinIO server: {e}")

    def _check_connection(self, client: Minio) -> None:
        try:
            client.list_buckets()
        except S3Error as e:
            logger.error(f"MinIO S3 Error: {e}")
            raise
        except Exception as e:
            logger.error(f"General error when checking connection to MinIO: {e}")
            raise

    def create_bucket(self, bucket_name: str) -> str:
        try:
            if not self.client.bucket_exists(bucket_name):
                self.client.make_bucket(bucket_name)
                return f"Bucket '{bucket_name}' created successfully."
            else:
                return f"Bucket '{bucket_name}' already exists."
        except S3Error as e:
            logger.error(f"Error creating bucket: {e}")
            return f"Failed to create bucket '{bucket_name}': {e}"

    def check_bucket(self, bucket_name: str) -> bool:
        return self.client.bucket_exists(bucket_name)

    def list_buckets(self) -> Union[list[Bucket], str]:
        try:
            return self.client.list_buckets()
        except S3Error as e:
            logging.error(f"Error listing buckets: {e}")
            return f"Failed to list buckets: {e}"

    def list_bucket_objects(
        self, bucket_name: str, prefix: str = None, recursive: bool = False
    ) -> list[Object] | str:
        try:
            return self.client.list_objects(
                bucket_name, prefix=prefix, recursive=recursive
            )
        except S3Error as e:
            logger.error(f"Error listing objects in bucket '{bucket_name}': {e}")
            return f"Failed to list objects in bucket '{bucket_name}': {e}"

    def upload_file(
        self,
        bucket_name: str,
        filename: str,
        file: BinaryIO,
        file_size: int,
        content_type: str = None,
    ) -> str:
        if not self.client.bucket_exists(bucket_name):
            return f"Bucket '{bucket_name}' does not exist."

        content_type = (
            content_type or guess_type(filename)[0] or "application/octet-stream"
        )

        try:
            self.client.put_object(bucket_name, filename, file, file_size, content_type)
            return f"File '{filename}' uploaded successfully to bucket '{bucket_name}'."
        except S3Error as e:
            logger.error(
                f"Error uploading file '{filename}' to bucket '{bucket_name}': {e}"
            )
            return f"Failed to upload file '{filename}' to bucket '{bucket_name}': {e}"

    def retrieve_file(
        self, bucket_name: str, filename: str
    ) -> str | bytes | tuple[str]:
        if not self.client.bucket_exists(bucket_name):
            return f"Bucket '{bucket_name}' does not exist."
        try:
            response = self.client.get_object(bucket_name, filename)
            with response:
                data_stream = io.BytesIO(response.data)
                data = data_stream.read()
            return data

        except S3Error as e:
            logger.error(
                f"Error retrieving file '{filename}' from bucket '{bucket_name}': {e}"
            )
            return (
                f"Failed to retrieve file '{filename}' from bucket '{bucket_name}': {e}",
            )
