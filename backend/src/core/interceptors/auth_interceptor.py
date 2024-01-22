import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from src.core.configs import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_jwt(token: str = Depends(oauth2_scheme)) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        print(payload)
        return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")