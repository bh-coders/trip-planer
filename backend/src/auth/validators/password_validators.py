from fastapi import HTTPException


def password_validator(password_value: str) -> str:
    if len(password_value) < 8:
        raise HTTPException(
            status_code=400, detail="Password must be at least 8 characters long"
        )
    if not any(char.isdigit() for char in password_value):
        raise HTTPException(
            status_code=400, detail="Password must contain at least one number"
        )
    if not any(char.isupper() for char in password_value):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter",
        )
    if not any(char.islower() for char in password_value):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one lowercase letter",
        )
    if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>/?~" for char in password_value):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one special character",
        )
    return password_value
