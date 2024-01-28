import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, relationship

from src.core.database import Base

if TYPE_CHECKING:
    from src.attraction.models import Attraction
    from src.auth.models import User


class Profile(Base):
    __tablename__ = "profiles"

    id: uuid.UUID = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        primary_key=True,
        nullable=False,
    )
    name: Optional[str] = Column(
        String(100),
        index=True,
    )
    surname: Optional[str] = Column(
        String(100),
        index=True,
    )
    user_id: Optional[uuid.UUID] = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(
        argument="User",
        back_populates="profile",
        foreign_keys="Profile.user_id",
    )
    attractions: Mapped[list["Attraction"]] = relationship(
        argument="Attraction",
        back_populates="profile",
        cascade="all, delete-orphan",
        uselist=True,
        foreign_keys="Attraction.profile_id",
    )

    def __repr__(self):
        return f"{self.user.email}"
