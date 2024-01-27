import logging
import requests
from fastapi import APIRouter, Depends, HTTPException
from pydantic import json
from sqlalchemy.orm import Session
from typing import Optional

from src.attraction.repositories.attraction_repo import AttractionRepository
from src.attraction.schemas import AttractionSchema
from src.attraction.services.attraction_service import AttractionService
from src.core.database import get_db
from src.core.interceptors.auth_interceptor import verify_jwt

logger = logging.getLogger(__name__)
router = APIRouter()

_attraction_service = AttractionService(AttractionRepository())


@router.get("/all")
def get_all_attractions(db: Session = Depends(get_db), is_token_valid: bool = Depends(verify_jwt)):
    return _attraction_service.get_all_attractions(db)


@router.get("/{attraction_id}")
def get_attraction_by_id(
        attraction_id: int,
        db: Session = Depends(get_db),
        is_token_valid: bool = Depends(verify_jwt),
):
    return _attraction_service.get_attraction_by_id(db, attraction_id)


@router.post("/create")
def create_attraction(
        attraction: AttractionSchema,
        db: Session = Depends(get_db),
        is_token_valid: bool = Depends(verify_jwt),
):
    return _attraction_service.create_attraction(db, attraction)


@router.patch("/{attraction_id}/update")
def update_attraction(
        attraction_id: int,
        updated_attraction: AttractionSchema,
        db: Session = Depends(get_db),
        is_token_valid: bool = Depends(verify_jwt),
):
    return _attraction_service.update_attraction(db, attraction_id, updated_attraction)


@router.delete("/{attraction_id}/delete")
def delete_attraction(
        attraction_id: int,
        db: Session = Depends(get_db),
        is_token_valid: bool = Depends(verify_jwt),
):
    return _attraction_service.delete_attraction(db, attraction_id)


@router.get("/search/")
def search_attraction(
        db: Session = Depends(get_db),
        name: Optional[str] = "",
        country: Optional[str] = "",
        state: Optional[str] = "",
        city: Optional[str] = ""
):
    return _attraction_service.search_attraction(db, name, country, state, city)


@router.get("/reverse-geocode/")
async def reverse_geocode(lat: float, lon: float):
    NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse"

    params = {
        "lat": lat,
        "lon": lon,
        "format": "json",
        "addressdetails": 1  # Include address details in the response
    }

    try:
        response = requests.get(NOMINATIM_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        address = data.get("address", {})
        return {"country": address["country"], "state": address["state"], "city": address["city"]}
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e))
