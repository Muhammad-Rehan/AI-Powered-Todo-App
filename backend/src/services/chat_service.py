from sqlmodel import Session, select
from typing import List
from datetime import datetime
import uuid

from ..models.message import Message, MessageCreate
from ..models.conversation import Conversation


def save_message(db: Session, message: Message) -> Message:
    """
    Save a message to the database.

    Args:
        db: Database session
        message: Message object to save

    Returns:
        Saved message object
    """
    try:
        db.add(message)
        db.commit()
        db.refresh(message)
        return message
    except Exception as e:
        db.rollback()
        raise e


def get_conversation_history(db: Session, conversation_id: str, user_id: uuid.UUID) -> List[dict]:
    """
    Retrieve the conversation history for a given conversation.

    Args:
        db: Database session
        conversation_id: ID of the conversation
        user_id: ID of the user (for validation)

    Returns:
        List of messages in the conversation
    """
    try:
        # Verify that the conversation belongs to the user
        conversation_statement = select(Conversation).where(
            Conversation.id == str(conversation_id),
            Conversation.user_id == user_id
        )
        conversation = db.exec(conversation_statement).first()

        if not conversation:
            raise ValueError("Conversation not found or does not belong to user")

        # Get messages in chronological order
        message_statement = select(Message).where(
            Message.conversation_id == conversation_id
        ).order_by(Message.created_at.asc())
        messages = db.exec(message_statement).all()

        # Format messages for AI consumption
        history = []
        for msg in messages:
            history.append({
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.created_at.isoformat()
            })

        return history

    except Exception as e:
        raise e


def create_new_conversation(db: Session, user_id: uuid.UUID, title: str = None) -> Conversation:
    """
    Create a new conversation for a user.

    Args:
        db: Database session
        user_id: ID of the user creating the conversation
        title: Optional title for the conversation

    Returns:
        Created conversation object
    """
    try:
        if not title:
            title = f"Chat started on {datetime.now().strftime('%Y-%m-%d %H:%M')}"

        conversation = Conversation(
            user_id=user_id,
            title=title
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    except Exception as e:
        db.rollback()
        raise e


def get_user_conversations(db: Session, user_id: uuid.UUID) -> List[Conversation]:
    """
    Get all conversations for a specific user.

    Args:
        db: Database session
        user_id: ID of the user

    Returns:
        List of user's conversations
    """
    try:
        statement = select(Conversation).where(
            Conversation.user_id == user_id
        ).order_by(Conversation.updated_at.desc())
        conversations = db.exec(statement).all()

        return conversations

    except Exception as e:
        raise e


def get_conversation_messages(db: Session, conversation_id: str, user_id: uuid.UUID) -> List[Message]:
    """
    Get all messages for a specific conversation.

    Args:
        db: Database session
        conversation_id: ID of the conversation
        user_id: ID of the user (for validation)

    Returns:
        List of messages in the conversation
    """
    try:
        # Verify that the conversation belongs to the user
        conversation_statement = select(Conversation).where(
            Conversation.id == str(conversation_id),
            Conversation.user_id == user_id
        )
        conversation = db.exec(conversation_statement).first()

        if not conversation:
            raise ValueError("Conversation not found or does not belong to user")

        message_statement = select(Message).where(
            Message.conversation_id == conversation_id
        ).order_by(Message.created_at.asc())
        messages = db.exec(message_statement).all()

        return messages

    except Exception as e:
        raise e