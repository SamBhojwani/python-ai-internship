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

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee API",
    description="A persistent Employee API using FastAPI and SQLite.",
    version="3.0.0",
)

app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the Employee API",
        "docs": "http://localhost:8000/docs",
    }