from fastapi import FastAPI, Request, Response, BackgroundTasks
import asyncio
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class ResponseTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response: Response = await call_next(request)
        duration_ms = (time.time() - start_time) * 1000
        print(f"Request duration: {duration_ms} milliseconds")
        response.headers["X-Request-Duration"] = f"{duration_ms:.1f}"
        return response

def send_email(email: str, message: str):
    # Simulate sending an email
    time.sleep(5)
    print(f"Email sent to {email} with message: {message}")

app = FastAPI()

app.add_middleware(ResponseTimeMiddleware)

@app.get(
    "/multiple-tasks",
    summary="Handle multiple tasks concurrently",
)
async def multiple_tasks() -> Response:
    return {
        "message": "Handling multiple tasks concurrently"
    }

@app.post(
    "/send-notification"
)
async def send_notification(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    return {"message": "Notification sent in the background"}
