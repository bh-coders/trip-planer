from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.core.configs import (
    SQLALCHEMY_DATABASE_URL,
)
from src.db.cache_storage import CacheHandler, RedisStorage

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_session():
    db = next(get_db())
    try:
        return db
    finally:
        db.close()


def get_redis():
    redis_storage = RedisStorage()
    return CacheHandler(pool_storage=redis_storage)
