import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Get the database URL
DATABASE_URL = os.getenv("DATABASE_URL")
NEON_DATABASE_URL = os.getenv("NEON_DATABASE_URL")


# Use DATABASE_URL if available, otherwise fall back to NEON_DATABASE_URL
if DATABASE_URL:
    url_to_test = DATABASE_URL
elif NEON_DATABASE_URL:
    url_to_test = NEON_DATABASE_URL
else:
    exit(1)


try:
    # Create engine
    engine = create_engine(
        url_to_test,
        echo=True,  # This will show SQL commands for debugging
        pool_size=1,
        max_overflow=0,
        connect_args={
            "connect_timeout": 10,
        }
    )

    # Test the connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1;"))

except OperationalError as e:
    pass

except Exception as e:
    pass