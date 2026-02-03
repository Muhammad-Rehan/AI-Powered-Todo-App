# MCP Server Deployment on Vercel

This MCP (Model Context Protocol) Server provides AI tools for task management in the Todo application.

## Deployment Configuration

The MCP server is configured for deployment on Vercel using:

- **Framework**: FastAPI
- **Runtime**: Python 3.9
- **Adapter**: Mangum (to make FastAPI compatible with Vercel's serverless functions)

## Endpoints

Once deployed, the MCP server will provide these endpoints:

- `GET /` - Root endpoint with server info
- `GET /health` - Health check endpoint
- `POST /add_task` - Add a new task
- `POST /list_tasks` - List all tasks for a user
- `POST /update_task` - Update an existing task
- `POST /delete_task` - Delete a task
- `POST /complete_task` - Mark a task as completed

## Configuration

The server will be deployed at: `https://your-vercel-project-url.vercel.app`

## Environment Variables

The MCP server may require the following environment variables:

- `DATABASE_URL` - Connection string for the PostgreSQL database
- `MCP_PORT` - Port number (defaults to 8001 for local development)

## Troubleshooting

If you encounter a 404 error after deployment:
1. Check that the `vercel.json` is properly configured
2. Ensure all dependencies are listed in `requirements.txt`
3. Verify that the Mangum adapter is properly handling the FastAPI app