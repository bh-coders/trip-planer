import uuid
from typing import TYPE_CHECKING, TypeVar

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, relationship

from src.db.database import Base

if TYPE_CHECKING:
    from src.users.models.user_model import User

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
    # One-to-one relationship with User
    user_id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
    )
    user: Mapped["UserType"] = relationship(
        "User",
        back_populates="profile",
    )

    def as_dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "surname": self.surname,
            "user_id": str(self.user_id),
        }
