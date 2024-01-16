from pydantic import BaseModel


class Attraction(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    opening_hours: dict[str, str]
    prices: dict[str, float]