from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid
from typing import Optional
from sqlalchemy import Index
from .user import User


class TaskBase(SQLModel):
    """Base model for Task with common fields"""
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)


class Task(TaskBase, table=True):
    """Task model representing a user's todo item"""
    __table_args__ = (
        Index('idx_task_user_id', 'user_id'),
        Index('idx_task_user_created', 'user_id', 'created_at'),
    )

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    user_id: uuid.UUID = Field(foreign_key="user.user_id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    def __setattr__(self, name, value):
        """Override to automatically update updated_at when fields change"""
        # Handle all SQLAlchemy internal attributes to avoid errors
        if name.startswith('_sa_'):
            # Allow setting internal SQLAlchemy attributes directly
            super().__setattr__(name, value)
        elif name != "updated_at":
            # Update updated_at for all other attributes (except updated_at itself)
            super().__setattr__("updated_at", datetime.utcnow())
            super().__setattr__(name, value)
        else:
            # For updated_at, just set normally
            super().__setattr__(name, value)


class TaskCreate(TaskBase):
    """Model for creating new tasks"""
    pass


class TaskRead(TaskBase):
    """Model for reading task data"""
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime


class TaskUpdate(SQLModel):
    """Model for updating existing tasks"""
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None