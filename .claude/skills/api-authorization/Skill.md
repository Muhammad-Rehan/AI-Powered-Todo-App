API Authorization Skill

## Metadata
name: api-authorization
description: Use for implementing API authorization and access control systems

## Overview
This Skill provides specialized knowledge for implementing API authorization and access control systems. When creating authorization logic, implementing access controls, or securing API endpoints, apply these guidelines to ensure proper security and access management.

## Access Control Models

- Implement role-based access control (RBAC) when appropriate
- Use attribute-based access control (ABAC) for complex scenarios
- Implement resource-based access control for fine-grained permissions
- Design authorization policies that scale with application growth
- Consider hierarchical access control models
- Implement principle of least privilege

## Authorization Logic

- Validate user permissions before data access
- Implement authorization checks at appropriate layers
- Use centralized authorization services when possible
- Implement proper authorization caching
- Handle authorization decisions consistently
- Log authorization decisions for audit purposes

## Resource-Level Authorization

- Implement user isolation (users can only access their own data)
- Validate ownership before resource modification
- Implement proper foreign key validation
- Check permissions at the database query level
- Handle resource sharing scenarios appropriately
- Implement soft delete policies where needed

## API Endpoint Protection

- Implement authorization middleware for protected endpoints
- Validate user permissions for each API operation
- Use dependency injection for authorization checks
- Implement proper authorization error responses
- Handle bulk operations with appropriate authorization
- Validate nested resource access permissions

## Permission Management

- Design clear permission hierarchies
- Implement permission inheritance patterns
- Use permission constants for consistency
- Implement permission evaluation algorithms
- Handle permission changes dynamically
- Support temporary permission grants

## Database-Level Security

- Implement row-level security where appropriate
- Use parameterized queries to prevent injection
- Validate user IDs in all database queries
- Implement proper foreign key constraints
- Use database views for access control when needed
- Implement audit logging for sensitive operations

## Multi-Tenant Authorization

- Implement tenant isolation for multi-tenant systems
- Validate tenant access for all operations
- Handle cross-tenant data access restrictions
- Implement tenant-specific permissions
- Manage shared resources appropriately
- Consider tenant data segregation requirements

## Error Handling

- Return appropriate HTTP status codes (401, 403, 404)
- Provide clear authorization error messages
- Log authorization failures for security monitoring
- Handle authorization cascading failures
- Implement graceful degradation for authorization systems
- Prevent information disclosure in error responses

## Performance Considerations

- Optimize authorization query performance
- Implement authorization result caching
- Use efficient permission lookup algorithms
- Minimize database round trips for authorization
- Implement authorization result batching when appropriate
- Consider asynchronous authorization for complex scenarios

## Security Measures

- Implement defense against authorization bypass
- Validate all inputs in authorization logic
- Prevent elevation of privilege scenarios
- Implement proper audit logging for access
- Monitor for unusual authorization patterns
- Secure authorization configuration data

## When to Apply

Apply these guidelines whenever implementing:
- API endpoint access controls
- User permission systems
- Resource-level authorization
- Multi-tenant access controls
- Role-based access systems
- Fine-grained permission management

## Code Standards

- Always validate user permissions before data access
- Implement consistent authorization patterns
- Use secure error handling that doesn't leak information
- Follow security best practices for all authorization logic
- Write comprehensive tests for authorization scenarios