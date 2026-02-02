Edge Case Analysis Skill

## Metadata
name: edge-case-analysis
description: Use for identifying and handling edge cases and boundary conditions in applications

## Overview
This Skill provides specialized knowledge for identifying and handling edge cases and boundary conditions in applications. When analyzing potential failure points, considering unusual usage scenarios, or ensuring robustness under extreme conditions, apply these guidelines to ensure comprehensive coverage and reliable behavior.

## Boundary Condition Analysis

- Identify input range boundaries and limits
- Test maximum and minimum value scenarios
- Analyze off-by-one errors and fencepost problems
- Consider buffer overflow and underflow scenarios
- Test empty and null input conditions
- Validate edge cases in mathematical operations

## Exceptional Flow Analysis

- Identify potential error and exception scenarios
- Consider failure points in system components
- Analyze resource exhaustion conditions
- Test system behavior under stress conditions
- Consider race conditions and concurrency issues
- Evaluate failure recovery mechanisms

## Data Type Boundaries

- Test integer overflow and underflow conditions
- Consider floating-point precision errors
- Analyze string length and character encoding issues
- Test boolean logic edge cases
- Consider data type conversion anomalies
- Validate timezone and date/time edge cases

## User Interaction Boundaries

- Consider rapid-fire user interactions
- Test simultaneous actions from multiple users
- Analyze interrupted or abandoned processes
- Consider unusual user input patterns
- Test accessibility and alternative input methods
- Validate internationalization edge cases

## Resource Limitations

- Test memory and storage constraints
- Analyze network timeout scenarios
- Consider CPU and processing limitations
- Test database connection pool exhaustion
- Evaluate file descriptor limits
- Analyze disk space constraints

## Concurrency Scenarios

- Consider simultaneous access to shared resources
- Test race conditions in multi-threaded code
- Analyze deadlocks and livelocks
- Consider transaction isolation issues
- Test distributed system consistency
- Evaluate locking mechanism failures

## System State Transitions

- Analyze state machine edge cases
- Test invalid state transitions
- Consider partial state updates
- Evaluate system recovery from corrupted states
- Test state persistence failures
- Analyze state synchronization issues

## Network and Communication

- Test network partition scenarios
- Consider intermittent connectivity issues
- Analyze message ordering and duplication
- Test timeout and retry mechanisms
- Consider packet loss and corruption
- Evaluate API rate limiting impacts

## Time-Related Conditions

- Test daylight saving time transitions
- Consider leap year and leap second scenarios
- Analyze clock skew in distributed systems
- Test system behavior at month/year boundaries
- Consider high-resolution timing issues
- Evaluate scheduled task edge cases

## Integration Points

- Test API boundary conditions
- Consider third-party service failures
- Analyze data format compatibility issues
- Test version compatibility scenarios
- Consider service dependency failures
- Evaluate data migration edge cases

## Security Boundaries

- Test input validation bypass attempts
- Consider privilege escalation scenarios
- Analyze authentication boundary conditions
- Test authorization edge cases
- Consider data sanitization failures
- Evaluate secure communication boundaries

## Performance Boundaries

- Test system behavior under peak loads
- Consider cold start and warm-up scenarios
- Analyze memory allocation patterns
- Test garbage collection impacts
- Consider caching boundary conditions
- Evaluate database query performance edges

## Recovery and Resilience

- Test system behavior after failures
- Consider data recovery scenarios
- Analyze graceful degradation patterns
- Test failover mechanisms
- Consider backup and restore edge cases
- Evaluate disaster recovery procedures

## When to Apply

Apply these guidelines whenever implementing:
- System reliability and robustness analysis
- Comprehensive test case design
- Error handling and exception management
- Performance and stress testing
- Security vulnerability assessment
- Data validation and input sanitization

## Code Standards

- Always consider boundary conditions in implementation
- Implement comprehensive error handling for edge cases
- Follow defensive programming practices
- Write tests that specifically target edge cases
- Document edge case handling in code comments