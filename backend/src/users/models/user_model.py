import uuid
from datetime import datetime
from typing import TYPE_CHECKING, TypeVar

from sqlalchemy import UUID, Boolean, Column, DateTime, String
from sqlalchemy.orm import Mapped, relationship

from src.db.database import Base

if TYPE_CHECKING:
    from src.attraction.models import Attraction
    from src.users.models import Profile

    ProfileType = TypeVar("ProfileType", bound=Profile)
    AttractionType = TypeVar("AttractionType", bound=Attraction)
    AttractionTypeList = TypeVar("AttractionTypeList", bound=list[Attraction])


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    username: Mapped[str] = Column(String(length=100), unique=True)
    email: Mapped[str] = Column(String(length=100), unique=True)
    password: Mapped[str] = Column(String(length=255))
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.utcnow())
    updated_at: Mapped[datetime] = Column(
        DateTime,
        nullable=True,
    )
    is_active: Mapped[bool] = Column(
        Boolean,
        default=False,
    )
    is_superuser: Mapped[bool] = Column(
        Boolean,
        default=False,
    )
    # One-to-one relationship with Profile
    profile: Mapped["ProfileType"] = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete",
    )
    # One-to-many relationship with Attraction
    attractions: Mapped["AttractionTypeList"] = relationship(
        "Attraction",
        back_populates="user",
        uselist=True,
        cascade="all, delete",
    )

    def as_dict(self):
        return {
            c.name: str(getattr(self, c.name))
            if c.name == "id"
            else getattr(self, c.name)
            for c in self.__table__.columns
            if c.name != "password"
            and c.name != "created_at"
            and c.name != "updated_at"
        }

    def __repr__(self):
        return f"<User {self.username}>"

    def __str__(self):
        return self.username
