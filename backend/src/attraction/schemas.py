from pydantic import BaseModel, UUID4
from typing_extensions import Union


class AttractionSchema(BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float
    open_hours: dict[str, dict[str, Union[int, float]]]
