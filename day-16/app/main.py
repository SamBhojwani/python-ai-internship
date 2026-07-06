"""
main.py
-------
FastAPI application setup and configuration.

Run:
    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.routes import router
from app.exceptions import http_exception_handler, validation_exception_handler

app = FastAPI(
    title="Employee API",
    description="A REST API for managing employee records with request validation and standardized responses.",
    version="2.0.0",
)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(router)


@app.get("/", tags=["Root"])
def root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the Employee API",
        "docs": "http://localhost:8000/docs",
        "health": "http://localhost:8000/health",
    }