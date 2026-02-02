from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Callable, Awaitable
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ErrorHandlerMiddleware:
    """
    Middleware to handle errors globally in the application.
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        async def handle_error(request: Request):
            try:
                return await self.app(scope, receive, send)
            except HTTPException as e:
                # Log the HTTP exception
                logger.warning(f"HTTPException: {e.status_code} - {e.detail}")

                # Return JSON response for HTTP exceptions
                return JSONResponse(
                    status_code=e.status_code,
                    content={
                        "detail": e.detail,
                        "status_code": e.status_code
                    }
                )
            except Exception as e:
                # Log the general exception
                logger.error(f"Unhandled exception: {str(e)}", exc_info=True)

                # Return a generic error response
                return JSONResponse(
                    status_code=500,
                    content={
                        "detail": "An internal server error occurred",
                        "status_code": 500
                    }
                )

        # Create a request object to pass to the error handler
        request = Request(scope)
        return await handle_error(request)


def add_error_handlers(app):
    """
    Add error handlers to the FastAPI app.
    """
    # Add middleware
    app.add_middleware(ErrorHandlerMiddleware)

    # Add exception handlers
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        logger.warning(f"HTTPException: {exc.status_code} - {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
                "status_code": exc.status_code
            }
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        logger.error(f"General exception: {str(exc)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "detail": "An internal server error occurred",
                "status_code": 500
            }
        )