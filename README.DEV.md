# Develop app

## environments

backend/.env

```bash
POSTGRES_HOST=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=triplane
POSTGRES_DB=postgres-triplane
POSTGRES_PORT=5432

SECRET_KEY=test
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=300
REFRESH_TOKEN_EXPIRE_DAYS=365

CORS_ORIGINS=http://localhost:8083

MINIO_HOST_URL=minio:9000
MINIO_ACCESS_KEY=superuser
MINIO_SECRET_KEY=superuser
MINIO_SECURE=False

FASTAPI_HOST=localhost
FASTAPI_PORT=8000
DEBUG=0

CACHE_STORAGE_HOST=redis
CACHE_STORAGE_PORT=6379
CACHE_STORAGE_PASSWORD=redis
CACHE_STORAGE_DB=1
CACHE_STORAGE_EXP=86400
```

### start app

```bash
docker-compose -f docker-compose.dev.yml up --build -d
docker-compose -f docker-compose.dev.yml stop

```

### debug

you can use:

```bash
docker-compose -f docker-compose.dev.yml start postgres
docker-compose -f docker-compose.dev.yml start redis
docker-compose -f docker-compose.dev.yml start minio
```

```bash
python ./backend/src/run_app.py
```
