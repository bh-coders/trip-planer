from email_validator import EmailNotValidError, validate_email
from fastapi import HTTPException


def email_validator(email_value: str) -> str:
    try:
        validate_email(email_value, check_deliverability=False)
    except EmailNotValidError:
        raise HTTPException(status_code=400, detail="Invalid email address")
    return email_value
