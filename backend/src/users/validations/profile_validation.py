import os

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


def validate_image_url(image_url: str) -> str:
    image_accepted_extensions = [".jpeg", ".png", ".jpg"]
    _, extension = os.path.splitext(image_url)
    if extension not in image_accepted_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Image URL must be a valid image {', '.join([x.lstrip('.') for x in image_accepted_extensions])}",
        )
    return image_url
