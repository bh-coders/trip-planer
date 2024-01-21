from src.auth.configs import ACCESS_TOKEN_EXPIRE_MINUTES
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

from src.auth.configs import SECRET_KEY, ALGORITHM


password_hashing = CryptContext(schemes=["bcrypt"], deprecated="auto")

def check_password(plain_password, hashed_password):
    return password_hashing.verify(plain_password, hashed_password)

def hash_password(password):
    return password_hashing.hash(password)

def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def return_token(user):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(data={"username": user.username, "id": user.id},
                                    expires_delta=access_token_expires)

    return {"user_id": user.id, "access_token": access_token, "token_type": "bearer"}


