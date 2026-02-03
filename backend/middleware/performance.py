import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class PerformanceMonitoringMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # ✅ Do NOT touch CORS preflight requests
        if request.method == "OPTIONS":
            return await call_next(request)

        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time
        formatted_time = f"{process_time:.4f}s"


        # Add response header with processing time
        response.headers["X-Process-Time"] = formatted_time

        return response
