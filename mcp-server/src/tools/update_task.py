from typing import Dict, Any
import uuid
from sqlmodel import Session, select
from ..db.database import get_session
from ..models.task import Task


async def update_task_tool(tool_call: Dict[str, Any]) -> Dict[str, Any]:
    """
    MCP tool to update an existing task for a user.

    Args:
        tool_call: Dictionary containing the tool call information including arguments

    Returns:
        Dictionary with the result of the operation
    """
    try:
        # Extract arguments from the tool call
        arguments = tool_call.get("arguments", {})
        user_id = arguments.get("user_id")
        task_id = arguments.get("task_id")
        title = arguments.get("title")
        description = arguments.get("description")

        # Validate required arguments
        if not user_id or not task_id:
            return {
                "success": False,
                "message": "Missing required arguments: user_id and task_id are required",
                "error_code": "MISSING_ARGUMENTS"
            }

        # Convert IDs to UUID if they're strings
        try:
            user_uuid = uuid.UUID(user_id) if isinstance(user_id, str) else user_id
            task_uuid = uuid.UUID(task_id) if isinstance(task_id, str) else task_id
        except ValueError:
            return {
                "success": False,
                "message": "Invalid user ID or task ID format",
                "error_code": "INVALID_ID_FORMAT"
            }

        # Get database session
        db = next(get_session())

        try:
            # Find the task that belongs to the user
            statement = select(Task).where(
                Task.id == task_uuid,
                Task.user_id == user_uuid
            )
            task = db.exec(statement).first()

            if not task:
                return {
                    "success": False,
                    "message": "Task not found or does not belong to user",
                    "error_code": "TASK_NOT_FOUND"
                }

            # Update the task with provided fields
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description

            # Commit the changes
            db.add(task)
            db.commit()
            db.refresh(task)

            return {
                "success": True,
                "task": {
                    "id": str(task.id),
                    "title": task.title,
                    "description": task.description or "",
                    "completed": task.completed,
                    "created_at": task.created_at.isoformat(),
                    "updated_at": task.updated_at.isoformat()
                },
                "message": f"Successfully updated task: {task.title}"
            }
        finally:
            db.close()

    except Exception as e:
        return {
            "success": False,
            "message": "Failed to update task",
            "error_code": "INTERNAL_ERROR"
        }


def get_update_task_schema() -> Dict[str, Any]:
    """
    Returns the JSON schema for the update_task tool.

    Returns:
        Dictionary containing the tool's schema
    """
    return {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "string",
                "description": "The ID of the user whose task to update"
            },
            "task_id": {
                "type": "string",
                "description": "The ID of the task to update"
            },
            "title": {
                "type": "string",
                "description": "Optional new title for the task"
            },
            "description": {
                "type": "string",
                "description": "Optional new description for the task"
            }
        },
        "required": ["user_id", "task_id"]
    }