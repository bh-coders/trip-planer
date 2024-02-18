from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    JSON,
    UUID,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
    select,
)
from sqlalchemy.orm import Mapped, column_property, relationship

from src.db.database import Base
from src.threads.models import Review


class Attraction(Base):
    __tablename__ = "attractions"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(255))
    description: Mapped[str] = Column(String)
    longitude: Mapped[float] = Column(Float)
    latitude: Mapped[float] = Column(Float)
    open_hours: Mapped[Optional[dict]] = Column(JSON, nullable=True)
    address: Mapped[str] = Column(String)
    city: Mapped[str] = Column(String)
    country: Mapped[str] = Column(String)
    category: Mapped[str] = Column(String)

    # Many-to-one relationship with User
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )
    user = relationship("User", back_populates="attractions")
    media = relationship(
        "Media", back_populates="attraction", cascade="all, delete-orphan"
    )

    rating: Mapped[Decimal] = column_property(
        select(func.coalesce(func.avg(Review.rating), 0))
        .where(Review.attraction_id == id)
        .correlate_except(Review)
        .scalar_subquery()
    )

    time_spent: Mapped[Decimal] = column_property(
        select(func.coalesce(func.avg(Review.time_spent), 0))
        .where(Review.attraction_id == id)
        .correlate_except(Review)
        .scalar_subquery()
    )

    price: Mapped[Decimal] = column_property(
        select(func.coalesce(func.avg(Review.price), 0))
        .where(Review.attraction_id == id)
        .correlate_except(Review)
        .scalar_subquery()
    )

    visits: Mapped[Decimal] = column_property(
        select(func.coalesce(func.count(Review.id), 0))
        .where(Review.attraction_id == id)
        .correlate_except(Review)
        .scalar_subquery()
    )

    def as_dict(self):
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        decimal_fields = ["price", "rating", "time_spent", "visits"]
        for field in decimal_fields:
            value = getattr(self, field, None)
            if isinstance(value, Decimal):
                data[field] = float(value)
            elif value is not None:
                data[field] = value
        data["media"] = [media.as_dict() for media in self.media]

        return data
