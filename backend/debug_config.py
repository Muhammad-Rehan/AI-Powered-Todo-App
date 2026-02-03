#!/usr/bin/env python3
"""
Debug script to check current configuration settings.
"""

import sys
from pathlib import Path

# Add the backend src directory to the path so we can import modules
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import settings


# Test creating an AI service to see what base URL it uses
from src.services.ai_agent_service import AIAssistantService

try:
    ai_service = AIAssistantService()
except Exception as e:
    pass