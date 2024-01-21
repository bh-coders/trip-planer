from src.database import Base
from sqlalchemy import Column, Integer, String, JSON, Float


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

