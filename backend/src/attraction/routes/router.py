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

_attraction_service = AttractionService(
    AttractionRepository(), RedisStorage(), CloudStorage(), MapsCoService()
)


@router.get("/all")
def get_all_attractions(
    db: Session = Depends(get_db), is_token_valid: bool = Depends(verify_jwt)
) -> list[AttractionSchema]:
    return _attraction_service.get_all_attractions(db)


@router.get("")
def get_attractions(
    filters: AttractionFilters = Depends(),
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
) -> list[AttractionSchema]:
    return _attraction_service.get_attractions(db, filters)


@router.get("/{attraction_id}")
def get_attraction_by_id(
    attraction_id: int,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
) -> AttractionSchema:
    return _attraction_service.get_attraction_by_id(db, attraction_id)


@router.post("/create")
def create_attraction(
    attraction: AttractionSchema,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
) -> Response:
    return _attraction_service.create_attraction(db, attraction)


@router.get("/{attraction_id}/images")
def get_attraction_images(
    attraction_id: int,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
) -> AttractionImages:
    return _attraction_service.get_attraction_images(db, attraction_id)


@router.patch("/{attraction_id}/update")
def update_attraction(
    attraction_id: int,
    updated_attraction: AttractionSchema,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
) -> AttractionSchema:
    return _attraction_service.update_attraction(db, attraction_id, updated_attraction)


@router.delete("/{attraction_id}/delete")
def delete_attraction(
    attraction_id: int,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
) -> Response:
    return _attraction_service.delete_attraction(db, attraction_id)
