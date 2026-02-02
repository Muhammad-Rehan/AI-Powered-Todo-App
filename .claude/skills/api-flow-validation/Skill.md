API Flow Validation Skill

## Metadata
name: api-flow-validation
description: Use for validating API request/response flows and integration scenarios

## Overview
This Skill provides specialized knowledge for validating API request/response flows and integration scenarios. When testing API interactions, validating request/response patterns, or ensuring API integration correctness, apply these guidelines to ensure proper API behavior and reliability.

## Request Validation

- Validate API request structure and content
- Check required parameters and data types
- Verify parameter validation and sanitization
- Test different request formats and encodings
- Validate authentication headers and tokens
- Check request size and rate limits

## Response Validation

- Verify API response structure and schema
- Validate HTTP status codes for different scenarios
- Check response time and performance metrics
- Validate error response formats and messages
- Test response data accuracy and completeness
- Verify response headers and metadata

## Integration Testing

- Test complete API call chains and dependencies
- Validate data flow between multiple API endpoints
- Test API interactions with external services
- Verify proper error propagation between services
- Check transactional consistency across APIs
- Validate callback and webhook functionality

## Authentication Flows

- Test authentication token validity and expiration
- Validate JWT token handling and verification
- Check session management and refresh flows
- Test unauthorized access scenarios
- Verify proper authentication error responses
- Validate multi-factor authentication flows

## Business Logic Validation

- Test API endpoints against business requirements
- Validate data transformation and processing
- Check business rule enforcement
- Test conditional logic execution
- Verify data consistency across related endpoints
- Validate complex workflow scenarios

## Error Handling Validation

- Test API behavior with invalid inputs
- Validate error response consistency
- Check proper error logging and monitoring
- Test API resilience to failures
- Verify graceful degradation patterns
- Test recovery from error states

## Performance Validation

- Measure API response times under various loads
- Test concurrent request handling
- Validate API rate limiting functionality
- Check memory and resource usage patterns
- Test API behavior under stress conditions
- Verify API scalability characteristics

## Security Validation

- Test API vulnerability to injection attacks
- Validate input sanitization and validation
- Check proper authentication enforcement
- Test authorization bypass attempts
- Verify sensitive data protection
- Validate secure communication protocols

## State Management Validation

- Test API behavior with different application states
- Validate session and state persistence
- Check consistency across multiple requests
- Test concurrent state modification
- Verify state recovery after failures
- Validate cache behavior and invalidation

## Data Consistency Validation

- Test data integrity across API operations
- Validate transactional behavior
- Check data synchronization between services
- Test concurrent data modification scenarios
- Verify data validation and constraints
- Validate backup and recovery procedures

## Contract Compliance

- Validate API adherence to OpenAPI specifications
- Check backward compatibility with older clients
- Verify proper versioning implementation
- Test API contract evolution scenarios
- Validate response schema compliance
- Check proper deprecation handling

## When to Apply

Apply these guidelines whenever implementing:
- API integration testing
- Request/response validation
- Authentication flow testing
- Business logic verification
- Error handling validation
- Performance and load testing

## Code Standards

- Implement comprehensive validation for all API interactions
- Use proper test data and realistic scenarios
- Follow consistent validation patterns and methodologies
- Validate both positive and negative test cases
- Write maintainable and reliable validation tests