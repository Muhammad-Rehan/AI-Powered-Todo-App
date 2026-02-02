JWT Auth Validation Skill

## Metadata
name: jwt-auth-validation
description: Use for implementing JWT-based authentication and validation systems

## Overview
This Skill provides specialized knowledge for implementing JWT-based authentication and validation systems. When creating authentication middleware, validating JWT tokens, or implementing user authorization, apply these guidelines to ensure secure and reliable authentication.

## JWT Implementation Best Practices

- Use python-jose or similar library for JWT operations
- Implement proper token signing and verification
- Use strong encryption algorithms (RS256 preferred)
- Store secret keys securely in environment variables
- Implement proper token expiration handling
- Validate token claims thoroughly

## Authentication Middleware

- Create reusable authentication dependencies in FastAPI
- Validate tokens for protected endpoints
- Extract user information from JWT payloads
- Handle expired tokens gracefully
- Implement refresh token functionality if needed
- Log authentication events for security monitoring

## Token Validation

- Verify token signature using the correct secret/key
- Validate token expiration (exp claim)
- Validate issuer (iss claim) if applicable
- Validate audience (aud claim) if applicable
- Validate subject (sub claim) matches expected user
- Reject tampered or invalid tokens immediately

## User Authorization

- Extract user ID or other identifiers from JWT
- Validate user permissions based on token claims
- Implement role-based access control if needed
- Ensure user isolation (users can only access their own data)
- Handle unauthorized access attempts with 401 responses
- Validate user existence and status during token validation

## Security Measures

- Use HTTPS in production environments
- Implement proper token storage on client side
- Prevent CSRF attacks when appropriate
- Implement token blacklisting for logout functionality
- Monitor for suspicious authentication patterns
- Rotate signing keys periodically

## Error Handling

- Return appropriate HTTP status codes (401, 403)
- Provide clear error messages without exposing sensitive information
- Log authentication failures for security monitoring
- Implement rate limiting for authentication attempts
- Handle token refresh scenarios appropriately

## When to Apply

Apply these guidelines whenever implementing:
- JWT token creation and validation
- Authentication middleware
- User authorization systems
- Protected API endpoints
- Token refresh mechanisms
- Logout functionality with token invalidation

## Code Standards

- Never hardcode secret keys in source code
- Validate all JWT claims thoroughly
- Use async functions for token validation operations
- Follow security best practices consistently
- Write comprehensive tests for authentication flows