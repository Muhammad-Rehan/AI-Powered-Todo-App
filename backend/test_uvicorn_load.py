#!/usr/bin/env python3
"""Test script that mimics uvicorn loading"""

import sys
import os

# Add the parent directory to the Python path (similar to what's in the api files)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    # Import the app exactly as uvicorn would
    from api.index import app

    auth_routes_found = False
    for route in app.routes:
        if hasattr(route, 'methods') and hasattr(route, 'path'):
            if 'auth' in route.path.lower():
                auth_routes_found = True

except Exception as e:
    pass