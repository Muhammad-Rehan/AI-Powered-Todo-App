API Contract Enforcement Skill

## Metadata
name: api-contract-enforcement
description: Use for implementing and enforcing API contracts and specifications

## Overview
This Skill provides specialized knowledge for implementing and enforcing API contracts and specifications. When creating APIs that must adhere to specific contracts, validating requests/responses, or ensuring consistency with defined specifications, apply these guidelines to ensure proper contract adherence.

## Contract Definition

- Implement APIs that strictly follow OpenAPI specifications
- Define clear request/response schemas
- Document all API endpoints with proper specifications
- Use consistent HTTP status codes
- Implement proper error response formats
- Follow RESTful API conventions

## Schema Validation

- Use Pydantic models for request validation
- Implement response schema validation
- Validate all input parameters against contracts
- Enforce data type consistency
- Implement comprehensive validation rules
- Provide clear validation error messages

## Request Validation

- Validate all incoming request parameters
- Check required fields and data types
- Validate path parameters, query parameters, and request bodies
- Implement proper request sanitization
- Reject requests that don't conform to contracts
- Provide clear error responses for invalid requests

## Response Consistency

- Ensure all responses match contract specifications
- Use consistent response formats
- Include proper metadata in responses
- Implement proper error response structures
- Maintain backward compatibility
- Follow content negotiation patterns

## Version Management

- Implement API versioning strategies
- Maintain backward compatibility
- Plan for contract evolution
- Use proper media types for versioning
- Document breaking changes clearly
- Implement gradual deprecation strategies

## Testing and Verification

- Implement contract testing
- Validate API responses against schemas
- Test error scenarios and responses
- Implement automated contract validation
- Verify all endpoints against specifications
- Test edge cases and boundary conditions

## Documentation Alignment

- Keep documentation synchronized with implementation
- Generate API documentation from code when possible
- Implement self-documenting APIs
- Provide comprehensive API documentation
- Include examples for all endpoints
- Document error responses and codes

## Monitoring and Compliance

- Monitor API contract compliance
- Track deviations from contracts
- Implement alerting for contract violations
- Log API usage patterns
- Monitor error rates and response times
- Ensure consistent behavior across deployments

## When to Apply

Apply these guidelines whenever implementing:
- API endpoint design and implementation
- Request/response validation
- API contract compliance
- Automated testing for APIs
- API documentation generation
- Version management for APIs

## Code Standards

- Always validate against API contracts
- Implement comprehensive error handling
- Follow consistent response patterns
- Maintain API documentation accuracy
- Write comprehensive tests for contract compliance