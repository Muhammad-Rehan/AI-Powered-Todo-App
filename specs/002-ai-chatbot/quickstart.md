# Quickstart Guide: Todo AI Chatbot (Phase III)

## Prerequisites

- Python 3.11+
- Node.js 18+ (for frontend)
- PostgreSQL-compatible database (Neon recommended)
- OpenAI API key
- MCP SDK

## Setup Instructions

### 1. Environment Configuration

Create `.env` files for backend and MCP server:

**Backend (.env)**:
```bash
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
JWT_SECRET=your_jwt_secret_key
JWT_ALGORITHM=HS256
```

**MCP Server (.env)**:
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
JWT_SECRET=your_jwt_secret_key
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install fastapi uvicorn openai python-jose[cryptography] sqlalchemy psycopg2-binary

# Run database migrations
python -m src.utils.database migrate

# Start the backend server
uvicorn src.api.main:app --reload
```

### 3. MCP Server Setup

```bash
# Navigate to MCP server directory
cd mcp-server

# Install dependencies
pip install openai mcp

# Start the MCP server
python -m src.server
```

### 4. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

## API Endpoints

### Chat Endpoint
```
POST /api/{user_id}/chat
Authorization: Bearer {jwt_token}
Content-Type: application/json

{
  "message": "Add a task to buy groceries",
  "conversation_id": "optional_existing_conversation_id"
}

Response:
{
  "response": "I've added the task 'buy groceries' for you.",
  "conversation_id": "new_or_existing_conversation_id",
  "tool_calls": [...]
}
```

## Running Tests

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Development Workflow

1. Make changes to the codebase
2. Run relevant tests
3. Update documentation if needed
4. Commit with descriptive messages
5. Create pull request for review

## Troubleshooting

- **JWT Token Issues**: Verify JWT_SECRET matches between frontend and backend
- **Database Connection**: Check DATABASE_URL is correctly configured
- **MCP Server Not Responding**: Ensure MCP server is running and accessible
- **AI Agent Not Responding**: Verify OpenAI API key is valid and has sufficient quota