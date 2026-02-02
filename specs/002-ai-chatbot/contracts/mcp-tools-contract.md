# MCP Tools Contract: Todo AI Chatbot (Phase III)

## Overview
This document defines the Model Context Protocol (MCP) tools for the Todo AI Chatbot system. These tools enable the AI agent to perform task management operations.

## Tool: add_task

**Description**: Creates a new task for a user

**Input Schema**:
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "description": "The ID of the user creating the task"
    },
    "title": {
      "type": "string",
      "description": "The title of the task"
    },
    "description": {
      "type": "string",
      "description": "Optional detailed description of the task"
    }
  },
  "required": ["user_id", "title"]
}
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the operation was successful"
    },
    "task_id": {
      "type": "string",
      "description": "The ID of the created task"
    },
    "message": {
      "type": "string",
      "description": "Human-readable result message"
    }
  }
}
```

## Tool: list_tasks

**Description**: Retrieves all tasks for a user

**Input Schema**:
```json
{
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
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the operation was successful"
    },
    "tasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the task"
          },
          "title": {
            "type": "string",
            "description": "Title of the task"
          },
          "description": {
            "type": "string",
            "description": "Detailed description of the task"
          },
          "completed": {
            "type": "boolean",
            "description": "Whether the task is completed"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "Time when the task was created"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "Time when the task was last updated"
          }
        }
      },
      "description": "Array of tasks belonging to the user"
    },
    "message": {
      "type": "string",
      "description": "Human-readable result message"
    }
  }
}
```

## Tool: update_task

**Description**: Updates an existing task for a user

**Input Schema**:
```json
{
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
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the operation was successful"
    },
    "task": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "Unique identifier for the task"
        },
        "title": {
          "type": "string",
          "description": "Updated title of the task"
        },
        "description": {
          "type": "string",
          "description": "Updated description of the task"
        },
        "completed": {
          "type": "boolean",
          "description": "Whether the task is completed"
        },
        "created_at": {
          "type": "string",
          "format": "date-time",
          "description": "Time when the task was created"
        },
        "updated_at": {
          "type": "string",
          "format": "date-time",
          "description": "Time when the task was last updated"
        }
      },
      "description": "The updated task object"
    },
    "message": {
      "type": "string",
      "description": "Human-readable result message"
    }
  }
}
```

## Tool: delete_task

**Description**: Deletes an existing task for a user

**Input Schema**:
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "description": "The ID of the user whose task to delete"
    },
    "task_id": {
      "type": "string",
      "description": "The ID of the task to delete"
    }
  },
  "required": ["user_id", "task_id"]
}
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the operation was successful"
    },
    "message": {
      "type": "string",
      "description": "Human-readable result message"
    }
  }
}
```

## Tool: complete_task

**Description**: Marks an existing task as completed for a user

**Input Schema**:
```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "description": "The ID of the user whose task to complete"
    },
    "task_id": {
      "type": "string",
      "description": "The ID of the task to complete"
    },
    "completed": {
      "type": "boolean",
      "description": "Whether to mark the task as completed (true) or active (false)",
      "default": true
    }
  },
  "required": ["user_id", "task_id"]
}
```

**Output Schema**:
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Indicates if the operation was successful"
    },
    "task": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "Unique identifier for the task"
        },
        "title": {
          "type": "string",
          "description": "Title of the task"
        },
        "description": {
          "type": "string",
          "description": "Description of the task"
        },
        "completed": {
          "type": "boolean",
          "description": "Whether the task is completed"
        },
        "created_at": {
          "type": "string",
          "format": "date-time",
          "description": "Time when the task was created"
        },
        "updated_at": {
          "type": "string",
          "format": "date-time",
          "description": "Time when the task was last updated"
        }
      },
      "description": "The updated task object"
    },
    "message": {
      "type": "string",
      "description": "Human-readable result message"
    }
  }
}
```

## Common Error Responses

All tools may return the following error response:

```json
{
  "success": false,
  "message": "Error description",
  "error_code": "string"
}
```