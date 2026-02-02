from sqlmodel import Session, select
from typing import Optional
from uuid import UUID
import json

from fastapi import HTTPException, status
import sys
import os

# Add the parent directory to the Python path for Vercel deployment
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.models.user import User, UserCreate, UserRead
from auth.utils import get_password_hash, verify_password
from cache.cache_service import cache_service


class UserService:
    @staticmethod
    def create_user(session: Session, user_data: UserCreate) -> UserRead:
        # Check if user already exists
        existing_user = session.exec(
            select(User).where(User.email == user_data.email)
        ).first()

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists",
            )

        # Truncate password to 72 bytes for bcrypt compatibility
        safe_password = user_data.password[:72]

        # Hash password (bcrypt-safe)
        hashed_password = get_password_hash(safe_password)

        # Create DB user
        db_user = User(
            email=user_data.email,
            password_hash=hashed_password,
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        user_read = UserRead(
            user_id=db_user.user_id,
            email=db_user.email,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )

        # Cache for 10 minutes (JSON-safe serialization)
        cache_key = f"user:{db_user.user_id}"
        cache_service.set(
            cache_key,
            json.dumps(user_read.model_dump(mode="json")),
            expire=600,
        )

        return user_read

    @staticmethod
    def authenticate_user(
        session: Session, email: str, password: str
    ) -> Optional[UserRead]:
        db_user = session.exec(
            select(User).where(User.email == email)
        ).first()

        # Truncate password to 72 bytes for bcrypt compatibility
        safe_password = password[:72]

        if not db_user or not verify_password(safe_password, db_user.password_hash):
            return None

        user_read = UserRead(
            user_id=db_user.user_id,
            email=db_user.email,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )

        cache_key = f"user:{db_user.user_id}"
        cache_service.set(
            cache_key,
            json.dumps(user_read.model_dump(mode="json")),
            expire=600,
        )

        return user_read

    @staticmethod
    def get_user_by_id(
        session: Session, user_id: UUID
    ) -> Optional[UserRead]:
        cache_key = f"user:{user_id}"
        cached_result = cache_service.get(cache_key)

        if cached_result:
            return UserRead(**json.loads(cached_result))

        db_user = session.exec(
            select(User).where(User.user_id == user_id)
        ).first()

        if not db_user:
            return None

        user_read = UserRead(
            user_id=db_user.user_id,
            email=db_user.email,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at,
        )

        cache_service.set(
            cache_key,
            json.dumps(user_read.model_dump(mode="json")),
            expire=600,
        )

        return user_read
