from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base
from pydantic_extra_types.coordinate import Coordinate

Base = declarative_base()


class AttractionOrm(Base):
    __tablename__ = 'attractions'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(63), unique=True)
    description = Column(String(255))
    coords = Column(ARRAY(String(255), as_tuple=True))


class Attraction(BaseModel):
    id: int
    name: str
    description: str
    coords: Coordinate
