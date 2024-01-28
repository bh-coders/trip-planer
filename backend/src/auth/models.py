import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import UUID, Boolean, Column, DateTime, String
from sqlalchemy.orm import Mapped, relationship

from src.core.database import Base

if TYPE_CHECKING:
    from src.users.models import Profile


class User(Base):
    __tablename__ = "users"

    id: uuid.UUID = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    username: str = Column(String(length=100), nullable=False)
    email: str = Column(String(length=100), unique=True, nullable=False)
    password: str = Column(String(length=255), nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow())
    updated_at: Optional[datetime] = Column(
        DateTime,
        nullable=True,
    )
    is_active: bool = Column(
        Boolean,
        default=False,
    )
    is_superuser: bool = Column(
        Boolean,
        default=False,
    )

    profile: Mapped["Profile"] = relationship(
        argument="Profile",
        uselist=False,
        back_populates="user",
        cascade="all, delete-orphan",
        foreign_keys="Profile.user_id",
    )
