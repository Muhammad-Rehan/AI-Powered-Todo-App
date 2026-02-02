#!/usr/bin/env python3
"""
Test script to verify OpenRouter configuration works correctly.
"""

import os
import sys
from pathlib import Path

# Add the backend src directory to the path so we can import modules
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import settings
from src.services.ai_agent_service import AIAssistantService


def test_configuration():
    """Test that the configuration is loaded correctly."""
    print("Testing configuration loading...")

    # Check that the new settings exist
    assert hasattr(settings, 'openrouter_base_url'), "Missing openrouter_base_url setting"
    assert hasattr(settings, 'openrouter_model'), "Missing openrouter_model setting"
    assert hasattr(settings, 'use_openrouter'), "Missing use_openrouter setting"

    print(f"[OK] OpenRouter base URL: {settings.openrouter_base_url}")
    print(f"[OK] OpenRouter model: {settings.openrouter_model}")
    print(f"[OK] Use OpenRouter flag: {settings.use_openrouter}")
    print(f"[OK] OpenAI API Key: {'SET' if settings.openai_api_key else 'NOT SET'}")

    return True


def test_ai_service_initialization():
    """Test that AIAssistantService initializes correctly with the new configuration."""
    print("\nTesting AI Assistant Service initialization...")

    # Enable OpenRouter mode temporarily for this test
    original_value = settings.use_openrouter
    settings.__dict__['use_openrouter'] = True  # Temporarily set for testing

    try:
        ai_service = AIAssistantService()

        print(f"[OK] OpenAI client initialized with base URL: {ai_service.openai_client.base_url}")
        print(f"[OK] Model configured: {ai_service.model}")
        print(f"[OK] OpenRouter mode: {settings.use_openrouter}")

        # Restore original value
        settings.__dict__['use_openrouter'] = original_value

        return True
    except Exception as e:
        print(f"[ERROR] Error initializing AI Assistant Service: {e}")
        # Restore original value
        settings.__dict__['use_openrouter'] = original_value
        return False


def test_openai_client_with_openrouter():
    """Test that OpenAI client can be configured with OpenRouter settings."""
    print("\nTesting OpenAI client configuration with OpenRouter...")

    from openai import OpenAI

    # Test creating a client with OpenRouter base URL
    try:
        client = OpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openrouter_base_url
        )

        print(f"[OK] OpenAI client created with OpenRouter base URL: {client.base_url}")
        print(f"[OK] API key is {'set' if client.api_key else 'not set'}")

        return True
    except Exception as e:
        print(f"[ERROR] Error creating OpenAI client with OpenRouter: {e}")
        return False


def main():
    """Run all tests."""
    print("Testing OpenRouter Configuration\n")
    print("="*50)

    all_passed = True

    # Test configuration loading
    try:
        all_passed &= test_configuration()
    except Exception as e:
        print(f"[ERROR] Configuration test failed: {e}")
        all_passed = False

    # Test AI service initialization
    try:
        all_passed &= test_ai_service_initialization()
    except Exception as e:
        print(f"[ERROR] AI service test failed: {e}")
        all_passed = False

    # Test OpenAI client with OpenRouter
    try:
        all_passed &= test_openai_client_with_openrouter()
    except Exception as e:
        print(f"[ERROR] OpenAI client test failed: {e}")
        all_passed = False

    print("\n" + "="*50)
    if all_passed:
        print("[OK] All tests passed! OpenRouter configuration is working correctly.")
        print("\nTo use OpenRouter:")
        print("1. Set OPENAI_API_KEY to your OpenRouter API key in .env")
        print("2. Set USE_OPENROUTER=true in .env")
        print("3. Restart the backend server")
    else:
        print("[ERROR] Some tests failed. Please check the configuration.")

    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)