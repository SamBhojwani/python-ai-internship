"""
responses.py
------------
Standard API response format for all endpoints.
"""

from typing import Any, Optional


def success_response(message: str, data: Any = None) -> dict:
    """Return a standardized success response."""
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message: str, errors: Optional[list] = None) -> dict:
    """Return a standardized error response."""
    return {
        "success": False,
        "message": message,
        "errors": errors or []
    }