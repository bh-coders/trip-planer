import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.core.interceptors.auth_interceptor import verify_jwt
from src.users.schemas import (
    ChangeEmailSchema,
    ChangePasswordSchema,
    UserCreateSchema,
    UserListSchema,
    UserSchema,
    UserUpdateSchema,
)
from src.users.services import UserService

logger = logging.getLogger(__name__)
router = APIRouter()
service = UserService()


@router.get("/detail/{user_id}", response_model=UserSchema, status_code=200)
def get_user(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
):
    if not is_token_valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    logger.info(f"Get user with id: {user_id}")
    return service.get_user_by_id(db, user_id)


@router.get("/list", response_model=UserListSchema, status_code=200)
def get_users(
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
):
    if not is_token_valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    logger.info("Get all users")
    return service.get_all_users(db)


@router.post("/register", response_model=UserCreateSchema, status_code=201)
def register_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    logger.info("Register new user: %s", user)
    return service.create_user(db, user)


@router.put("/update/{user_id}", response_model=UserUpdateSchema, status_code=200)
def update_user(
    user_id: uuid.UUID,
    user: UserUpdateSchema,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
):
    if not is_token_valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    logger.info("Update user with id: %s", user_id)
    return service.update_user(db, user_id, user)


@router.delete("/delete/{user_id}", response_model=None, status_code=204)
def delete_user(
    user_id: uuid.UUID,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
):
    if not is_token_valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    logger.info("Delete user with id: %s", user_id)
    return service.delete_user(db, user_id)


@router.post(
    "/change-email/{user_id}", response_model=ChangeEmailSchema, status_code=200
)
def change_email(
    user_id: uuid.UUID,
    user_data: ChangeEmailSchema,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
):
    if not is_token_valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    logger.info("Change email for user with id: %s", user_id)
    return service.change_email(db, user_id, user_data)


@router.post(
    "/change-password/{user_id}", response_model=ChangePasswordSchema, status_code=200
)
def change_password(
    user_id: uuid.UUID,
    user_data: ChangePasswordSchema,
    db: Session = Depends(get_db),
    is_token_valid: bool = Depends(verify_jwt),
):
    if not is_token_valid:
        raise HTTPException(status_code=401, detail="Invalid token")
    logger.info("Change password for user with id: %s", user_id)
    return service.change_password(db, user_id, user_data)
