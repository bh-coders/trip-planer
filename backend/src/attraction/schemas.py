from pydantic import BaseModel, UUID4
from typing_extensions import Union


class Attraction(BaseModel):
    id: UUID4
    name: str
    latitude: float
    longitude: float
    opening_hours: dict[str, dict[str, Union[int, float]]]
    prices: dict[str, dict[str, Union[int, float]]]
