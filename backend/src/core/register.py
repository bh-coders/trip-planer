import logging

from fastapi import FastAPI

from src.attraction.routes.router import router as attraction_router
from src.core.logger import LoggerSetup
from src.database import Base, engine
from src.middleware.log_middleware import LoggingMiddleware


def _init_app(version: str) -> FastAPI:
    Base.metadata.create_all(bind=engine)
    return FastAPI(version=version, debug=True)


def _read_version() -> str:
    with open("src/VERSION.txt", "r") as version_file:
        version = version_file.read()
        return version


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


def register_router(app: FastAPI):
    app.include_router(attraction_router, prefix="/attractions")


def register_logger() -> LoggerSetup:
    return LoggerSetup()
