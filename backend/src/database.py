from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configs import (
    POSRGRES_HOST,
    POSRGRES_PORT,
    POSTGRES_DB_NAME,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
)

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSRGRES_HOST}:{POSRGRES_PORT}/{POSTGRES_DB_NAME}"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Maybe we should move it someweher, idk
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
