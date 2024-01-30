from sqlalchemy import JSON, UUID, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import Optional
from src.core.database import Base


class Attraction(Base):
    __tablename__ = "attractions"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255))
    description: str = Column(String)
    longitude: float = Column(Float)
    latitude: float = Column(Float)
    open_hours: Optional[dict] = Column(JSON, nullable=True)
    address: str = Column(String)
    city: str = Column(String)
    country: str = Column(String)
    category: str = Column(String)

    # Many-to-one relationship with User
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )
    user = relationship("User", back_populates="attractions")
