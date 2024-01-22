from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.repositories.auth_repo import AuthRepository
from src.auth.schemas import UserSchema, SignInSchema
from src.auth.services.auth_service import AuthService
from src.core.database import get_db

router = APIRouter()
_auth_service = AuthService(AuthRepository())


@router.post("/register", response_model=dict)
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    return _auth_service.register_user(user, db)

@router.post("/sign-in", response_model=dict)
def sign_in_user(sign_in_user: SignInSchema, db: Session = Depends(get_db)):
    return _auth_service.sign_in_user(sign_in_user, db)
