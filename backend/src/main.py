from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.chat_endpoints import router as chat_router
from .middleware.error_handler import add_error_handlers
import os


# Create FastAPI app instance
app = FastAPI(
    title="Todo AI Chatbot API",
    description="API for interacting with the AI-powered todo chatbot",
    version="1.0.0"
)


# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Add error handling middleware
add_error_handlers(app)


# Include chat API routes
app.include_router(chat_router)


@app.get("/")
def read_root():
    """
    Root endpoint for health check.
    """
    return {
        "message": "Todo AI Chatbot Backend API",
        "status": "healthy",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {
        "status": "healthy",
        "service": "todo-ai-chatbot-backend"
    }


# Additional configuration can be added here
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=True
    )