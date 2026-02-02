# Data Model: Todo AI Chatbot (Phase III)

## Entity Definitions

### Task
**Description**: Represents a user's todo item
**Fields**:
- id (UUID/string): Unique identifier for the task
- user_id (UUID/string): Foreign key linking to the user who owns this task
- title (string): Brief title/description of the task
- description (string, optional): Detailed description of the task
- completed (boolean): Status indicating if the task is completed
- created_at (timestamp): Time when the task was created
- updated_at (timestamp): Time when the task was last updated

**Validation rules**:
- user_id must reference a valid user
- title must not be empty
- completed defaults to false

**State transitions**:
- Active → Completed (when task is marked as done)
- Completed → Active (when task is reopened)

### Conversation
**Description**: Represents a chat session containing a sequence of messages
**Fields**:
- id (UUID/string): Unique identifier for the conversation
- user_id (UUID/string): Foreign key linking to the user who owns this conversation
- title (string, optional): Generated or user-provided title for the conversation
- created_at (timestamp): Time when the conversation was started
- updated_at (timestamp): Time when the conversation was last updated

**Validation rules**:
- user_id must reference a valid user
- Each user can have multiple conversations

### Message
**Description**: Represents individual chat messages within a conversation
**Fields**:
- id (UUID/string): Unique identifier for the message
- conversation_id (UUID/string): Foreign key linking to the conversation
- user_id (UUID/string): Foreign key linking to the user who sent this message
- role (enum: 'user'|'assistant'): Indicates whether the message is from user or AI assistant
- content (string): The actual text content of the message
- tool_calls (JSON, optional): Metadata about any MCP tools called during this interaction
- created_at (timestamp): Time when the message was created

**Validation rules**:
- conversation_id must reference a valid conversation
- user_id must match the conversation owner
- role must be either 'user' or 'assistant'

## Relationships

- **User → Task**: One-to-many (one user can have many tasks)
- **User → Conversation**: One-to-many (one user can have many conversations)
- **Conversation → Message**: One-to-many (one conversation contains many messages)

## Constraints

- All entities must enforce user isolation: users can only access their own tasks and conversations
- All timestamps should be stored in UTC
- Foreign key constraints must be enforced at the database level
- Soft deletes should be implemented where needed to maintain conversation history