from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.users.models import Profile

router = APIRouter()


@router.get("/all")
def get_all_profiles(db: Session = Depends(get_db)):
    return db.query(Profile).all()
