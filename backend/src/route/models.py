import uuid
from typing import TypeVar

from sqlalchemy import Column, String, UUID, Table, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.auth.models import User
from src.attraction.models import Attraction
from src.db.database import Base


class Route(Base):
    __tablename__ = "routes"

    AttractionTypeList = TypeVar("AttractionTypeList", bound=list[Attraction])
    UserTypeList = TypeVar("UserTypeList", bound=list[User])

    user_route_table = Table(
        'user_route', Base.metadata,
        Column('user_id', ForeignKey('users.id', ondelete="CASCADE"), primary_key=True),
        Column('route_id', ForeignKey('routes.id', ondelete="CASCADE"), primary_key=True)
    )

    id: Mapped[UUID] = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)

    name: Mapped[str] = Column(String(length=100), unique=True)
    description: Mapped[str] = Column(String(length=100))

    users: Mapped["UserTypeList"] = relationship("User", secondary="user_route_table", back_populates="route")
    attractions: Mapped["AttractionTypeList"] = relationship("Attraction", back_populates="route")
