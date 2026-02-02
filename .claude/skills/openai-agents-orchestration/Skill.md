OpenAI Agents Orchestration Skill

## Metadata
name: openai-agents-orchestration
description: Use for orchestrating OpenAI Agents SDK and managing agent workflows

## Overview
This Skill provides specialized knowledge for orchestrating OpenAI Agents SDK and managing agent workflows. When creating AI agent systems, integrating with MCP tools, or managing agent execution flows, apply these guidelines to ensure proper orchestration and tool integration.

## Agent Configuration

- Configure OpenAI agents with proper system instructions
- Register MCP tools with the agent
- Set up proper tool calling configurations
- Configure agent parameters for optimal performance
- Implement proper error handling for agent operations
- Manage agent state and context appropriately

## Tool Integration

- Integrate MCP tools with OpenAI agents
- Map natural language to appropriate tool calls
- Handle tool execution results properly
- Implement chained tool usage when needed
- Manage tool execution order and dependencies
- Validate tool call parameters before execution

## Context Management

- Provide conversation history to agents
- Manage context windows and token limits
- Implement proper context serialization
- Handle context persistence across requests
- Implement context recovery mechanisms
- Optimize context for agent performance

## Response Processing

- Process agent responses appropriately
- Handle direct responses vs tool calls
- Format responses for end users
- Implement response validation
- Handle partial response scenarios
- Manage streaming responses if applicable

## Error Handling

- Handle agent execution errors gracefully
- Manage tool call failures
- Implement retry mechanisms for failures
- Provide fallback responses when needed
- Log agent execution for debugging
- Handle token limit exceeded scenarios

## Performance Optimization

- Optimize agent response times
- Implement proper caching strategies
- Manage token usage efficiently
- Optimize context window usage
- Handle concurrent agent requests
- Implement proper resource management

## Security Considerations

- Validate agent outputs for safety
- Implement proper input sanitization
- Handle sensitive information appropriately
- Implement rate limiting for agent usage
- Monitor for prompt injection attempts
- Secure agent configurations and keys

## State Management

- Maintain conversation state without server-side sessions
- Use database for conversation persistence
- Implement proper context recovery
- Handle conversation continuity across requests
- Manage multiple concurrent conversations
- Implement conversation cleanup when needed

## When to Apply

Apply these guidelines whenever implementing:
- OpenAI agent configuration
- Tool integration with agents
- Agent response processing
- Context management for agents
- Error handling for agent operations
- Performance optimization for agents

## Code Standards

- Always validate agent outputs before user presentation
- Implement proper error handling for all agent operations
- Follow OpenAI API best practices
- Secure agent configurations and API keys
- Write comprehensive tests for agent workflows