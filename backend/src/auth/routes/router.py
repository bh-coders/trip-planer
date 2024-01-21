from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.repositories.auth_repo import AuthRepository
from src.auth.schemas import UserSchema
from src.auth.services.auth_service import AuthService
from src.database import get_db

router = APIRouter()
_auth_service = AuthService(AuthRepository())


@router.post("/register")
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    return _auth_service.register_user(db, user)

