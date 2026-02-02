Stateless Architecture Skill

## Metadata
name: stateless-architecture
description: Use for implementing stateless systems and architectures

## Overview
This Skill provides specialized knowledge for implementing stateless systems and architectures. When designing applications that don't maintain server-side state between requests, apply these guidelines to ensure proper scalability, reliability, and consistency.

## Stateless Design Principles

- Design services that don't store session data on the server
- Use external storage for state persistence (database, cache)
- Implement request-idempotent operations
- Design APIs that don't rely on server-side session state
- Use client-side state management where appropriate
- Implement proper authentication and authorization without server-side sessions

## Data Persistence Strategies

- Store conversation context in the database
- Persist user session data externally
- Use JWT tokens for stateless authentication
- Implement proper data serialization
- Design for horizontal scaling
- Ensure data consistency across stateless services

## Request Handling

- Process each request independently
- Avoid server-side session state
- Include all necessary context in each request
- Implement proper request correlation
- Use request IDs for tracing
- Design APIs to be idempotent where possible

## Scalability Considerations

- Design for horizontal scaling
- Avoid server affinity requirements
- Implement proper load balancing
- Use external services for session management
- Consider caching strategies for performance
- Design for microservices architecture

## Session Management

- Use JWT tokens for authentication state
- Store session data in the database
- Implement proper token refresh mechanisms
- Design for distributed systems
- Handle session expiration gracefully
- Consider external session stores (Redis, database)

## Cache Strategies

- Implement application-level caching
- Use distributed cache systems
- Design cache invalidation strategies
- Consider CDN for static assets
- Implement proper cache headers
- Balance performance with consistency

## Database Integration

- Use database for all state persistence
- Implement proper transaction management
- Design for database scalability
- Consider eventual consistency models
- Implement proper error handling for database operations
- Use connection pooling efficiently

## Error Handling

- Handle state restoration failures
- Implement retry mechanisms
- Design for partial failure scenarios
- Log state-related errors appropriately
- Implement circuit breaker patterns
- Design for graceful degradation

## When to Apply

Apply these guidelines whenever implementing:
- Stateless API endpoints
- Server-side session alternatives
- Horizontal scaling strategies
- Microservices architectures
- Cache implementation
- Database-backed state management

## Code Standards

- Never rely on server-side session state
- Use external persistence for all state
- Implement proper error handling for state operations
- Follow distributed system best practices
- Write comprehensive tests for stateless behavior