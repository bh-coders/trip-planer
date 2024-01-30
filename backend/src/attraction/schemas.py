from enum import Enum
from pydantic import BaseModel
from typing_extensions import Union


class AttractionCategory(str, Enum):
    Gastronomy = "gastronomy"
    Culture = "culture"


class AttractionSchema(BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float
    open_hours: dict[str, dict[str, Union[int, float]]]
    category: AttractionCategory
    address: str
    city: str
    country: str


class AttractionImages(BaseModel):
    id: int | None
    image_urls: list[str] = []
