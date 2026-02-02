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

print("Current Configuration Settings:")
print("=" * 40)
print(f"use_openrouter: {settings.use_openrouter}")
print(f"openrouter_base_url: {settings.openrouter_base_url}")
print(f"openrouter_model: {settings.openrouter_model}")
print(f"openai_api_key set: {'Yes' if settings.openai_api_key else 'No'}")
print(f"openai_api_key (first 10 chars): {settings.openai_api_key[:10] if settings.openai_api_key else 'N/A'}")
print("=" * 40)

# Test creating an AI service to see what base URL it uses
from src.services.ai_agent_service import AIAssistantService

try:
    ai_service = AIAssistantService()
    print(f"AI Service initialized with base URL: {ai_service.openai_client.base_url}")
    print(f"AI Service model: {ai_service.model}")
    print(f"OpenRouter mode active: {settings.use_openrouter}")
except Exception as e:
    print(f"Error initializing AI service: {e}")