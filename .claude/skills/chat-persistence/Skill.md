Chat Persistence Skill

## Metadata
name: chat-persistence
description: Use for implementing conversation and message persistence systems

## Overview
This Skill provides specialized knowledge for implementing chat conversation and message persistence systems. When creating database models for conversations, storing messages, or implementing conversation history features, apply these guidelines to ensure proper data structure, performance, and user isolation.

## Conversation Data Modeling

- Create proper Conversation model with user_id, created_at, updated_at
- Implement Message model with conversation_id, user_id, role, content, created_at
- Use UUIDs for conversation and message identifiers
- Include metadata fields for tool calls and AI responses
- Implement proper foreign key relationships between models
- Ensure proper indexing for frequently queried fields

## Message Storage

- Store user and AI assistant messages separately
- Include role field to distinguish between user and assistant messages
- Store conversation context with each message
- Implement proper serialization for complex message data
- Include timestamps for all messages
- Store tool call metadata when MCP tools are invoked

## Conversation Management

- Create new conversations when needed
- Associate messages with correct conversations
- Implement conversation history retrieval
- Support multiple conversations per user
- Implement conversation cleanup and archival if needed
- Maintain conversation context across requests

## User Isolation

- Ensure users can only access their own conversations
- Validate user_id in all conversation operations
- Implement proper foreign key constraints
- Use user_id in all query filters
- Prevent cross-user data access
- Implement proper access controls for conversation sharing if needed

## Performance Optimization

- Implement proper indexing for conversation queries
- Use pagination for large conversation histories
- Optimize database queries for message retrieval
- Cache frequently accessed conversation data if appropriate
- Implement efficient message insertion patterns
- Consider database partitioning for large datasets

## Data Integrity

- Implement proper transaction management
- Ensure atomic operations for message creation
- Validate message relationships before storage
- Implement proper error handling for database operations
- Maintain referential integrity between models
- Handle database constraint violations gracefully

## Privacy and Compliance

- Implement data retention policies
- Support data export functionality
- Implement proper data deletion procedures
- Consider privacy regulations (GDPR, CCPA) compliance
- Implement audit logging for data access
- Encrypt sensitive message content if required

## When to Apply

Apply these guidelines whenever implementing:
- Conversation model definitions
- Message storage systems
- Conversation history retrieval
- User isolation mechanisms
- Performance optimization for chat data
- Data privacy and compliance features

## Code Standards

- Always validate user ownership before data access
- Use async operations for all database interactions
- Implement proper error handling for persistence operations
- Follow database transaction best practices
- Write comprehensive tests for persistence functionality