import asyncio
from typing import Dict, Any, List
import os

from src.tools.add_task import add_task_tool, get_add_task_schema
from src.tools.list_tasks import list_tasks_tool, get_list_tasks_schema
from src.tools.update_task import update_task_tool, get_update_task_schema
from src.tools.delete_task import delete_task_tool, get_delete_task_schema
from src.tools.complete_task import complete_task_tool, get_complete_task_schema



class MCPServer:
    """
    MCP (Model Context Protocol) Server that exposes tools to AI agents.
    Handles task management operations for the AI chatbot.
    """

    def __init__(self):
        """Initialize the MCP server with all available tools."""
        self.tools_registry = {}
        self._register_tools()

    def _register_tools(self):
        """Register all available tools with their schemas."""
        tools = [
            {
                "name": "add_task",
                "function": add_task_tool,
                "schema": get_add_task_schema()
            },
            {
                "name": "list_tasks",
                "function": list_tasks_tool,
                "schema": get_list_tasks_schema()
            },
            {
                "name": "update_task",
                "function": update_task_tool,
                "schema": get_update_task_schema()
            },
            {
                "name": "delete_task",
                "function": delete_task_tool,
                "schema": get_delete_task_schema()
            },
            {
                "name": "complete_task",
                "function": complete_task_tool,
                "schema": get_complete_task_schema()
            }
        ]

        for tool in tools:
            self.tools_registry[tool["name"]] = {
                "function": tool["function"],
                "schema": tool["schema"]
            }

    async def execute_tool(self, tool_name: str, tool_call: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a tool with the given arguments.

        Args:
            tool_name: Name of the tool to execute
            tool_call: Dictionary containing the tool call information

        Returns:
            Result of the tool execution
        """
        if tool_name not in self.tools_registry:
            return {
                "success": False,
                "message": f"Tool '{tool_name}' not found",
                "error_code": "TOOL_NOT_FOUND"
            }

        try:
            # Execute the registered tool function
            tool_func = self.tools_registry[tool_name]["function"]
            result = await tool_func(tool_call) if asyncio.iscoroutinefunction(tool_func) else tool_func(tool_call)

            return result
        except Exception as e:
            print(f"Error executing tool {tool_name}: {str(e)}")

            return {
                "success": False,
                "message": f"Error executing tool {tool_name}: {str(e)}",
                "error_code": "EXECUTION_ERROR"
            }

    def get_tool_schema(self, tool_name: str) -> Dict[str, Any]:
        """
        Get the schema for a specific tool.

        Args:
            tool_name: Name of the tool

        Returns:
            Schema definition for the tool
        """
        if tool_name not in self.tools_registry:
            return {}

        return self.tools_registry[tool_name]["schema"]

    def get_available_tools(self) -> List[str]:
        """
        Get a list of all available tool names.

        Returns:
            List of available tool names
        """
        return list(self.tools_registry.keys())


# Global server instance
mcp_server = MCPServer()


async def handle_tool_request(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle an incoming tool request.

    Args:
        tool_name: Name of the tool to execute
        arguments: Arguments for the tool

    Returns:
        Result of the tool execution
    """
    tool_call = {
        "arguments": arguments
    }

    result = await mcp_server.execute_tool(tool_name, tool_call)
    return result


def main():
    """Main entry point for the MCP server."""
    print("Starting MCP Server...")
    print(f"Available tools: {mcp_server.get_available_tools()}")

    # In a real implementation, this would start an HTTP server
    # For now, we'll just print startup info
    print("MCP Server is ready to handle tool requests")


if __name__ == "__main__":
    main()