import jwt

from src.core.configs import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from passlib.context import CryptContext
from src.core.configs import SECRET_KEY, ALGORITHM

password_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")

def check_password(plain_password: str, hashed_password: str) -> bool:
    return password_hashing.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    return password_hashing.hash(password)

def create_jwt_token(data: dict, expires_delta: timedelta) -> dict:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def return_token(username: str, user_id: str) -> dict:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(data={"username": username, "id": user_id},
                                    expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


