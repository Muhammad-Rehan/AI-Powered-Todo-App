Tool Routing Skill

## Metadata
name: tool-routing
description: Use for routing natural language to appropriate tools and functions

## Overview
This Skill provides specialized knowledge for routing natural language to appropriate tools and functions. When implementing natural language understanding, intent classification, or mapping user requests to specific tools, apply these guidelines to ensure accurate and reliable routing.

## Intent Classification

- Analyze user input to determine intent
- Map natural language to specific tool functions
- Implement confidence scoring for routing decisions
- Handle ambiguous requests appropriately
- Provide fallback mechanisms for uncertain routing
- Use context to improve routing accuracy

## Tool Matching

- Match user requests to available tools
- Implement fuzzy matching for variations in language
- Consider synonyms and alternative phrasings
- Use tool descriptions for matching logic
- Implement hierarchical routing for complex requests
- Handle compound requests requiring multiple tools

## Context-Aware Routing

- Use conversation history for improved routing
- Consider current conversation state
- Implement context-sensitive tool selection
- Handle follow-up requests appropriately
- Use previous tool calls to inform routing decisions
- Maintain context for multi-turn interactions

## Ambiguity Handling

- Detect ambiguous user requests
- Ask clarifying questions when needed
- Provide suggestions for unclear requests
- Implement disambiguation flows
- Handle partial matches appropriately
- Allow user to refine their requests

## Error Handling

- Handle unmatched requests gracefully
- Provide helpful error messages
- Suggest alternative tools or actions
- Implement fallback responses
- Log routing failures for improvement
- Recover from routing errors gracefully

## Performance Optimization

- Optimize routing algorithm performance
- Implement caching for frequent routing decisions
- Use efficient data structures for tool matching
- Minimize latency in routing decisions
- Implement asynchronous routing when needed
- Profile routing performance regularly

## Learning and Adaptation

- Track routing effectiveness
- Learn from user corrections
- Improve routing accuracy over time
- Implement feedback mechanisms
- Monitor routing success rates
- Adjust routing logic based on usage patterns

## Multi-Step Routing

- Handle complex requests requiring multiple tools
- Implement sequential tool execution
- Manage state between tool calls
- Handle conditional tool execution
- Implement rollback for failed sequences
- Provide clear feedback during multi-step operations

## When to Apply

Apply these guidelines whenever implementing:
- Natural language to tool mapping
- Intent classification systems
- Dynamic tool selection
- Ambiguity resolution
- Multi-step operation routing
- Context-aware command interpretation

## Code Standards

- Always validate routing decisions before tool execution
- Implement proper error handling for routing failures
- Use context to improve routing accuracy
- Provide clear feedback for routing decisions
- Write comprehensive tests for routing logic