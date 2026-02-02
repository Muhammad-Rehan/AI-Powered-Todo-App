#!/usr/bin/env python3
"""Debug script to test app creation"""

print("Starting app creation debug...")

try:
    print("Importing modules...")
    from api.auth import router as auth_router
    print("[OK] Auth router imported")

    from api.tasks import router as tasks_router
    print("[OK] Tasks router imported")

    from src.api.chat_endpoints import router as chat_router
    print("[OK] Chat router imported")

    print("\nCreating app...")
    from api.index import create_app
    app = create_app()

    print("[OK] App created successfully!")

    # Print registered routes
    print("\nRegistered routes:")
    for route in app.routes:
        if hasattr(route, 'methods') and hasattr(route, 'path'):
            print(f"  {route.methods} {route.path}")

except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()