from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, Field, ValidationError

from ..models.message import Message, MessageCreate
from ..models.conversation import Conversation, ConversationCreate
from ..models.task import Task
from ..services.jwt_auth import get_current_user, get_user_id_from_token
from ..utils.database import get_session
from ..services.chat_service import save_message, get_conversation_history
from ..services.ai_agent_service import AIAssistantService


# Request models for validation
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000, description="The user's message to the chatbot")
    conversation_id: Optional[str] = Field(default=None, description="Optional ID of an existing conversation")


class GetConversationRequest(BaseModel):
    conversation_id: str = Field(..., description="The ID of the conversation")

router = APIRouter()


@router.post("/api/{user_id}/chat")
async def chat_endpoint(
    user_id: str,
    request: ChatRequest,
    db: Session = Depends(get_session)
):
    """
    Main chat endpoint that handles communication with the AI assistant.

    Args:
        user_id: The ID of the authenticated user
        message_data: Dictionary containing message and optional conversation_id
        conversation_id: Optional ID of an existing conversation
        db: Database session

    Returns:
        Response from the AI assistant with conversation context
    """
    try:
        # Validate user_id format
        try:
            user_uuid = uuid.UUID(user_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        # Extract message content from the validated request
        user_message = request.message
        conv_id = request.conversation_id

        # Use the provided conversation_id or create a new one
        if not conv_id:
            # Create a new conversation
            new_conversation = Conversation(
                user_id=user_uuid,
                title=f"Chat started on {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            )
            db.add(new_conversation)
            db.commit()
            db.refresh(new_conversation)
            conv_id = new_conversation.id
        else:
            # Validate conversation_id format
            try:
                conv_uuid = uuid.UUID(conv_id)
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid conversation ID format"
                )

            # Validate that the conversation belongs to the user
            statement = select(Conversation).where(
                Conversation.id == str(conv_uuid),
                Conversation.user_id == user_uuid
            )
            conversation = db.exec(statement).first()

            if not conversation:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Conversation not found or does not belong to user"
                )

        # Save the user's message to the conversation
        user_msg = Message(
            conversation_id=conv_id,
            user_id=user_uuid,
            role="user",
            content=user_message
        )
        saved_user_msg = save_message(db, user_msg)

        # Get conversation history to provide context to the AI
        conversation_history = get_conversation_history(db, conv_id, user_uuid)

        # Initialize AI assistant service
        ai_service = AIAssistantService()

        # Process the message with the AI assistant
        ai_response = await ai_service.process_message(
            user_message=user_message,
            conversation_history=conversation_history,
            user_id=user_uuid
        )

        # Save the AI's response to the conversation
        ai_msg = Message(
            conversation_id=conv_id,
            user_id=user_uuid,  # The AI acts on behalf of the system/user
            role="assistant",
            content=ai_response.get("response", ""),
            tool_calls=ai_response.get("tool_calls", {})
        )
        saved_ai_msg = save_message(db, ai_msg)

        # Prepare the response
        response = {
            "response": ai_response.get("response", ""),
            "conversation_id": conv_id,
            "tool_calls": ai_response.get("tool_calls", []),
            "timestamp": datetime.utcnow().isoformat()
        }

        return response

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your request"
        )


@router.get("/api/{user_id}/conversations")
async def get_user_conversations(
    user_id: str,
    db: Session = Depends(get_session)
):
    """
    Retrieve all conversations for a specific user.

    Args:
        user_id: The ID of the authenticated user
        db: Database session

    Returns:
        List of user's conversations
    """
    try:
        # Validate user_id format
        try:
            user_uuid = uuid.UUID(user_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        # Query conversations for the user
        statement = select(Conversation).where(
            Conversation.user_id == user_uuid
        ).order_by(Conversation.updated_at.desc())
        conversations = db.exec(statement).all()

        return {
            "conversations": [
                {
                    "id": conv.id,
                    "title": conv.title,
                    "created_at": conv.created_at.isoformat(),
                    "updated_at": conv.updated_at.isoformat()
                } for conv in conversations
            ]
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving conversations"
        )


@router.get("/api/{user_id}/conversations/{conversation_id}")
async def get_conversation_messages(
    user_id: str,
    conversation_id: str,
    db: Session = Depends(get_session)
):
    """
    Retrieve messages for a specific conversation.

    Args:
        user_id: The ID of the authenticated user
        conversation_id: The ID of the conversation
        db: Database session

    Returns:
        Messages in the conversation
    """
    try:
        # Validate user_id format
        try:
            user_uuid = uuid.UUID(user_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid user ID format"
            )

        # Validate conversation_id format
        try:
            conv_uuid = uuid.UUID(conversation_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid conversation ID format"
            )

        # Verify that the conversation belongs to the user
        conversation_statement = select(Conversation).where(
            Conversation.id == str(conv_uuid),
            Conversation.user_id == user_uuid
        )
        conversation = db.exec(conversation_statement).first()

        if not conversation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Conversation not found or does not belong to user"
            )

        # Get messages in the conversation
        message_statement = select(Message).where(
            Message.conversation_id == conv_uuid
        ).order_by(Message.created_at.asc())
        messages = db.exec(message_statement).all()

        return {
            "conversation_id": conversation_id,
            "messages": [
                {
                    "id": msg.id,
                    "role": msg.role,
                    "content": msg.content,
                    "tool_calls": msg.tool_calls,
                    "created_at": msg.created_at.isoformat()
                } for msg in messages
            ]
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving conversation messages"
        )