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

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=APP_NAME,
    description="Employee API with JWT authentication and protected endpoints.",
    version="4.0.0",
)

app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint."""
    return {
        "message": f"Welcome to the {APP_NAME}",
        "docs": "http://localhost:8000/docs",
    }