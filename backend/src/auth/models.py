from src.database import Base
from sqlalchemy import Column, String, UUID
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    username = Column(String(length=100), nullable=False)
    email = Column(String(length=100), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)

