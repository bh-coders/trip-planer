import uuid
from datetime import datetime

from sqlalchemy import UUID, Boolean, Column, DateTime, String
from sqlalchemy.orm import relationship

from src.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    username = Column(String(length=100), nullable=False, unique=True)
    email = Column(String(length=100), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(
        DateTime,
        nullable=True,
    )
    is_active = Column(
        Boolean,
        default=False,
    )
    is_superuser = Column(
        Boolean,
        default=False,
    )
    # One-to-one relationship with Profile
    profile = relationship(
        argument="Profile",
        uselist=False,
        back_populates="user",
        cascade="all, delete-orphan",
        foreign_keys="Profile.user_id",
    )
    # One-to-many relationship with Attraction
    attractions = relationship("Attraction", back_populates="user")
