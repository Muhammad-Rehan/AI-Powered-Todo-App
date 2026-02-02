# OpenRouter Configuration Changes

## Files Modified:

1. **backend/config.py**:
   - Added new configuration options for OpenRouter:
     - `openrouter_base_url`: Default "https://openrouter.ai/api/v1"
     - `openrouter_model`: Default "google/gemini-2.0-flash-exp:free"
     - `use_openrouter`: Boolean flag to switch between OpenAI and OpenRouter (default: False)

2. **backend/src/services/ai_agent_service.py**:
   - Updated initialization to conditionally configure OpenAI client based on `use_openrouter` setting
   - When `use_openrouter` is True, the client is initialized with the custom base URL
   - Made the model configurable instead of hardcoded to "gpt-3.5-turbo"

3. **backend/requirements.txt**:
   - Updated openai library requirement from 1.3.5 to >=1.10.0 to ensure proper support for custom base URLs

4. **.env**:
   - Added OpenRouter configuration variables:
     - `OPENAI_API_KEY`: Your OpenRouter API key
     - `OPENROUTER_BASE_URL`: https://openrouter.ai/api/v1
     - `OPENROUTER_MODEL`: google/gemini-2.0-flash-exp:free
     - `USE_OPENROUTER`: true to enable OpenRouter

5. **README.md**:
   - Added documentation for OpenRouter configuration in the Environment Variables section

## How to Use:

1. Replace the placeholder API key in your `.env` file with your actual OpenRouter API key
2. Set `USE_OPENROUTER=true` in your `.env` file
3. Restart the backend server
4. The AI chatbot will now use OpenRouter instead of OpenAI

## Testing:

A test script (`test_openrouter_config.py`) was created to verify that all configuration changes work correctly. The test confirmed that:
- Configuration loads properly
- AIAssistantService initializes correctly with OpenRouter settings
- OpenAI client can be configured with the custom OpenRouter base URL