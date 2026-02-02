Conversation Testing Skill

## Metadata
name: conversation-testing
description: Use for testing conversational AI systems and chatbot functionality

## Overview
This Skill provides specialized knowledge for testing conversational AI systems and chatbot functionality. When creating test suites for chatbots, validating conversation flows, or verifying natural language processing capabilities, apply these guidelines to ensure comprehensive testing coverage.

## Test Strategy

- Develop comprehensive test scenarios for conversation flows
- Test both happy path and error scenarios
- Create tests for different conversation contexts
- Implement boundary condition testing
- Design tests for edge cases and unexpected inputs
- Consider multi-turn conversation testing

## Natural Language Testing

- Test various phrasings for the same intent
- Validate intent recognition accuracy
- Test handling of ambiguous requests
- Verify appropriate responses to unclear inputs
- Test language variation and synonyms
- Validate negation handling

## Conversation Flow Testing

- Test sequential conversation steps
- Validate context preservation across turns
- Verify conversation state management
- Test interruption and topic changes
- Validate conversation continuity
- Handle conversation timeouts appropriately

## Tool Integration Testing

- Test MCP tool invocation accuracy
- Verify tool parameters are passed correctly
- Validate tool response handling
- Test chained tool execution
- Verify error handling from tools
- Test tool response formatting

## Error Scenario Testing

- Test invalid user inputs
- Validate graceful error handling
- Test system error responses
- Verify fallback mechanism functionality
- Test rate limiting scenarios
- Handle service unavailability gracefully

## Performance Testing

- Test response time under various loads
- Validate concurrent conversation handling
- Test memory usage during long conversations
- Verify system stability during extended use
- Test database performance with conversation history
- Validate API rate limits and throttling

## User Experience Testing

- Validate response quality and relevance
- Test conversation coherence
- Verify user-friendly error messages
- Validate loading and transition states
- Test accessibility considerations
- Ensure consistent tone and personality

## Data Validation Testing

- Verify conversation persistence
- Test user data isolation
- Validate conversation history accuracy
- Test data integrity during conversation
- Verify proper cleanup and retention
- Validate backup and recovery scenarios

## Security Testing

- Test for prompt injection vulnerabilities
- Validate input sanitization
- Test authentication in conversation context
- Verify user data protection
- Test for information disclosure
- Validate secure token handling

## Regression Testing

- Create baseline conversation tests
- Implement automated regression testing
- Track conversation quality metrics
- Monitor for behavioral changes
- Validate backward compatibility
- Test new features with existing flows

## Monitoring and Analytics

- Implement conversation success tracking
- Monitor error rates and failure patterns
- Track user satisfaction indicators
- Log conversation metrics for analysis
- Monitor system performance during conversations
- Implement alerting for critical failures

## When to Apply

Apply these guidelines whenever implementing:
- Chatbot functionality testing
- Natural language processing validation
- Conversation flow verification
- Tool integration testing
- Error handling validation
- Performance and load testing

## Code Standards

- Implement comprehensive test coverage for all conversation paths
- Use realistic test data and scenarios
- Follow consistent testing patterns and methodologies
- Validate both functional and non-functional requirements
- Write maintainable and understandable test cases