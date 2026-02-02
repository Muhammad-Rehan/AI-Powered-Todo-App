from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from fastapi.middleware.cors import CORSMiddleware
import logging
import sys
import os

# Add the current directory's parent to the Python path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from config import settings
from database import get_engine, create_db_and_tables
from api.auth import router as auth_router
from api.tasks import router as tasks_router
from src.api.chat_endpoints import router as chat_router
from middleware.performance import PerformanceMonitoringMiddleware

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Allowed CORS origins (NO paths)
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://muhammad-rehan.github.io",
]

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
    )

    # -------------------------------
    # CORS middleware (ONLY place CORS is handled)
    # -------------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # -------------------------------
    # Custom middleware
    # -------------------------------
    @app.middleware("http")
    async def log_requests(request, call_next):
        logger.info(f"Request path: {request.url.path}")
        response = await call_next(request)
        return response

    app.add_middleware(PerformanceMonitoringMiddleware)

    logger.info(f"CORS allowed origins: {ALLOWED_ORIGINS}")

    # -------------------------------
    # ✅ Global OPTIONS handler for preflight requests
    # -------------------------------
    from fastapi import Request
    from starlette.responses import Response

    @app.options("/{full_path:path}")
    async def preflight(full_path: str, request: Request):
        # Return proper CORS headers for preflight
        response = Response(status_code=200)
        origin = request.headers.get("origin")
        if origin and any(allowed_origin == origin or allowed_origin == "*" for allowed_origin in ALLOWED_ORIGINS):
            response.headers["Access-Control-Allow-Origin"] = origin
        else:
            # If origin is not in allowed list, use first allowed origin (or handle as needed)
            if ALLOWED_ORIGINS:
                response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGINS[0]

        response.headers["Access-Control-Allow-Credentials"] = "true"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, PATCH, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type, Set-Cookie"
        return response

    # -------------------------------
    # Routers
    # -------------------------------
    # CORRECT
    app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
    app.include_router(tasks_router, prefix="/api/tasks", tags=["Tasks"])
    app.include_router(chat_router, prefix="/api/v1", tags=["Chat"])  # Chat endpoints at /api/v1/{user_id}/chat, etc.


    # -------------------------------
    # Startup event
    # -------------------------------
    @app.on_event("startup")
    def on_startup():
        logger.info("Testing database connection...")
        try:
            engine = get_engine()
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            logger.info("Database connection successful.")
            create_db_and_tables()
            logger.info("Database tables ensured.")
        except OperationalError as e:
            logger.error("Database connection failed.")
            logger.error(str(e))
            raise RuntimeError(
                "Cannot connect to database. Check DATABASE_URL and credentials."
            ) from e

    # -------------------------------
    # Health check
    # -------------------------------
    @app.get("/")
    def health():
        return {"status": "ok", "service": settings.app_name}

    return app


# Required for Vercel
app = create_app()
