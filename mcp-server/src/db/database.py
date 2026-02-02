from sqlmodel import create_engine, Session
from typing import Generator
import os


# Database configuration - using the same as backend
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_mfqNW7JHD6an@ep-rough-base-a4yps7fz-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require")


# Create the database engine
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)


def get_session() -> Generator[Session, None, None]:
    """
    Dependency to get a database session for the MCP server.

    Yields:
        Database session
    """
    with Session(engine) as session:
        yield session