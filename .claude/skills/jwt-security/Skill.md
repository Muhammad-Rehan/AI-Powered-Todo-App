JWT Security Skill

## Metadata
name: jwt-security
description: Use for implementing JWT security best practices and secure authentication systems

## Overview
This Skill provides specialized knowledge for implementing JWT security best practices and secure authentication systems. When creating secure JWT implementations, handling token validation, or implementing authentication security measures, apply these guidelines to ensure robust security.

## Token Generation Security

- Use strong cryptographic algorithms (RS256 preferred over HS256)
- Implement proper secret key management
- Generate cryptographically secure random tokens
- Use appropriate token expiration times
- Include proper claims in tokens
- Implement proper token signing procedures

## Secret Key Management

- Store secret keys in environment variables or secure vaults
- Never hardcode secrets in source code
- Implement key rotation strategies
- Use different keys for different environments
- Secure keys with appropriate access controls
- Regularly rotate signing keys

## Token Validation

- Verify token signatures using the correct public key
- Validate token expiration (exp claim)
- Validate issuer (iss claim) when applicable
- Validate audience (aud claim) when applicable
- Validate subject (sub claim) against expected user
- Reject tampered or invalid tokens immediately

## Security Headers and Transport

- Always use HTTPS in production environments
- Implement proper transport security
- Consider using HttpOnly cookies for token storage
- Prevent token exposure in URLs and logs
- Implement proper Content Security Policy
- Use secure headers for token protection

## Attack Prevention

- Protect against JWT confusion attacks
- Prevent algorithm confusion vulnerabilities
- Implement proper token validation order
- Protect against timing attacks in validation
- Validate all token claims thoroughly
- Prevent token replay attacks

## Token Scope and Permissions

- Include role/permission claims in tokens when needed
- Implement proper scope validation
- Limit token privileges to minimum required
- Validate user permissions during token use
- Implement role-based access control
- Include organization/user context in tokens

## Expiration and Refresh Strategies

- Set appropriate expiration times (not too long, not too short)
- Implement refresh token mechanisms when needed
- Handle token expiration gracefully
- Implement sliding expiration if appropriate
- Track token usage and refresh patterns
- Consider different expiration times for different use cases

## Error Handling and Logging

- Handle authentication failures securely
- Log authentication events without exposing sensitive data
- Implement proper error responses without information disclosure
- Monitor for suspicious authentication patterns
- Track failed authentication attempts
- Implement account lockout mechanisms if needed

## Storage Security

- Secure JWT storage on client-side
- Consider HttpOnly cookies for enhanced security
- Protect against XSS attacks that could steal tokens
- Implement proper session management
- Secure mobile app token storage appropriately
- Consider biometric authentication for sensitive tokens

## Compliance and Auditing

- Implement audit trails for authentication events
- Consider regulatory compliance requirements
- Implement proper data retention policies
- Log authentication events for security monitoring
- Support security incident investigation
- Document security procedures and protocols

## When to Apply

Apply these guidelines whenever implementing:
- JWT token creation and validation
- Authentication security measures
- Token storage and transmission
- Security audit and compliance
- Attack prevention mechanisms
- Token lifecycle management

## Code Standards

- Never log sensitive token information
- Validate all JWT claims thoroughly
- Use secure algorithms and proper key management
- Implement comprehensive error handling
- Write security-focused tests for authentication flows