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

    # Check that the new settings exist
    assert hasattr(settings, 'openrouter_base_url'), "Missing openrouter_base_url setting"
    assert hasattr(settings, 'openrouter_model'), "Missing openrouter_model setting"
    assert hasattr(settings, 'use_openrouter'), "Missing use_openrouter setting"

    return True


def test_ai_service_initialization():
    """Test that AIAssistantService initializes correctly with the new configuration."""

    # Enable OpenRouter mode temporarily for this test
    original_value = settings.use_openrouter
    settings.__dict__['use_openrouter'] = True  # Temporarily set for testing

    try:
        ai_service = AIAssistantService()

        # Restore original value
        settings.__dict__['use_openrouter'] = original_value

        return True
    except Exception as e:
        # Restore original value
        settings.__dict__['use_openrouter'] = original_value
        return False


def test_openai_client_with_openrouter():
    """Test that OpenAI client can be configured with OpenRouter settings."""

    from openai import OpenAI

    # Test creating a client with OpenRouter base URL
    try:
        client = OpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openrouter_base_url
        )

        return True
    except Exception as e:
        return False


def main():
    """Run all tests."""

    all_passed = True

    # Test configuration loading
    try:
        all_passed &= test_configuration()
    except Exception as e:
        all_passed = False

    # Test AI service initialization
    try:
        all_passed &= test_ai_service_initialization()
    except Exception as e:
        all_passed = False

    # Test OpenAI client with OpenRouter
    try:
        all_passed &= test_openai_client_with_openrouter()
    except Exception as e:
        all_passed = False

    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)