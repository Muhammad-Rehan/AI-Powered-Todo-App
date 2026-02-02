#!/usr/bin/env python3
"""Test script that mimics uvicorn loading"""

import sys
import os

# Add the parent directory to the Python path (similar to what's in the api files)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

print("Testing app creation the same way uvicorn does...")

try:
    # Import the app exactly as uvicorn would
    from api.index import app

    print("[OK] App imported successfully from api.index")

    # Print registered routes
    print("\nRegistered routes:")
    auth_routes_found = False
    for route in app.routes:
        if hasattr(route, 'methods') and hasattr(route, 'path'):
            print(f"  {route.methods} {route.path}")
            if 'auth' in route.path.lower():
                auth_routes_found = True

    if auth_routes_found:
        print("\n[OK] Authentication routes found!")
    else:
        print("\n[WARNING] Authentication routes NOT found!")

except Exception as e:
    print(f"[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()