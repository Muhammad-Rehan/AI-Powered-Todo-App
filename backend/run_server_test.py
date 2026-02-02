#!/usr/bin/env python3
"""Direct test to run the app with uvicorn-like configuration"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import and create the app
from api.index import create_app

app = create_app()

# Test if we can manually trigger the route registration
print("Testing route registration...")
for route in app.routes:
    if hasattr(route, 'methods') and hasattr(route, 'path'):
        if 'auth' in route.path:
            print(f"Found auth route: {route.methods} {route.path}")

# Now run with uvicorn programmatically
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)