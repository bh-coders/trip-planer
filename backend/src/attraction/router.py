from fastapi import APIRouter


from .schemas import Attraction
from .services.attraction_service import AttractionService
from .repositories.in_memory_repo import InMemoryRepository

router = APIRouter()
in_memory_repo = InMemoryRepository()
_attraction_service = AttractionService(in_memory_repo)


@router.get("/all")
def get_all_attractions():
    return _attraction_service.get_all_items()


@router.get("/{attraction_id}")
def get_attraction_by_id(attraction_id: str):
    return _attraction_service.get_item_by_id(attraction_id)


@router.post("/create")
def create_attraction(attraction: Attraction):
    return _attraction_service.create_item(attraction)


@router.patch("/{attraction_id}/update")
def update_attraction(attraction_id: str, updated_attraction: Attraction):
    if attraction_id == str(updated_attraction.id):
        return _attraction_service.update_item(updated_attraction)

@router.delete("/{attraction_id}/delete")
def delete_attraction(attraction_id: str, ):
    return _attraction_service.delete_item(attraction_id)
