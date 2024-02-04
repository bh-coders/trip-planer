import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class AttractionCategory(str, Enum):
    Gastronomy = "gastronomy"
    Culture = "culture"


class OpenHoursSchema(BaseModel):
    open: Optional[int] = None
    close: Optional[int] = None


class AttractionSchema(BaseModel):
    id: Optional[int] = None
    user_id: Optional[uuid.UUID] = None
    name: Optional[str] = None
    description: Optional[str] = None
    latitude: float
    longitude: float
    open_hours: Optional[dict[str, OpenHoursSchema]] = None
    category: Optional[AttractionCategory] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    rating: float = 0.0
    time_spent: float = 0.0
    price: float = 0.0
    visits: int = 0


class AttractionImages(BaseModel):
    id: int | None
    image_urls: list[str] = []
