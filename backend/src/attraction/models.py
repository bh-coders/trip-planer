import uuid
from typing import TYPE_CHECKING, Optional

from sqlalchemy import JSON, UUID, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from src.core.database import Base

if TYPE_CHECKING:
    from src.users.models import Profile


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

    profile_id: Optional[uuid.UUID] = Column(
        UUID(as_uuid=True), ForeignKey("profiles.id"), nullable=True
    )
    profile: Mapped["Profile"] = relationship(
        argument="Profile", back_populates="attractions"
    )
