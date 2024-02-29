import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from src.common.schemas.common_schema import SortDirection
from src.file.models.schemas import MediaRead


class AttractionCategory(str, Enum):
    Gastronomy = "gastronomy"
    Culture = "culture"


class OpenHoursSchema(BaseModel):
    open: Optional[int] = None
    close: Optional[int] = None


class AttractionBase(BaseModel):
    id: Optional[int] = None
    user_id: Optional[uuid.UUID] = None


class AttractionCreate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    latitude: float
    longitude: float
    open_hours: Optional[dict[str, OpenHoursSchema]] = None
    category: Optional[AttractionCategory] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    media: list[
        MediaRead
    ] = []  # Something to think about is whether we need so much data


class AttractionSchema(AttractionBase, AttractionCreate):
    rating: float = 0.0
    time_spent: float = 0.0
    price: float = 0.0
    visits: int = 0


class AttractionImages(BaseModel):
    id: Optional[int] = None  # attraction_id
    image_urls: list[str] = []


class AttractionSortedBy(str, Enum):
    TopRated = "topRated"
    MostRated = "mostRated"


class AttractionFilters(BaseModel):
    country: Optional[str] = None  # 'Poland' for only developing
    state: Optional[str] = None
    city: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    category: Optional[AttractionCategory] = None
    radius: Optional[int] = 1000
    sort_by: Optional[AttractionSortedBy] = None
    sort_direction: Optional[SortDirection] = SortDirection.Desc
