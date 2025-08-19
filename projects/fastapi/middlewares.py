from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time

class ResponseTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await super().dispatch(request, call_next)
        duration_ms = (time.time() - start_time) * 1000
        print(f"Request duration: {duration_ms} milliseconds")
        response.headers["X-Request-Duration"] = f"{duration_ms:.1f}"
        return response