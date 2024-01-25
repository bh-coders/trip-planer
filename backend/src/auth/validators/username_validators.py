import re

from fastapi import HTTPException


def username_validator(username_value: str) -> str:
    pattern = r"^[a-zA-Z0-9_-]{3,16}$"
    if not re.match(pattern, username_value):
        raise HTTPException(status_code=400, detail="Invalid username")
    return username_value
