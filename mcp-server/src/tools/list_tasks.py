from typing import Dict, Any
import uuid
from sqlmodel import Session, select
from ..db.database import get_session
from ..models.task import Task


async def list_tasks_tool(tool_call: Dict[str, Any]) -> Dict[str, Any]:
    """
    MCP tool to list all tasks for a user.

    Args:
        tool_call: Dictionary containing the tool call information including arguments

    Returns:
        Dictionary with the result of the operation
    """
    try:
        # Extract arguments from the tool call
        arguments = tool_call.get("arguments", {})
        user_id = arguments.get("user_id")
        completed_only = arguments.get("completed_only", None)
        active_only = arguments.get("active_only", None)

        # Validate required arguments
        if not user_id:
            return {
                "success": False,
                "message": "Missing required argument: user_id is required",
                "error_code": "MISSING_ARGUMENTS"
            }

        # Convert user_id to UUID if it's a string
        try:
            user_uuid = uuid.UUID(user_id) if isinstance(user_id, str) else user_id
        except ValueError:
            return {
                "success": False,
                "message": "Invalid user ID format",
                "error_code": "INVALID_USER_ID"
            }

        # Get database session and query tasks
        db = next(get_session())

        try:
            # Build the query based on filters
            query = select(Task).where(Task.user_id == user_uuid)

            if completed_only is True:
                query = query.where(Task.completed == True)
            elif active_only is True:
                query = query.where(Task.completed == False)

            # Execute the query
            tasks = db.exec(query).all()

            # Format the tasks for response
            formatted_tasks = []
            for task in tasks:
                formatted_tasks.append({
                    "id": str(task.id),
                    "title": task.title,
                    "description": task.description or "",
                    "completed": task.completed,
                    "created_at": task.created_at.isoformat(),
                    "updated_at": task.updated_at.isoformat()
                })

            formatted_tasks_str = ""
            if formatted_tasks:
                formatted_tasks_str = "\n\n--- Your Tasks ---" # Header
                for task in formatted_tasks:
                    formatted_tasks_str += (
                        f"\n\nID: {task['id']}"
                        f"\nTitle: {task['title']}"
                        f"\nDescription: {task['description'] if task['description'] else 'N/A'}"
                        f"\nCompleted: {'Yes' if task['completed'] else 'No'}"
                    )
                formatted_tasks_str += "\n------------------" # Footer
            else:
                formatted_tasks_str = "\n\nNo tasks found for this user."

            status_message = "Here's an overview of your task list."
            if completed_only:
                status_message = "Here are your completed tasks."
            elif active_only:
                status_message = "Here are your active tasks."
            
            final_message = f"{status_message}{formatted_tasks_str}"

            return {
                "success": True,
                "tasks": formatted_tasks,
                "message": final_message, # Use the combined message
                "count": len(formatted_tasks)
            }
        finally:
            db.close()

    except Exception as e:
        return {
            "success": False,
            "message": "Failed to list tasks",
            "error_code": "INTERNAL_ERROR"
        }


def get_list_tasks_schema() -> Dict[str, Any]:
    """
    Returns the JSON schema for the list_tasks tool.

    Returns:
        Dictionary containing the tool's schema
    """
    return {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "string",
                "description": "The ID of the user whose tasks to retrieve"
            },
            "completed_only": {
                "type": "boolean",
                "description": "Optional flag to retrieve only completed tasks"
            },
            "active_only": {
                "type": "boolean",
                "description": "Optional flag to retrieve only active tasks"
            }
        },
        "required": ["user_id"]
    }