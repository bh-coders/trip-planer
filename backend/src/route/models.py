from pydantic import BaseModel

from src.attraction.models import Attraction


class Route(BaseModel):
    id: int
    name: str
    attractions: list[Attraction]
