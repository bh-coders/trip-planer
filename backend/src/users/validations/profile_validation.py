
from fastapi import HTTPException


def validate_name(name: str) -> str:
    if len(name) < 3:
        raise HTTPException(
            status_code=400, detail="Name must be at least 3 characters long"
        )
    return name


def validate_surname(surname: str) -> str:
    if len(surname) < 3:
        raise HTTPException(
            status_code=400, detail="Surname must be at least 3 characters long"
        )
    return surname
