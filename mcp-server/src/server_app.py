import asyncio
from fastapi import FastAPI, HTTPException, Request
from typing import Dict, Any
import uvicorn
import os
from src.server import handle_tool_request


# Create FastAPI app instance for MCP server
app = FastAPI(
    title="Todo AI Chatbot MCP Server",
    description="MCP server for exposing task management tools to AI agents",
    version="1.0.0"
)


@app.on_event('startup')
async def startup_event():
    """Initialize the MCP server on startup."""


@app.post("/add_task")
async def add_task_endpoint(request: Request) -> Dict[str, Any]:
    """
    Endpoint for the add_task tool.
    """
    try:
        payload = await request.json()
        arguments = payload.get("arguments", {})

        result = await handle_tool_request("add_task", arguments)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/list_tasks")
async def list_tasks_endpoint(request: Request) -> Dict[str, Any]:
    """
    Endpoint for the list_tasks tool.
    """
    try:
        payload = await request.json()
        arguments = payload.get("arguments", {})

        result = await handle_tool_request("list_tasks", arguments)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/update_task")
async def update_task_endpoint(request: Request) -> Dict[str, Any]:
    """
    Endpoint for the update_task tool.
    """
    try:
        payload = await request.json()
        arguments = payload.get("arguments", {})

        result = await handle_tool_request("update_task", arguments)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/delete_task")
async def delete_task_endpoint(request: Request) -> Dict[str, Any]:
    """
    Endpoint for the delete_task tool.
    """
    try:
        payload = await request.json()
        arguments = payload.get("arguments", {})

        result = await handle_tool_request("delete_task", arguments)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/complete_task")
async def complete_task_endpoint(request: Request) -> Dict[str, Any]:
    """
    Endpoint for the complete_task tool.
    """
    try:
        payload = await request.json()
        arguments = payload.get("arguments", {})

        result = await handle_tool_request("complete_task", arguments)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    """
    Root endpoint for health check.
    """
    return {
        "message": "Todo AI Chatbot MCP Server",
        "status": "healthy",
        "version": "1.0.0",
        "available_tools": ["add_task", "list_tasks", "update_task", "delete_task", "complete_task"]
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {
        "status": "healthy",
        "service": "todo-ai-chatbot-mcp-server"
    }



def create_app():
    return app

# For Vercel deployment
app = create_app()

# For local development
if __name__ == "__main__":
    port = int(os.getenv("MCP_PORT", "8001"))
    uvicorn.run("src.server_app:app", host="0.0.0.0", port=port, reload=True)
