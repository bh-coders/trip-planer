## Develop app

### environments
- this get environments from backend/.env and override it with .env.local in containers 

backend/.env.local

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
DEBUG=1
PYTHONBREAKPOINT=pdb.set_trace

CACHE_STORAGE_HOST=redis
CACHE_STORAGE_PORT=6379
CACHE_STORAGE_PASSWORD=redis
CACHE_STORAGE_DB=0
CACHE_STORAGE_EXP=86400

```

### build app

```bash
docker-compose --profile dev up --build -d
docker-compose --profile dev stop
```

### debug with docker pdb++

```bash
docker-compose run --rm --service-ports backend
```

or

```bash
./commands/debug.sh
```

### run containers to vscode or pycharm ide then step debug

```bash
docker-compose --profile dev-less start
```

### debug with vscode
- add in project dir ".vscode/launch.json"

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "FastAPI",
            "cwd": "${workspaceFolder}/backend",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app",
                "--host",
                "127.0.0.1",
                "--port",
                "8000",
                "--reload"
            ],
            "envFile": "${workspaceFolder}/backend/.env"
        },
        {
            "name": "FastAPI local",
            "cwd": "${workspaceFolder}/backend",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app",
                "--host",
                "127.0.0.1",
                "--port",
                "8080",
                "--reload"
            ]
        }
    ]
}
```

### debug with pycharm

```bash
python ./backend/src/run_app.py
```