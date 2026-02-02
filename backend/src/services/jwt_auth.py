from datetime import datetime, timedelta
from typing import Optional
import os
from sqlmodel import Session
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from ..models.user import User
import uuid


# JWT Configuration
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "Kv5h_ZokMQYw9gZXLgcJqZiAHcI91HI0KECrVLuhudz29Ydy47dZ-5_C2l7wgnt7")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


security = HTTPBearer()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a new JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    """Verify the JWT token and return the payload"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return payload
    except JWTError:
        raise credentials_exception


def get_current_user(token: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """Dependency to get the current user from the JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = verify_token(token.credentials, credentials_exception)
    user_id = payload.get("sub")

    if user_id is None:
        raise credentials_exception

    try:
        # Convert the user_id to UUID if it's a string representation
        user_uuid = uuid.UUID(user_id) if isinstance(user_id, str) else user_id
    except ValueError:
        raise credentials_exception

    # In a real implementation, we would fetch the user from the database
    # For now, we'll just return a basic user object with the ID
    user = User()
    user.user_id = user_uuid

    return user


def get_user_id_from_token(token: str) -> Optional[uuid.UUID]:
    """Extract user ID from JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = verify_token(token, credentials_exception)
    user_id_str = payload.get("sub")

    if user_id_str is None:
        return None

    try:
        return uuid.UUID(user_id_str)
    except ValueError:
        return None