from pydantic import BaseModel
from backend.src.attraction.models import Attraction


class Route(BaseModel):
    id: int
    name: str
    attractions: list[Attraction]