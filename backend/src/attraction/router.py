from fastapi import APIRouter

router = APIRouter()


@router.get("/all")
async def get_all_attractions():
    pass


@router.get("/{id}")
async def get_attraction_by_id():
    pass


@router.get("/{latitude},{longitude}/")
async def get_all_attractions_by_coords(latitude: float, longitude: float):
    return {"latitude": round(latitude, 4), "longitude": round(longitude, 4)}


