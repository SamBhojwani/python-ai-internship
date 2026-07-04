"""
main.py
-------
FastAPI application setup and configuration.

Run:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Employee API",
    description="A REST API for managing employee records built with FastAPI.",
    version="1.0.0",
)

app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the Employee API",
        "docs": "http://localhost:8000/docs",
        "health": "http://localhost:8000/health",
    }