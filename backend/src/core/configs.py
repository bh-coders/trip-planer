import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB", "postgres")
SECRET_KEY = os.getenv("SECRET_KEY", "asd123")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "300"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "365"))
MINIO_HOST_URL = str(os.getenv("MINIO_HOST_URL"))
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_SECURE = os.getenv("MINIO_SECURE", False) == "True"
CORS_ORIGINS_ENV = os.getenv("CORS_ORIGINS", "http://localhost:8081")
CORS_ORIGINS = CORS_ORIGINS_ENV.split(",")

CACHE_STORAGE_HOST = os.getenv("CACHE_STORAGE_HOST", "localhost")
CACHE_STORAGE_PORT = os.getenv("CACHE_STORAGE_PORT", "6379")
CACHE_STORAGE_DB = os.getenv("CACHE_STORAGE_DB", "1")
CACHE_STORAGE_PASSWORD = os.getenv("CACHE_STORAGE_PASSWORD", "jp2")
CACHE_STORAGE_EXP = int(os.getenv("CACHE_STORAGE_EXP", "86400"))
