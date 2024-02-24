from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src.attraction.routes.router import router as attraction_router
from src.auth.routes import auth_router
from src.core.configs import BASE_DIR, CORS_ORIGINS
from src.core.logger import LoggerSetup
from src.core.utils import start_events
from src.db.cache_storage import CacheHandler, RedisStorage
from src.db.cloudstorage import CloudStorage
from src.db.database import Base, engine, get_db
from src.file.router import file_router
from src.middleware.log_middleware import LoggingMiddleware
from src.threads.routes.router import threads_router
from src.users.repositories import ProfileRepository
from src.users.routes import user_router
from src.users.services import ProfileService


def _init_app(version: str) -> FastAPI:
    Base.metadata.create_all(bind=engine)
    return FastAPI(version=version, debug=True)


def _read_version() -> str:
    """
    Read the Rest API version from a VERSION.txt file.

    This function attempts to read the version of the Rest API from a text file named
    VERSION.txt located in the 'src' directory. If the file is found, it reads the version,
    trims any leading or trailing whitespace, and returns the version string. If the file
    is not found, it creates the file, writes a default version '0.0.0' into it, and returns
    this default version.

    Returns:
    - str: The version string read from the file, or the default '0.0.0' if the file does not exist.
    """
    try:
        with open(BASE_DIR / "src" / "VERSION.txt", "r") as version_file:
            version = version_file.read()
            return version.strip()
    except FileNotFoundError:
        with open(BASE_DIR / "src" / "VERSION.txt", "w") as version_file:
            version_file.write("0.0.0")
        return "0.0.0"


def register_app():
    VERSION = _read_version()
    # config = config.Settings() if we create Settings object we can put this to init_app
    app = _init_app(version=VERSION)

    register_router(app)
    # we can initialize all configurations, middlewares, cors etc. here
    register_logger()
    register_middleware(app)
    return app


def register_middleware(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def startup_events():
    redis_storage = RedisStorage()
    cloud_storage = CloudStorage()
    cache_handler = CacheHandler(redis=redis_storage)

    services = [
        ProfileService(
            repository=ProfileRepository(),
            cache_handler=cache_handler,
            cloud_storage=cloud_storage,
        ),
    ]
    with Session(bind=engine) as db:
        for service in services:
            service.get_sqlalchemy_session(db=db)

    start_events(services=services)


def register_router(app: FastAPI):
    app.add_event_handler(
        "startup",
        startup_events,
    )

    app.include_router(attraction_router, prefix="/attractions", tags=["Attractions"])
    app.include_router(auth_router, prefix="/auth", tags=["Authorizations"])
    app.include_router(user_router, prefix="/me", tags=["Users"])
    app.include_router(file_router, prefix="/files", tags=["Files"])
    app.include_router(threads_router, prefix="/threads", tags=["Threads"])


def register_logger() -> LoggerSetup:
    return LoggerSetup()
