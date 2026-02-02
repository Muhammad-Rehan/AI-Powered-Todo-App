OpenAI ChatKit UI Skill

## Metadata
name: openai-chatkit-ui
description: Use for implementing OpenAI ChatKit UI components and interfaces

## Overview
This Skill provides specialized knowledge for implementing OpenAI ChatKit UI components and interfaces. When creating chat interfaces, integrating ChatKit components, or implementing conversational UI elements, apply these guidelines to ensure proper functionality and user experience.

## ChatKit Integration

- Properly initialize ChatKit components
- Configure ChatKit with appropriate settings
- Implement proper event handlers for chat interactions
- Handle ChatKit lifecycle events appropriately
- Customize ChatKit appearance and behavior
- Integrate ChatKit with application state

## Component Architecture

- Create reusable chat UI components
- Implement proper component hierarchy
- Use appropriate state management for chat features
- Handle component props and callbacks effectively
- Implement proper error boundaries for chat components
- Create consistent component interfaces

## User Experience Design

- Implement smooth chat interaction flows
- Handle loading states and transitions
- Provide clear feedback for user actions
- Implement proper error messaging
- Handle different message types (text, errors, confirmations)
- Ensure responsive design across devices

## Message Display

- Format messages appropriately for display
- Handle different message roles (user, assistant)
- Implement proper message threading
- Display tool call results and metadata
- Show typing indicators and status updates
- Handle rich content in messages

## State Management

- Manage conversation state effectively
- Handle message history and persistence
- Implement proper state synchronization
- Handle concurrent conversations if needed
- Manage loading and error states
- Implement undo/redo functionality if appropriate

## API Integration

- Connect chat UI to backend API endpoints
- Handle JWT token attachment to requests
- Implement proper request/response handling
- Manage network error scenarios
- Handle authentication failures gracefully
- Implement retry mechanisms for failed requests

## Accessibility

- Implement proper ARIA attributes
- Ensure keyboard navigation support
- Provide screen reader compatibility
- Follow WCAG accessibility guidelines
- Implement proper color contrast ratios
- Support various accessibility needs

## Performance Optimization

- Optimize rendering for large message histories
- Implement virtual scrolling for long chats
- Optimize network requests and caching
- Handle memory management for chat components
- Implement proper cleanup for unmounted components
- Optimize image and media loading

## Error Handling

- Handle API connection failures
- Manage authentication errors
- Display appropriate error messages to users
- Implement graceful degradation
- Handle message sending failures
- Provide recovery options for errors

## When to Apply

Apply these guidelines whenever implementing:
- OpenAI ChatKit integration
- Chat interface components
- Message display and interaction
- API connection for chat features
- State management for conversations
- Accessibility features for chat UI

## Code Standards

- Follow React/Next.js best practices for components
- Implement proper error handling for all interactions
- Use TypeScript for type safety
- Ensure accessibility compliance
- Write comprehensive tests for UI components