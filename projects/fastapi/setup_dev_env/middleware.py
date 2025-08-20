from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time

class ResponseTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response: Response = await call_next(request)
        process_time_ms = (time.time() - start_time) * 1000
        response.headers["X-Process-Time"] = f"{process_time_ms:.2f} ms"
        return response
