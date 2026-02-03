# mcp-server/api_handler.py
# Vercel-compatible handler for FastAPI application

import asyncio
from fastapi import FastAPI
from mangum import Mangum
import sys
import os
from pathlib import Path

# Add the mcp-server directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from src.server_app import app_instance

# Create a Mangum adapter to convert FastAPI app to ASGI handler
handler = Mangum(app_instance)

# For Vercel, we'll also define the default handler
def app(event, context):
    return handler(event, context)