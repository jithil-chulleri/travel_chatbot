from fastapi import FastAPI
from app.routers import hello

app = FastAPI(title="Sample FastAPI App")

app.include_router(hello.router, prefix="/api")
