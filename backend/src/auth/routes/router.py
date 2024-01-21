from fastapi import APIRouter, Depends

from src.auth.repositories.auth_repo import AuthRepository
from src.auth.services.auth_service import AuthService

router = APIRouter()
_auth_service = AuthService(AuthRepository())


@router.get("/")
def get_index():
    return {"auth": "in_progress"}

