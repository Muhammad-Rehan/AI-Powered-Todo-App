Auth Token Propagation Skill

## Metadata
name: auth-token-propagation
description: Use for implementing authentication token handling and propagation in applications

## Overview
This Skill provides specialized knowledge for implementing authentication token handling and propagation in applications. When managing JWT tokens, implementing authentication flows, or ensuring secure token transmission across components, apply these guidelines to ensure proper security and functionality.

## Token Storage

- Store JWT tokens securely in browser storage
- Use HttpOnly cookies for enhanced security when appropriate
- Implement proper token storage hierarchy (localStorage, sessionStorage, cookies)
- Secure tokens against XSS attacks
- Implement proper token cleanup and expiration handling
- Consider token refresh strategies

## Token Transmission

- Attach JWT tokens to API requests in Authorization header
- Implement proper token inclusion in HTTP requests
- Use Bearer token format consistently
- Handle token transmission for different API types
- Implement secure token transmission over HTTPS
- Consider token inclusion in request bodies when necessary

## Client-Side Management

- Implement token retrieval from storage
- Handle token validation and expiration checks
- Manage token refresh mechanisms
- Implement proper token cleanup on logout
- Handle token propagation across React components
- Secure token access in component lifecycles

## API Integration

- Configure API clients with token attachment
- Implement token refresh for expired tokens
- Handle authentication failures gracefully
- Manage concurrent requests with token refresh
- Implement retry mechanisms for authentication failures
- Secure API endpoints with proper authentication

## Security Measures

- Protect against CSRF attacks
- Implement proper token validation
- Secure tokens against XSS and injection attacks
- Use secure cookie attributes when applicable
- Implement token rotation strategies
- Monitor for token misuse or leaks

## Token Lifecycle

- Handle token acquisition during login
- Manage token renewal and refresh
- Implement proper logout and token invalidation
- Handle token expiration gracefully
- Implement token cleanup on session end
- Manage token persistence across application restarts

## Error Handling

- Handle authentication failures appropriately
- Manage token refresh failures
- Implement fallback authentication mechanisms
- Provide clear error messages without exposing security details
- Log authentication-related errors for monitoring
- Handle network failures during token operations

## Component Integration

- Pass tokens through component props when needed
- Use React Context for token sharing across components
- Implement authentication HOCs or hooks
- Handle token availability in server components
- Manage token state in client components
- Secure token access in custom hooks

## Performance Considerations

- Optimize token retrieval and validation
- Implement caching for token validation results
- Minimize token-related operations in rendering
- Handle token propagation asynchronously
- Optimize token refresh frequency
- Reduce token-related network requests

## When to Apply

Apply these guidelines whenever implementing:
- JWT token management systems
- Authentication flow handling
- Secure token transmission
- Token refresh mechanisms
- API authentication integration
- Component-level token access

## Code Standards

- Never expose tokens in URLs or query parameters
- Implement proper error handling for all token operations
- Use secure storage and transmission methods
- Follow authentication best practices consistently
- Write comprehensive tests for token handling flows