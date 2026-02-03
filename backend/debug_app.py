#!/usr/bin/env python3
"""Debug script to test app creation"""

try:
    from api.auth import router as auth_router
    from api.tasks import router as tasks_router
    from src.api.chat_endpoints import router as chat_router
    from api.index import create_app
    app = create_app()

except Exception as e:
    pass