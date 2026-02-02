from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid
from typing import Optional
from sqlalchemy import JSON, Column


class MessageBase(SQLModel):
    """Base model for Message with common fields"""
    conversation_id: str = Field(foreign_key="conversation.id", nullable=False)
    user_id: uuid.UUID = Field(foreign_key="user.user_id", nullable=False)
    role: str = Field(regex="^(user|assistant)$")  # Either 'user' or 'assistant'
    content: str = Field(min_length=1)
    tool_calls: Optional[dict] = Field(default=None, sa_column=Column(JSON))


class Message(MessageBase, table=True):
    """Message model representing individual chat messages"""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)



class MessageCreate(MessageBase):
    """Model for creating new messages"""
    pass


class MessageRead(MessageBase):
    """Model for reading message data"""
    id: str
    created_at: datetime


class MessageUpdate(SQLModel):
    """Model for updating existing messages"""
    content: Optional[str] = Field(default=None, min_length=1)
    tool_calls: Optional[dict] = Field(default=None, sa_column=Column(JSON))