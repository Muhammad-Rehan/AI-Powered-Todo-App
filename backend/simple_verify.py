#!/usr/bin/env python3
"""
Simple verification of environment variables.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print("Checking Environment Variables Directly:")
print("=" * 50)
print(f"USE_OPENROUTER: {os.getenv('USE_OPENROUTER')}")
print(f"OPENROUTER_BASE_URL: {os.getenv('OPENROUTER_BASE_URL')}")
print(f"OPENROUTER_MODEL: {os.getenv('OPENROUTER_MODEL')}")
print(f"OPENAI_API_KEY (first 10 chars): {os.getenv('OPENAI_API_KEY', '')[:10]}")
print("=" * 50)

expected_model = "qwen/qwen3-next-80b-a3b-instruct:free"
expected_api_key_prefix = "sk-or-v1-8e5d"

actual_model = os.getenv('OPENROUTER_MODEL')
actual_api_key = os.getenv('OPENAI_API_KEY')

if actual_model == expected_model:
    print(f"[OK] Model correctly set to: {actual_model}")
else:
    print(f"[ERROR] Model mismatch! Expected: {expected_model}, Got: {actual_model}")

if actual_api_key and actual_api_key.startswith(expected_api_key_prefix):
    print(f"[OK] API key correctly starts with: {expected_api_key_prefix}")
else:
    print(f"[ERROR] API key mismatch! Expected to start with: {expected_api_key_prefix}")

print("=" * 50)
print("Environment variable check complete.")