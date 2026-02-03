import asyncio
from typing import Dict, Any, List
import os
import uuid
from openai import OpenAI
import aiohttp
from config import settings


class AIAssistantService:
    """
    Service to handle AI agent interactions and manage communication
    with the MCP server for task operations.
    """

    def __init__(self):
        """
        Initialize the AI Assistant Service.
        """
        # Configure OpenAI client based on settings
        if settings.use_openrouter:
            self.openai_client = OpenAI(
                api_key=settings.openai_api_key,
                base_url=settings.openrouter_base_url
            )
            self.model = settings.openrouter_model
        else:
            self.openai_client = OpenAI(api_key=settings.openai_api_key)
            self.model = "gpt-3.5-turbo"  # Default OpenAI model

        self.mcp_server_url = os.getenv("MCP_SERVER_URL", "https://ai-mcp-server-sigma.vercel.app/")
        self.system_instructions = self._get_system_instructions()

        # Define available tools that match MCP server tools
        self.tools = self._define_tools()

    def _define_tools(self) -> List[Dict[str, Any]]:
        """
        Define the tools available to the AI agent that connect to MCP server.

        Returns:
            List of tool definitions in OpenAI format
        """
        return [
            {
                "type": "function",
                "function": {
                    "name": "add_task",
                    "description": "Creates a new task for a user",
                    "parameters": {
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
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "list_tasks",
                    "description": "Retrieves all tasks for a user",
                    "parameters": {
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
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "update_task",
                    "description": "Updates an existing task for a user",
                    "parameters": {
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
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "delete_task",
                    "description": "Deletes an existing task for a user",
                    "parameters": {
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
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "complete_task",
                    "description": "Marks an existing task as completed for a user",
                    "parameters": {
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
                                "default": True
                            }
                        },
                        "required": ["user_id", "task_id"]
                    }
                }
            }
        ]

    def _get_system_instructions(self) -> str:
        """
        Get the system instructions for the AI agent based on behavior spec.

        Returns:
            System instructions as a string
        """
        return """
        You are an AI assistant that helps users manage their todo tasks through natural language.
        You can help users add, list, update, delete, and complete tasks.
        You must use the available tools to perform these operations.
        You should provide clear, user-friendly responses and confirmations after successful operations.
        Always ensure that task operations are performed for the correct user.
        """

    async def process_message(
        self,
        user_message: str,
        conversation_history: List[Dict[str, Any]],
        user_id: uuid.UUID
    ) -> Dict[str, Any]:
        """
        Process a user message with the AI agent and return the response.

        Args:
            user_message: The message from the user
            conversation_history: History of the conversation
            user_id: The ID of the user

        Returns:
            Dictionary containing the AI response and any tool calls
        """
        try:
            # Prepare the messages for the AI
            messages = [{"role": "system", "content": self.system_instructions}]

            # Add conversation history
            for msg in conversation_history:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

            # Add the current user message
            messages.append({
                "role": "user",
                "content": user_message
            })

            # Make the API call to OpenAI/OpenRouter
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools,
                tool_choice="auto"  # Let the model decide when to use tools
            )

            # Process the response
            ai_response = response.choices[0]
            message = ai_response.message

            result = {
                "response": message.content if message.content else "",
                "tool_calls": []
            }

            # Handle any tool calls
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    # Parse the arguments safely using json.loads instead of eval
                    import json
                    try:
                        tool_args = json.loads(tool_call.function.arguments)
                    except json.JSONDecodeError:
                        tool_args = {}

                    # Add user_id to tool args if not present
                    if "user_id" not in tool_args:
                        tool_args["user_id"] = str(user_id)

                    # Execute the tool call (this would connect to the MCP server)
                    tool_result = await self._execute_tool_call(tool_name, tool_args)

                    result["tool_calls"].append({
                        "name": tool_name,
                        "arguments": tool_args,
                        "result": tool_result
                    })

                    # Update the response if needed based on tool results
                    if tool_result.get("success"):
                        # Add confirmation to response
                        result["response"] += f"\n\n{tool_result.get('message', '')}"

            return result

        except Exception as e:
            return {
                "response": "Sorry, I encountered an error while processing your request. Please try again.",
                "tool_calls": []
            }

    async def _execute_tool_call(self, tool_name: str, tool_args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a tool call through the MCP server.

        Args:
            tool_name: Name of the tool to call
            tool_args: Arguments for the tool

        Returns:
            Result of the tool call
        """
        try:
            # Construct the URL for the MCP server tool endpoint
            tool_url = f"{self.mcp_server_url}/{tool_name}"

            # Prepare the payload
            payload = {
                "arguments": tool_args
            }

            # Make the HTTP request to the MCP server
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    tool_url,
                    json=payload,
                    headers={"Content-Type": "application/json"}
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result
                    else:
                        error_text = await response.text()
                        return {
                            "success": False,
                            "message": f"Tool call failed with status {response.status}: {error_text}",
                            "error_code": f"MCP_SERVER_ERROR_{response.status}"
                        }

        except aiohttp.ClientConnectorError:
            return {
                "success": False,
                "message": f"Cannot connect to MCP server at {self.mcp_server_url}. Please ensure the MCP server is running.",
                "error_code": "MCP_SERVER_CONNECTION_ERROR"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error executing tool {tool_name}: {str(e)}",
                "error_code": "EXECUTION_ERROR"
            }

    def validate_intent(self, user_input: str) -> Dict[str, Any]:
        """
        Validate the user's intent from their input.

        Args:
            user_input: Raw user input

        Returns:
            Dictionary with intent and extracted parameters
        """
        # This would use more sophisticated NLP in a real implementation
        # For now, we rely on the OpenAI model's ability to understand intent

        return {
            "raw_input": user_input,
            "requires_tool": any(keyword in user_input.lower() for keyword in
                               ["add", "create", "new", "task", "list", "show",
                                "update", "change", "complete", "done", "finish",
                                "delete", "remove"])
        }