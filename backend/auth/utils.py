from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from sqlmodel import Session, select
import sys
import os

# Add the parent directory to the Python path for Vercel deployment
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.models.user import User
from config import settings

# ------------------------------------------------------------------
# Password hashing configuration
# ------------------------------------------------------------------

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

BCRYPT_MAX_BYTES = 72  # hard bcrypt limit


def _truncate_password(password: str) -> str:
    """
    Safely truncate password to bcrypt's 72-byte limit.
    Handles UTF-8 multi-byte characters correctly.
    """
    if not password:
        return password

    encoded = password.encode("utf-8")

    # Truncate at exactly 72 bytes to satisfy bcrypt requirements
    if len(encoded) > BCRYPT_MAX_BYTES:
        encoded = encoded[:BCRYPT_MAX_BYTES]

    # Decode back to string, handling potential multi-byte character cuts
    truncated_password = encoded.decode("utf-8", errors="ignore")

    return truncated_password


# ------------------------------------------------------------------
# Password helpers
# ------------------------------------------------------------------

def get_password_hash(password: str) -> str:
    """
    Hash a password using bcrypt with safe truncation.
    """
    if not password:
        raise ValueError("Password cannot be empty")

    safe_password = _truncate_password(password)
    return pwd_context.hash(safe_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its bcrypt hash.
    """
    if not plain_password or not hashed_password:
        return False

    safe_password = _truncate_password(plain_password)
    return pwd_context.verify(safe_password, hashed_password)


# ------------------------------------------------------------------
# Authentication helpers
# ------------------------------------------------------------------

def authenticate_user(
    session: Session,
    email: str,
    password: str,
) -> Optional[User]:
    """
    Authenticate user by email and password.
    """
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user


# ------------------------------------------------------------------
# JWT helpers
# ------------------------------------------------------------------

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None,
) -> str:
    """
    Create a signed JWT access token.
    """
    to_encode = data.copy()

    expire = (
        datetime.utcnow() + expires_delta
        if expires_delta
        else datetime.utcnow()
        + timedelta(minutes=settings.jwt_access_token_expire_minutes)
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )


def verify_token(token: str) -> dict:
    """
    Decode and validate a JWT token.
    """
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user_from_token(token: str) -> dict:
    """
    Dependency helper used by protected routes.
    """
    payload = verify_token(token)

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return payload