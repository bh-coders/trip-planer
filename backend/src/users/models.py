from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from src.core.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
    )
    name = Column(
        String(100),
        index=True,
    )
    surname = Column(
        String(100),
        index=True,
    )
    # One-to-one relationship with User
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )
    user = relationship(
        "User",
        back_populates="profile",
    )
