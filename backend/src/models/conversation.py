from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid
from typing import Optional


class ConversationBase(SQLModel):
    """Base model for Conversation with common fields"""
    title: Optional[str] = Field(default=None, max_length=255)


class Conversation(ConversationBase, table=True):
    """Conversation model representing a chat session"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.user_id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    def __setattr__(self, name, value):
        """Override to automatically update updated_at when fields change"""
        # Avoid interfering with SQLAlchemy internals
        if name != "updated_at" and not name.startswith('_sa_'):
            super().__setattr__("updated_at", datetime.utcnow())
        super().__setattr__(name, value)


class ConversationCreate(ConversationBase):
    """Model for creating new conversations"""
    pass


class ConversationRead(ConversationBase):
    """Model for reading conversation data"""
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime


class ConversationUpdate(SQLModel):
    """Model for updating existing conversations"""
    title: Optional[str] = Field(default=None, max_length=255)