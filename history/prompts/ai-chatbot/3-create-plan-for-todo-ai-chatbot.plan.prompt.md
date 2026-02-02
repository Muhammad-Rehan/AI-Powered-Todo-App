---
id: 3
title: Create Plan For Todo AI Chatbot
stage: plan
date: 2026-01-23
surface: agent
model: claude-opus-4-5-20251101
feature: ai-chatbot
branch: 002-ai-chatbot
user: user
command: sp.plan
labels: [plan, ai-chatbot, mcp-tools, architecture]
links:
  spec: ./spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-ai-chatbot/plan.md
 - specs/002-ai-chatbot/research.md
 - specs/002-ai-chatbot/data-model.md
 - specs/002-ai-chatbot/quickstart.md
 - specs/002-ai-chatbot/contracts/chat-api.yaml
 - specs/002-ai-chatbot/contracts/mcp-tools-contract.md
tests:
---

## Prompt

Phase III: Todo AI Chatbot
1. System Architecture

Extend the existing Todo full-stack application by adding an AI chatbot layer.

Introduce a stateless chat API endpoint that orchestrates AI agents, MCP tools, and database persistence.

Maintain strict separation between frontend UI, backend API, AI logic, and MCP tool execution.

2. Frontend (Chat Interface)

Embed an OpenAI ChatKit-based conversational UI into the existing frontend.

Send user messages to a single chat API endpoint.

Display assistant responses, confirmations, and errors in conversational format.

Attach JWT token to every chat request for user identification.

3. Backend (Chat Orchestration)

Add a POST /api/{user_id}/chat endpoint in FastAPI.

Validate JWT token and enforce user isolation.

Fetch conversation history and messages from the database per request.

Persist all user and assistant messages.

Remain fully stateless across requests.

4. AI Agent Execution

Use OpenAI Agents SDK to process user messages.

Construct agent input using stored conversation history plus the new user message.

Allow the agent to decide whether to respond directly or invoke MCP tools.

Ensure all task-related decisions are delegated to the agent.

5. MCP Server & Tools

Implement a dedicated MCP server using the official MCP SDK.

Expose task operations as MCP tools:

add_task

list_tasks

update_task

complete_task

delete_task

MCP tools must:

Accept user_id explicitly

Perform database operations via ORM

Return structured, deterministic results

Store no in-memory state

6. Database Layer

Extend schema to include:

conversations (chat sessions)

messages (conversation history)

Persist all task changes, conversations, and messages in Neon PostgreSQL.

Enforce task ownership at query level.

7. Conversation Lifecycle

Receive user message

Load prior conversation state from database

Store user message

Run AI agent with MCP tools enabled

Execute MCP tool calls if requested by agent

Store assistant response and tool call metadata

Return response to frontend

8. Error Handling & Validation

Handle invalid tokens with 401 responses.

Gracefully manage missing tasks, invalid inputs, and tool failures.

Ensure assistant responses clearly communicate failures or confirmations.

9. Security & Scalability

Require JWT authentication for all chat requests.

Share JWT secret between frontend and backend via environment variables.

Design for horizontal scalability with no server-side session state.

10. Deployment Considerations

Ensure ChatKit domain allowlist is configured for production URLs.

Support local development without domain restrictions.

Keep configuration driven by environment variables.

## Response snapshot

Completed the implementation planning for the Todo AI Chatbot (Phase III) feature. The plan includes:

- Comprehensive technical context with language, dependencies, and constraints
- Constitution check ensuring all principles are satisfied
- Detailed project structure separating backend, frontend, and MCP server
- Research document resolving all technology decisions
- Data model defining Task, Conversation, and Message entities
- Quickstart guide with setup instructions and API endpoints
- API contracts for chat endpoint and MCP tools in YAML and Markdown formats
- Agent context updated with new technologies for the feature

All required artifacts have been created and the plan aligns with the constitution requirements for AI decision-making, MCP tool determinism, and conversation state recovery.

## Outcome

- ✅ Impact: Complete implementation plan with all required artifacts
- 🧪 Tests: No tests needed for planning phase
- 📁 Files: Created multiple docs in specs/002-ai-chatbot/ directory
- 🔁 Next prompts: Proceed with task breakdown based on this plan
- 🧠 Reflection: Plan comprehensively covers all requirements with proper separation of concerns

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task breakdown phase