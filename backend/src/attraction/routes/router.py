import logging

from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from src.attraction.repositories.attraction_repo import AttractionRepository
from src.attraction.schemas import AttractionFilters, AttractionImages, AttractionSchema
from src.attraction.services.attraction_service import AttractionService
from src.attraction.services.geocoding_service import MapsCoService
from src.core.interceptors.auth_interceptor import verify_jwt
from src.db.cache_storage import RedisStorage
from src.db.cloud_storage import CloudStorage
from src.db.database import get_db

logger = logging.getLogger(__name__)
router = APIRouter()
attraction_repo = AttractionRepository()
cloud_storage = CloudStorage()
cache_storage = RedisStorage()
geo_service = MapsCoService()
_attraction_service = AttractionService(attraction_repo, cache_storage, cloud_storage, geo_service)


@router.get("/all", dependencies=[Depends(verify_jwt)])
def get_all_attractions(
        db: Session = Depends(get_db)
) -> list[AttractionSchema]:
    return _attraction_service.get_all_attractions(db)


@router.get("", dependencies=[Depends(verify_jwt)])
def get_attractions(
        filters: AttractionFilters = Depends(),
        db: Session = Depends(get_db)
) -> list[AttractionSchema]:
    return _attraction_service.get_attractions(db, filters)


@router.get("/{attraction_id}")
async def get_attraction_by_id(
        attraction_id: int,
        db: Session = Depends(get_db)
) -> AttractionSchema:
    return _attraction_service.get_attraction_by_id(db, attraction_id)


@router.post("/create", dependencies=[Depends(verify_jwt)])
def create_attraction(
        attraction: AttractionSchema,
        db: Session = Depends(get_db)
) -> Response:
    return _attraction_service.create_attraction(db, attraction)


@router.get("/{attraction_id}/images", dependencies=[Depends(verify_jwt)])
def get_attraction_images(
        attraction_id: int,
        db: Session = Depends(get_db)
) -> AttractionImages:
    return _attraction_service.get_attraction_images(db, attraction_id)


@router.patch("/{attraction_id}/update", dependencies=[Depends(verify_jwt)])
def update_attraction(
        attraction_id: int,
        updated_attraction: AttractionSchema,
        db: Session = Depends(get_db)
) -> AttractionSchema:
    return _attraction_service.update_attraction(db, attraction_id, updated_attraction)


@router.delete("/{attraction_id}/delete", dependencies=[Depends(verify_jwt)])
def delete_attraction(
        attraction_id: int,
        db: Session = Depends(get_db)
) -> Response:
    return _attraction_service.delete_attraction(db, attraction_id)
