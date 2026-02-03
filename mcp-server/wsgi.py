# mcp-server/wsgi.py
# Entry point for Vercel deployment

import sys
import os
from pathlib import Path

# Add the mcp-server directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from src.server_app import app_instance

# Vercel will look for the 'app' variable
app = app_instance