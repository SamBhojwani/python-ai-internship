"""
schemas.py
----------
Pydantic schemas for request validation and response serialization.
"""

from pydantic import BaseModel
from typing import Optional


class EmployeeCreate(BaseModel):
    """Schema for creating a new employee - used in POST requests."""
    name: str
    department: str
    salary: float
    email: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Aman Sharma",
                "department": "Engineering",
                "salary": 90000,
                "email": "aman@example.com"
            }
        }
    }


class EmployeeUpdate(BaseModel):
    """Schema for updating an employee - all fields optional for PUT requests."""
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    email: Optional[str] = None


class EmployeeResponse(BaseModel):
    """Schema for employee API response - includes ID."""
    employee_id: str
    name: str
    department: str
    salary: float
    email: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "employee_id": "E001",
                "name": "Aman Sharma",
                "department": "Engineering",
                "salary": 90000,
                "email": "aman@example.com"
            }
        }
    }