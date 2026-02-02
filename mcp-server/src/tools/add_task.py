from typing import Dict, Any
import uuid
from sqlmodel import Session
from src.db.database import engine
from src.models.task import Task

async def add_task_tool(tool_call: Dict[str, Any]) -> Dict[str, Any]:
    try:
        # 1. Extract arguments
        arguments = tool_call.get("arguments", {})
        user_id = arguments.get("user_id")
        title = arguments.get("title")
        description = arguments.get("description", "")

        # 2. Validation
        if not user_id or not title:
            return {
                "success": False,
                "message": "Missing required arguments: user_id and title are required",
                "error_code": "MISSING_ARGUMENTS",
            }

        try:
            # Convert string ID from frontend to valid UUID
            user_uuid = uuid.UUID(user_id)
        except ValueError:
            return {
                "success": False,
                "message": "Invalid user ID format",
                "error_code": "INVALID_USER_ID",
            }

        # 3. Create Database Object
        new_task = Task(
            title=title,
            description=description,
            completed=False,
            user_id=user_uuid,
        )


        # 4. Save to Database
        with Session(engine) as db:
            db.add(new_task)
            db.commit()
            db.refresh(new_task)  # Refresh to get DB generated values

        # 5. Return Success Response
        return {
            "success": True,
            "task_id": str(new_task.id),
            "message": f"Successfully added task: {title}",
            "task": {
                "id": str(new_task.id),
                "title": new_task.title,
                "description": new_task.description,
                "completed": new_task.completed,
                "created_at": new_task.created_at.isoformat(),
                "updated_at": new_task.updated_at.isoformat(),
            },
        }

    except Exception as e:
        # Print full error to your server logs for debugging
        print(f"CRITICAL Error in add_task_tool: {repr(e)}")
        
        return {
            "success": False,
            "message": f"Failed to add task: {str(e)}",
            "error_code": "INTERNAL_ERROR",
        }

def get_add_task_schema() -> Dict[str, Any]:
    """
    Returns the JSON schema for the add_task tool.

    Returns:
        Dictionary containing the tool's schema
    """
    return {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "string",
                "description": "The ID of the user for whom to add the task"
            },
            "title": {
                "type": "string",
                "description": "The title of the task"
            },
            "description": {
                "type": "string",
                "description": "Optional description for the task"
            }
        },
        "required": ["user_id", "title"]
    }
