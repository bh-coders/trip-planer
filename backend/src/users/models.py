import uuid
from datetime import datetime
from typing import Annotated, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from src.attraction.models import Attraction
from src.core.database import Base
from src.users.utils import email_is_valid


class CreatedUpdatedMixin(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        index=True,
        default=datetime.utcnow,
    )
    updated_at: Mapped[datetime] = mapped_column(
        index=True,
    )


class User(CreatedUpdatedMixin):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    name: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )
    surname: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )
    email: Mapped[str] = mapped_column(
        String(100),
        index=True,
        unique=True,
        nullable=False,
    )
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    username: Mapped[str] = mapped_column(
        String(100),
        index=True,
        unique=True,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        default=False,
    )

    is_superuser: Mapped[bool] = mapped_column(
        default=False,
    )
    attraction: Mapped[
        List[Annotated[Attraction, "src.attraction.models.Attraction"]]
    ] = relationship(
        back_populates="users",
    )

    def __repr__(self):
        return f"{self.email}"

    @validates("email")
    def validate_email(self, email: email) -> email:
        if not email_is_valid(email=email):
            raise ValueError("Invalid email address")
        return email

    @validates("password")
    def validate_password(self, password: password) -> password:
        if password:
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters long")
            return password
        raise ValueError("No password provided")
