from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid
from typing import Optional
from sqlalchemy import Index


MAX_BCRYPT_PASSWORD_LENGTH = 72  # bcrypt max bytes


class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False, max_length=255)


class User(UserBase, table=True):
    """
    User model representing an authenticated user with unique identifier,
    email, password hash, and timestamps.
    """
    __table_args__ = (
        Index('idx_user_email', 'email'),
    )

    user_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(min_length=8, max_length=MAX_BCRYPT_PASSWORD_LENGTH)


class UserRead(UserBase):
    """Schema for reading user data"""
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class UserUpdate(SQLModel):
    """Schema for updating user information"""
    email: Optional[str] = Field(default=None, max_length=255)
    password: Optional[str] = Field(default=None, min_length=8, max_length=MAX_BCRYPT_PASSWORD_LENGTH)