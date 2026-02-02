<!--
Sync Impact Report:
Version change: 1.0.0 -> 1.1.0
List of modified principles:
- Spec-Driven Development (updated to reflect AI chatbot context)
- Code Quality & Architecture (updated for stateless chatbot backend)
- API Correctness & Consistency (updated to reflect MCP tools)
- Authentication & Security (retained for JWT user isolation)
- Data Integrity & Persistence (retained for database persistence)
- User Experience Consistency (updated for AI chatbot UX)
- Performance & Scalability (retained for performance requirements)
- Error Handling & Reliability (updated for graceful error handling)
- Added: AI Decision-Making Principle (new principle for OpenAI Agents)
- Added: MCP Tool Determinism Principle (new principle for deterministic tools)
- Added: Conversation State Recovery Principle (new principle for context recovery)

Added sections: AI Decision-Making, MCP Tool Determinism, Conversation State Recovery
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
Follow-up TODOs: None
-->
# Todo AI Chatbot (Phase III) Constitution

## Core Principles

### Spec-Driven Development
All development must follow the Agentic Dev Stack workflow. No implementation without approved spec, plan, and tasks. AI chatbot functionality must be designed with clear intent mapping and conversation flows before implementation.

### Code Quality & Architecture
Backend must remain fully stateless with all conversation history and task state persisted in database. Clear separation between AI agent logic, MCP server tools, and data persistence layers. Architecture must support AI decision-making via OpenAI Agents SDK without hardcoded intent logic outside the agent.

### API Correctness & Consistency
All task operations (add, list, update, delete, complete) must be executed only via MCP tools exposed by a dedicated MCP server. MCP tools must be deterministic, side-effect safe, and persist all changes directly to the database. All responses must be predictable, validated, and user-scoped through JWT authentication.

### Authentication & Security
All API requests must require a valid JWT token. JWT verification must be enforced on every backend request. Users must only access and modify their own tasks. Shared JWT secret must be consistently applied across frontend and backend. Task access must be strictly isolated per user with no cross-user data leakage allowed.

### Data Integrity & Persistence
All task data and conversation history must be stored in database with proper user scoping. ORM models must accurately represent database schema with user ownership relationships. Task ownership and conversation history must be enforced at the database query level with strict user isolation.

### User Experience Consistency
AI chatbot must provide natural language interface with clear, user-friendly confirmations for all successful task actions. Responses must be consistent and contextual, maintaining conversation flow. All interactions must feel natural and intuitive through AI-powered responses rather than rigid command structures.

### AI Decision-Making Principle
AI decision-making must be handled exclusively by OpenAI Agents SDK. No hardcoded intent logic should exist outside the agent. The system must rely on AI to interpret natural language and map to appropriate MCP tools without predetermined rule-based routing for intents like add, list, update, delete, or complete tasks.

### MCP Tool Determinism Principle
MCP tools must be deterministic and side-effect safe, with all changes persisted directly to the database. Each tool must have predictable behavior and return consistent results for identical inputs. Tools must handle all persistence directly without relying on external state management for task operations.

### Conversation State Recovery Principle
Conversation context must be fully recoverable after server restarts using stored messages. Both conversation history and task state must be retrievable from persistent storage to maintain continuity. System must restore complete context without loss of conversation flow or task information upon restart.

## Performance & Scalability
AI agent responses must be delivered efficiently with reasonable latency. Database queries must be optimized and scoped by user. Stateless backend behavior must be preserved via JWT auth while maintaining conversation context through database persistence. System must handle concurrent conversations without cross-contamination of context or data.

## Error Handling & Reliability
Invalid inputs and edge cases must be handled gracefully without breaking conversation flow. Task-not-found and invalid-input errors must be managed with appropriate user feedback. System must not expose internal errors or sensitive data while maintaining conversation continuity. AI agent must recover gracefully from misinterpretation of user intent.

## Governance
Deterministic Behavior: Same authenticated request must always produce the same result through MCP tools. No hidden state or cross-user side effects are allowed. Reviewability & Auditability: Each conversation and task operation must be traceable from user input to database persistence. Code and structure must be easy to review and reason about with clear separation between AI agent logic and MCP tool implementations.

**Version**: 1.1.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2026-01-23