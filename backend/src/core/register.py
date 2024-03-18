from src.attraction.models import *  # noqa
from src.file.models.media_models import *  # noqa
from src.threads.models import *  # noqa

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.attraction.routes.router import router as attraction_router
from src.auth.routes import auth_router
from src.core.configs import BASE_DIR, CORS_ORIGINS
from src.core.logger import LoggerSetup
from src.db.database import engine, Base
from src.file.routers.media_router import media_router
from src.middleware.log_middleware import LoggingMiddleware
from src.threads.routes.router import threads_router
from src.users.routes import profile_router, user_router


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
    version = _read_version()
    app = _init_app(version=version)

    register_router(app)
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


def register_router(app: FastAPI):
    app.include_router(attraction_router, prefix="/attractions", tags=["Attractions"])
    app.include_router(auth_router, prefix="/auth", tags=["Authorizations"])
    app.include_router(user_router, prefix="/users", tags=["Users"])
    app.include_router(profile_router, prefix="/profiles", tags=["Profiles"])
    app.include_router(media_router, prefix="/media", tags=["Media"])
    app.include_router(threads_router, prefix="/threads", tags=["Threads"])


def register_logger() -> LoggerSetup:
    return LoggerSetup()
