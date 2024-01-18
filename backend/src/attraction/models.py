from database import Base
from sqlalchemy import Column, Integer, String, JSON, Float


class Attraction(Base):
    __tablename__ = "attractions"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    open_hours = Column(JSON, nullable=True)
