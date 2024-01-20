import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.attraction.repositories.sqlalchemy_repository import SQLAlchemyRepository
from src.attraction.schemas import AttractionSchema
from src.attraction.services.attraction_service import AttractionService
from src.database import get_db

logger = logging.getLogger(__name__)
router = APIRouter()
in_memory_repo = SQLAlchemyRepository()
_attraction_service = AttractionService(in_memory_repo)


@router.get("/all")
def get_all_attractions(db: Session = Depends(get_db)):
    logger.info("Getting all attractions")
    return _attraction_service.get_all_attractions(db)


@router.get("/{attraction_id}")
def get_attraction_by_id(attraction_id: int, db: Session = Depends(get_db)):
    logger.info(f"Getting attraction by ID: {attraction_id}")

    return _attraction_service.get_attraction_by_id(db, attraction_id)


@router.post("/create")
def create_attraction(attraction: AttractionSchema, db: Session = Depends(get_db)):
    logger.info("Creating new attraction")

    return _attraction_service.create_attraction(db, attraction)


@router.patch("/{attraction_id}/update")
def update_attraction(
        attraction_id: int,
        updated_attraction: AttractionSchema,
        db: Session = Depends(get_db),
):
    logger.info(f"Updating attraction with ID: {attraction_id}")

    return _attraction_service.update_attraction(db, attraction_id, updated_attraction)


@router.delete("/{attraction_id}/delete")
def delete_attraction(attraction_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting attraction with ID: {attraction_id}")

    return _attraction_service.delete_attraction(db, attraction_id)
