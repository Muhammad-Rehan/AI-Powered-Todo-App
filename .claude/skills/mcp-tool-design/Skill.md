MCP Tool Design Skill

## Metadata
name: mcp-tool-design
description: Use for designing and implementing Model Context Protocol (MCP) tools

## Overview
This Skill provides specialized knowledge for designing and implementing Model Context Protocol (MCP) tools. When creating MCP tools for AI agents, defining tool schemas, or implementing tool execution logic, apply these guidelines to ensure proper structure, determinism, and stateless operation.

## MCP Tool Best Practices

- Design stateless tools that don't maintain in-memory state
- Implement deterministic behavior for identical inputs
- Define clear input and output schemas using JSON Schema
- Implement proper error handling within tools
- Use structured, machine-readable outputs
- Validate all input parameters before processing
- Follow MCP SDK conventions and patterns

## Tool Schema Design

- Define comprehensive JSON Schema for input parameters
- Include clear descriptions for all parameters
- Mark required parameters appropriately
- Use appropriate data types for all fields
- Include examples for complex parameters
- Validate parameter values within acceptable ranges

## Tool Implementation

- Implement business logic for each tool separately
- Perform user ownership validation within each tool
- Use database connections for all persistence operations
- Return structured responses with success indicators
- Include human-readable messages in responses
- Handle edge cases and error conditions gracefully

## Statelessness

- Never store state in memory between tool calls
- Use database persistence for all data operations
- Implement tools as pure functions where possible
- Avoid global variables or instance state
- Ensure tools can run independently
- Design for horizontal scalability

## Security Implementation

- Validate user identity and permissions within each tool
- Ensure user isolation (users can only modify their own data)
- Implement proper authentication checks
- Validate all input parameters for security
- Prevent privilege escalation scenarios
- Log tool execution for audit purposes

## Error Handling

- Implement comprehensive error handling within tools
- Return structured error responses
- Distinguish between user errors and system errors
- Provide clear error messages without exposing internals
- Handle database connection failures gracefully
- Implement timeouts for long-running operations

## Performance Considerations

- Optimize database queries within tools
- Implement efficient data retrieval patterns
- Use async operations where appropriate
- Minimize data transfer between components
- Consider caching for frequently accessed data
- Implement proper resource cleanup

## When to Apply

Apply these guidelines whenever implementing:
- MCP tool definitions
- Tool input/output schemas
- Tool business logic
- Database operations within tools
- Error handling for tool execution
- Security validation in tools

## Code Standards

- Always validate user ownership within tools
- Use structured output formats consistently
- Implement proper error handling for all scenarios
- Follow MCP SDK best practices
- Write comprehensive tests for tool functionality