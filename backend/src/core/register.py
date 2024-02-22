from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# we need to import all models to create tables in database
from src.attraction.models import *  # noqa
from src.route.models import *
from src.file.models.media_models import *  # noqa
from src.threads.models import *  # noqa

from src.attraction.routes.router import router as attraction_router
from src.route.routes.router import router as route_router
from src.auth.routes import auth_router
from src.core.configs import CORS_ORIGINS
from src.core.logger import LoggerSetup
from src.db.database import engine
from src.file.routers.media_router import media_router
from src.middleware.log_middleware import LoggingMiddleware
from src.threads.routes.router import threads_router
from src.users.routes import router as users_router


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
        with open("src/VERSION.txt", "r") as version_file:
            version = version_file.read()
            return version.strip()
    except FileNotFoundError:
        with open("src/VERSION.txt", "w") as version_file:
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


def register_router(app: FastAPI):
    app.include_router(attraction_router, prefix="/attractions", tags=["Attractions"])
    app.include_router(route_router, prefix="/routes", tags=["Routes"])
    app.include_router(auth_router, prefix="/auth", tags=["Authorizations"])
    app.include_router(users_router, prefix="/me", tags=["Users"])
    app.include_router(media_router, prefix="/media", tags=["Media"])
    app.include_router(threads_router, prefix="/threads", tags=["Threads"])


def register_logger() -> LoggerSetup:
    return LoggerSetup()
