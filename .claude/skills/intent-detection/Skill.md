Intent Detection Skill

## Metadata
name: intent-detection
description: Use for detecting user intent from natural language input

## Overview
This Skill provides specialized knowledge for detecting user intent from natural language input. When analyzing user messages, determining their underlying intentions, or mapping natural language to specific actions, apply these guidelines to ensure accurate and reliable intent detection.

## Natural Language Analysis

- Analyze user input for semantic meaning
- Identify keywords and phrases indicating intent
- Consider context and conversation history
- Handle variations in language and phrasing
- Detect negations and conditional statements
- Recognize implicit and explicit requests

## Intent Categories

- Define clear categories for different intents
- Support common task management intents (add, list, update, delete, complete)
- Implement intent hierarchy for complex requests
- Handle compound intents requiring multiple actions
- Support contextual intent variations
- Implement intent confidence scoring

## Context Awareness

- Use conversation history to inform intent detection
- Consider the current conversation state
- Apply context-specific intent interpretation
- Handle follow-up requests appropriately
- Maintain context for multi-turn interactions
- Use previous intents to inform current analysis

## Linguistic Patterns

- Identify common phrasing patterns for each intent
- Handle synonyms and alternative expressions
- Recognize intent regardless of sentence structure
- Consider idiomatic expressions and colloquialisms
- Handle misspellings and grammatical variations
- Use linguistic features for intent classification

## Confidence Scoring

- Assign confidence scores to detected intents
- Implement threshold-based decision making
- Handle low-confidence detections appropriately
- Provide uncertainty indicators when needed
- Use multiple signals for confidence assessment
- Allow for intent correction mechanisms

## Ambiguity Resolution

- Detect ambiguous requests requiring clarification
- Implement disambiguation strategies
- Ask clarifying questions when needed
- Provide suggestions for unclear intents
- Allow users to specify their intent more clearly
- Handle partially understood requests

## Error Handling

- Handle unrecognizable intents gracefully
- Provide helpful fallback responses
- Suggest alternative interpretations
- Log intent detection failures for analysis
- Implement recovery from detection errors
- Maintain conversation flow despite detection issues

## Machine Learning Integration

- Use ML models for intent classification when appropriate
- Train models on domain-specific data
- Implement continuous learning from user interactions
- Fine-tune models for specific use cases
- Monitor model performance and accuracy
- Update models based on usage patterns

## Validation and Verification

- Validate detected intents against available actions
- Cross-check intents with conversation context
- Verify intent feasibility before action execution
- Implement intent confirmation when needed
- Allow for intent correction by users
- Log intent-action correlations for improvement

## When to Apply

Apply these guidelines whenever implementing:
- Natural language understanding systems
- Intent classification algorithms
- Chatbot command interpretation
- Voice command processing
- Text-based action mapping
- Conversational AI systems

## Code Standards

- Always validate intent detection results before action execution
- Implement proper error handling for detection failures
- Use confidence scoring to improve reliability
- Consider context in intent interpretation
- Write comprehensive tests for intent detection