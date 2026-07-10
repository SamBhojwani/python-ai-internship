"""
main.py
-------
FastAPI application setup and configuration.

Run:
    uvicorn app.main:app --reload
"""

import time
from fastapi import FastAPI, Request
from app.database import engine, Base
from app.routes import router
from app.config import APP_NAME
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    description="Employee API with JWT authentication, SQLite persistence, and structured logging.",
    version="5.0.0",
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log every incoming request with method, path, status code and execution time."""
    start_time = time.time()
    response = await call_next(request)
    duration = round((time.time() - start_time) * 1000, 2)
    logger.info(f"{request.method} {request.url.path} - Status: {response.status_code} - {duration}ms")
    return response


app.include_router(router)

logger.info(f"{APP_NAME} started successfully")


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint."""
    return {
        "message": f"Welcome to the {APP_NAME}",
        "docs": "http://localhost:8000/docs",
    }