from sqlalchemy import JSON, UUID, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.core.database import Base


class Attraction(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    open_hours = Column(JSON, nullable=True)

    # Many-to-one relationship with User
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )
    user = relationship("User", back_populates="attractions")
