# Todo AI Chatbot (Phase III)

An AI-powered chatbot that allows authenticated users to manage their todo tasks using natural language through a single chat endpoint. The system uses OpenAI Agents SDK to interpret user intent and execute task operations exclusively through MCP (Model Context Protocol) tools, with all conversation history and task data persisted in the database.

## Features

- AI-powered natural language task management (add, list, update, delete, complete tasks)
- User authentication and registration with JWT tokens
- Persistent conversation history with context preservation
- Secure access control (users can only access their own tasks and conversations)
- MCP (Model Context Protocol) integration for safe task operations
- Real-time chat interface with responsive design
- RESTful API with proper error handling
- PostgreSQL database with Neon Serverless support

## Tech Stack

- **Frontend**: Next.js 14+ with App Router, React-based chat interface
- **Backend**: FastAPI with Python 3.11+, OpenAI Agents SDK integration
- **MCP Server**: Dedicated server for exposing safe tools to AI agents
- **Database**: PostgreSQL with SQLModel ORM
- **Authentication**: JWT-based with custom middleware
- **AI Integration**: OpenAI GPT models with function calling
- **Deployment**: GitHub Pages (via GitHub Actions) or modern cloud platforms

## Project Structure

```
├── backend/                       # FastAPI backend with AI integration
│   ├── src/
│   │   ├── models/               # SQLModel database models (tasks, conversations, messages)
│   │   ├── services/             # Business logic services (AI agent, chat, auth)
│   │   ├── api/                  # API route definitions (chat endpoints)
│   │   ├── middleware/           # Error handling and other middleware
│   │   └── utils/                # Utility functions (database, etc.)
│   ├── requirements.txt
│   └── alembic/                  # Database migrations
├── mcp-server/                   # Model Context Protocol server for task operations
│   ├── src/
│   │   ├── tools/                # Task management tools (add, list, update, delete, complete)
│   │   ├── models/               # Database models for MCP server
│   │   ├── db/                   # Database utilities for MCP server
│   │   └── server_app.py         # FastAPI wrapper for MCP server
│   └── requirements.txt
├── frontend/                     # Next.js frontend with chat interface
│   ├── src/
│   │   ├── components/           # React components (ChatInterface)
│   │   ├── services/             # API client utilities
│   │   └── utils/                # Authentication utilities
│   └── package.json
├── specs/002-ai-chatbot/         # Feature specifications for Phase III
├── .env                          # Environment variables
├── .gitignore                    # Git ignore rules
├── pyproject.toml                # Python project configuration
└── package.json                  # Root monorepo configuration
```

## Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL (or Neon Serverless account)
- OpenAI API Key (for AI chatbot functionality)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
JWT_SECRET_KEY=your-super-secret-jwt-key-change-in-production
OPENAI_API_KEY=your_openai_api_key_here
MCP_SERVER_URL=http://localhost:8001
```

4. Run the application:
```bash
python -m uvicorn src.main:app --reload
```

### MCP Server Setup (Required for AI Chatbot)

1. Navigate to the MCP server directory:
```bash
cd mcp-server
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the MCP server:
```bash
python -m uvicorn src.server_app:app --port 8001 --reload
```


### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

## API Endpoints

### Chat API

- `POST /api/{user_id}/chat` - Send a message to the AI chatbot
- `GET /api/{user_id}/conversations` - Get all conversations for a user
- `GET /api/{user_id}/conversations/{conversation_id}` - Get messages in a specific conversation

### Legacy Task API (still available)

- `GET /api/tasks` - Get all tasks for authenticated user
- `POST /api/tasks` - Create a new task for authenticated user
- `GET /api/tasks/{task_id}` - Get a specific task by ID
- `PUT /api/tasks/{task_id}` - Update a specific task by ID
- `DELETE /api/tasks/{task_id}` - Delete a specific task by ID
- `PATCH /api/tasks/{task_id}/toggle` - Toggle completion status of a task

### Authentication

- `POST /api/auth/signup` - Create a new user account
- `POST /api/auth/signin` - Authenticate user and return JWT token

## Environment Variables

The application uses the following environment variables:

### Backend Variables
- `DATABASE_URL` - PostgreSQL database connection string
- `JWT_SECRET_KEY` - Secret key for JWT token signing
- `JWT_ALGORITHM` - Algorithm for JWT token signing (default: HS256)
- `JWT_ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time in minutes
- `OPENAI_API_KEY` - API key for OpenAI services (or OpenRouter if using OpenRouter)
- `MCP_SERVER_URL` - URL for the MCP server (default: http://localhost:8001)
- `OPENROUTER_BASE_URL` - Base URL for OpenRouter API (default: https://openrouter.ai/api/v1)
- `OPENROUTER_MODEL` - Model to use with OpenRouter (default: google/gemini-2.0-flash-exp:free)
- `USE_OPENROUTER` - Flag to use OpenRouter instead of OpenAI (default: false)

### MCP Server Variables
- `DATABASE_URL` - PostgreSQL database connection string (same as backend)
- `JWT_SECRET_KEY` - Secret key for JWT token verification (same as backend)
- `MCP_PORT` - Port for MCP server (default: 8001)

### Frontend Variables
- `NEXT_PUBLIC_API_BASE_URL` - Base URL for backend API calls (e.g., http://localhost:8000)

## Database Migrations

This project uses Alembic for database migrations:

1. To create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

2. To apply migrations:
```bash
alembic upgrade head
```

## Testing

Run backend tests with pytest:
```bash
cd backend
python -m pytest
```

## Security

- All API endpoints require valid JWT authentication tokens
- Users can only access their own tasks
- Passwords are securely hashed using bcrypt
- Input validation is performed on all endpoints

## Development

This project follows the Spec-Driven Development approach with specifications in the `specs/` directory. All development should align with the defined specifications, plans, and tasks.

## Deployment

### GitHub Pages Deployment

This project is configured to automatically deploy to GitHub Pages when changes are pushed to the main branch. The deployment is handled by the GitHub Actions workflow defined in `.github/workflows/github-pages.yml`.

### Manual Deployment

To build and export the frontend manually for static hosting:

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Build and export the static site:
```bash
npm run export
```

The built site will be available in the `out/` directory.

### Backend Deployment

The backend FastAPI application can be deployed to any cloud platform that supports Python applications (e.g., Heroku, Railway, AWS, GCP, etc.). You'll need to configure environment variables for database connection and JWT secrets.

## Running the Complete Application

To run the full application with AI chatbot functionality:

1. Start the MCP server (port 8001):
```bash
cd mcp-server && python -m uvicorn src.server_app:app --port 8001 --reload
```

2. Start the main backend server (port 8000):
```bash
cd backend && python -m uvicorn src.main:app --reload
```

3. Start the frontend (port 3000):
```bash
cd frontend && npm run dev
```

4. Visit `http://localhost:3000` in your browser to access the application.

The AI Chatbot will be accessible from:
- The main page via the "Try AI Chat" button
- The dashboard via the "AI Chat Assistant" button
- Directly at `/chat` route when logged in