#!/usr/bin/env python3
"""
Verify the new configuration is loaded correctly.
"""

import os
import sys
from pathlib import Path

# Force reload of environment variables
os.environ.clear()
os.environ.update({key: value for key, value in os.environ.items()})

# Reload the environment from .env file
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

# Add the backend src directory to the path so we can import modules
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import settings

