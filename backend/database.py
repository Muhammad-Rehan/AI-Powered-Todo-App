# src/database.py
from sqlmodel import Session, SQLModel
from typing import Generator
from config import settings       # <-- changed to relative import for Vercel
import logging

logger = logging.getLogger(__name__)

# ---------------------------------
# Lazy Engine Creation for Serverless
# ---------------------------------
def get_engine():
    from sqlmodel import create_engine

    # Create engine only when needed (lazy initialization)
    engine = create_engine(
        settings.database_url,
        echo=True,
        # Use smaller pool sizes for serverless
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        pool_recycle=300,
        connect_args={
            "sslmode": "require",
            # Additional connection args for serverless
            "connect_timeout": 10,
        },
    )
    return engine


# ---------------------------------
# Session Dependency
# ---------------------------------
def get_session() -> Generator[Session, None, None]:
    engine = get_engine()
    with Session(engine) as session:
        yield session

# ---------------------------------
# Create Tables
# ---------------------------------
def create_db_and_tables() -> None:
    from src.models.user import User   # <-- relative import for Vercel
    from src.models.task import Task   # <-- relative import for Vercel
    from src.models.conversation import Conversation   # <-- Add Conversation model
    from src.models.message import Message   # <-- Add Message model

    logger.info("Creating database tables if not present...")
    engine = get_engine()
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables ready.")
