FastAPI API Design Skill

## Metadata
name: fastapi-api-design
description: Use for designing and implementing FastAPI endpoints, request/response schemas, and API architecture

## Overview
This Skill provides specialized knowledge for designing and implementing FastAPI endpoints following best practices and architectural principles. When creating API endpoints, request/response schemas, or API architecture, apply these guidelines to ensure proper structure, validation, and documentation.

## FastAPI Best Practices

- Use Pydantic models for request/response validation
- Implement proper HTTP status codes (200, 201, 400, 401, 404, 500, etc.)
- Follow RESTful API conventions
- Use dependency injection for authentication and authorization
- Implement comprehensive request validation
- Provide clear API documentation with OpenAPI/Swagger

## Request/Response Design

- Define clear input/output schemas using Pydantic models
- Validate all incoming request data
- Use proper type hints for all function parameters
- Implement error response schemas
- Follow consistent naming conventions for endpoints
- Use path parameters, query parameters, and request bodies appropriately

## Security Implementation

- Implement JWT token authentication using FastAPI dependencies
- Validate user permissions for each endpoint
- Use proper authentication middleware
- Implement rate limiting where appropriate
- Sanitize all user inputs
- Prevent common security vulnerabilities

## Performance Considerations

- Use async/await for all I/O operations
- Implement proper caching strategies
- Use pagination for large datasets
- Optimize database queries
- Implement proper error handling without exposing internal details

## When to Apply

Apply these guidelines whenever implementing:
- New API endpoints
- Request/response schema design
- Authentication and authorization logic
- API documentation
- Error handling patterns
- Performance optimizations
- Security measures

## Code Standards

- Use async functions for all I/O operations
- Implement proper error handling with HTTPException
- Follow FastAPI dependency injection patterns
- Use type hints for all functions
- Write comprehensive tests for API endpoints