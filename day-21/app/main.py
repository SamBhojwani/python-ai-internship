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
from app.routes.auth_routes import router as auth_router
from app.routes.employee_routes import router as employee_router
from app.config import APP_NAME
from app.logger import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    description="Production-ready Employee Management REST API with JWT authentication, SQLite persistence, structured logging and Docker deployment.",
    version="1.0.0",
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log every incoming request with method, path, status code and execution time."""
    start_time = time.time()
    response = await call_next(request)
    duration = round((time.time() - start_time) * 1000, 2)
    logger.info(f"{request.method} {request.url.path} - Status: {response.status_code} - {duration}ms")
    return response


app.include_router(auth_router)
app.include_router(employee_router)

logger.info(f"{APP_NAME} started successfully")


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint."""
    return {
        "message": f"Welcome to the {APP_NAME}",
        "docs": "http://localhost:8000/docs",
    }