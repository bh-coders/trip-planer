import re

from email_validator import EmailNotValidError
from email_validator import validate_email as _validate_email
from fastapi import HTTPException


# TODO comment all of this and stay only return
def check_passwords_match(password: str, rewrite_password: str) -> bool:
    if password != rewrite_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    return True


def validate_password(password: str) -> str:
    if len(password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long",
        )
    if not any(char.isdigit() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one number",
        )
    if not any(char.isupper() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter",
        )
    if not any(char.islower() for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one lowercase letter",
        )
    if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>/?~" for char in password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one special character",
        )
    return password


def validate_username(username: str) -> str:
    pattern = r"^[a-zA-Z0-9_-]{3,16}$"
    if not re.match(pattern, username):
        raise HTTPException(status_code=400, detail="Invalid username")
    return username


def validate_email(email: str) -> str:
    try:
        _validate_email(email, check_deliverability=False)
    except EmailNotValidError:
        raise HTTPException(status_code=400, detail="Invalid email address")
    return email
