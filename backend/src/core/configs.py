import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = int(os.getenv("DEBUG", 1))
if DEBUG:
    LOGS_DIR = BASE_DIR / "logs"
    LOGS_FILE_PATH = LOGS_DIR / "api-logs.log"

FAST_API_HOST = os.getenv("FAST_API_HOST", "localhost")
FAST_API_PORT = os.getenv("FAST_API_PORT", 8080)

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5433")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "triplane")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB", "postgres-triplane")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB_NAME}"
)

SECRET_KEY = os.getenv("SECRET_KEY", "asd123")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "300"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "365"))
MINIO_HOST_URL = os.getenv("MINIO_HOST_URL", "localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "superuser")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "superuser")
MINIO_SECURE = os.getenv("MINIO_SECURE", False) == "True"
CORS_ORIGINS_ENV = os.getenv("CORS_ORIGINS", "http://localhost:8081")
CORS_ORIGINS = CORS_ORIGINS_ENV.split(",")

CACHE_STORAGE_HOST = os.getenv("CACHE_STORAGE_HOST", "localhost")
CACHE_STORAGE_PORT = os.getenv("CACHE_STORAGE_PORT", "6379")
CACHE_STORAGE_DB = os.getenv("CACHE_STORAGE_DB", "1")
CACHE_STORAGE_PASSWORD = os.getenv("CACHE_STORAGE_PASSWORD", "redis")
CACHE_STORAGE_EXP = int(os.getenv("CACHE_STORAGE_EXP", "86400"))

GEOCODES_CO_API_KEY = os.getenv("GEOCODES_CO_API_KEY", "")
