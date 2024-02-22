import logging
from typing import Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.attraction.services.geocoding_service import MapsCoService
from src.core.interceptors.auth_interceptor import verify_jwt
from src.db.cache_storage import RedisStorage
from src.db.cloud_storage import CloudStorage
from src.db.database import get_db

logger = logging.getLogger(__name__)
router = APIRouter()
cloud_storage = CloudStorage()
cache_storage = RedisStorage()
geo_service = MapsCoService()


@router.get("/")
def index(
        db: Session = Depends(get_db), is_token_valid: bool = Depends(verify_jwt)
) -> Dict:
    return {"Status": "Ok"}