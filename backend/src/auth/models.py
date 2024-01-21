from src.core.database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(length=100), nullable=False)
    email = Column(String(length=100), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)

