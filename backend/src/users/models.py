import uuid
from typing import TYPE_CHECKING, TypeVar

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, relationship

from src.core.database import Base

if TYPE_CHECKING:
    from src.auth.models import User

    UserType = TypeVar("UserType", bound=User)


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str] = Column(
        String(100),
        index=True,
    )
    surname: Mapped[str] = Column(
        String(100),
        index=True,
    )
    image_url: Mapped[str] = Column(
        String(255),
    )
    # One-to-one relationship with User
    user_id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
    )
    user: Mapped["UserType"] = relationship(
        "User",
        back_populates="profile",
    )
