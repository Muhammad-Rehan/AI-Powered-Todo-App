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

print("Verifying New Configuration Settings:")
print("=" * 50)
print(f"use_openrouter: {settings.use_openrouter}")
print(f"openrouter_base_url: {settings.openrouter_base_url}")
print(f"openrouter_model: {settings.openrouter_model}")
print(f"openai_api_key (first 10 chars): {settings.openai_api_key[:10] if settings.openai_api_key else 'N/A'}")
print("=" * 50)

# Check if the values match what we expect
expected_model = "qwen/qwen3-next-80b-a3b-instruct:free"
expected_api_key_prefix = "sk-or-v1-8e5d"

if settings.openrouter_model == expected_model:
    print(f"✅ Model correctly set to: {settings.openrouter_model}")
else:
    print(f"❌ Model mismatch! Expected: {expected_model}, Got: {settings.openrouter_model}")

if settings.openai_api_key.startswith(expected_api_key_prefix):
    print(f"✅ API key correctly starts with: {expected_api_key_prefix}")
else:
    print(f"❌ API key mismatch! Expected to start with: {expected_api_key_prefix}")

print("=" * 50)
print("Configuration verification complete.")