"""
main.py
-------
FastAPI application setup and configuration.

Run:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
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

app.include_router(router)

logger.info(f"{APP_NAME} started successfully")


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint."""
    return {
        "message": f"Welcome to the {APP_NAME}",
        "docs": "http://localhost:8000/docs",
    }