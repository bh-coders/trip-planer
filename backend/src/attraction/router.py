from fastapi import APIRouter

from src.attraction.schemas import Attraction

router = APIRouter()


@router.get("/all")
def get_all_attractions() -> list[Attraction]:
    ...


@router.get("/{id}")
def get_attraction_by_id() -> Attraction:
    ...


@router.get("/{latitude},{longitude}/")
async def get_all_attractions_by_coords(
    latitude: float, longitude: float
) -> dict[str, float]:
    return {"latitude": round(latitude, 4), "longitude": round(longitude, 4)}
