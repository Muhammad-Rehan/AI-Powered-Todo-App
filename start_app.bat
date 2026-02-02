@echo off
echo Starting Todo AI Chatbot Application...
echo.

REM Function to start MCP server in a new window
echo Starting MCP Server on port 8001...
start "MCP Server" cmd /k "cd /d %~dp0mcp-server && python -m uvicorn src.server_app:app --port 8001 --reload"

REM Wait a bit for MCP server to start
timeout /t 3 /nobreak >nul

REM Function to start backend in a new window
echo Starting Backend Server on port 8000...
start "Backend Server" cmd /k "cd /d %~dp0backend && python -m uvicorn src.main:app --reload"

REM Wait a bit for backend to start
timeout /t 3 /nobreak >nul

REM Function to start frontend in a new window
echo Starting Frontend on port 3000...
start "Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo All services started successfully!
echo MCP Server: http://localhost:8001
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Visit http://localhost:3000 to access the application.
pause