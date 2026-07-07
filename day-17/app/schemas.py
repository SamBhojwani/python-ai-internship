"""
schemas.py
----------
Pydantic schemas for request validation and response serialization.
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class EmployeeCreate(BaseModel):
    """Schema for creating a new employee."""
    name: str = Field(..., min_length=1, description="Full name of the employee")
    email: EmailStr = Field(..., description="Valid email address")
    department: str = Field(..., min_length=1, description="Department name")
    salary: float = Field(..., gt=0, description="Salary must be greater than 0")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Aman Sharma",
                "email": "aman@example.com",
                "department": "Engineering",
                "salary": 90000
            }
        }
    }


class EmployeeUpdate(BaseModel):
    """Schema for updating an employee - all fields optional."""
    name: Optional[str] = Field(None, min_length=1)
    email: Optional[EmailStr] = None
    department: Optional[str] = Field(None, min_length=1)
    salary: Optional[float] = Field(None, gt=0)


class EmployeeResponse(BaseModel):
    """Schema for employee API response."""
    id: int
    employee_id: str
    name: str
    department: str
    salary: float
    email: str

    model_config = {
        "from_attributes": True
    }