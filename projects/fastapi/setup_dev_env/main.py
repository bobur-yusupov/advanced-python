from fastapi import FastAPI

from models import User
from middleware import ResponseTimeMiddleware

app=FastAPI()

app.add_middleware(ResponseTimeMiddleware)

@app.get("/")
async def read_root():
    return {
        "message": "Hello, World!"
    }

@app.post("/create")
async def create_user(user: User):
    return {
        "message": "User created successfully!",
        "user": user
    }
