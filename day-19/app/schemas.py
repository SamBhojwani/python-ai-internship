"""
schemas.py
----------
Pydantic schemas for User and Employee request/response validation.
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# User Schemas

class UserRegister(BaseModel):
    """Schema for registering a new user."""
    username: str = Field(..., min_length=3, description="Username")
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=6, description="Password")
    role: Optional[str] = "Employee"

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "samarth",
                "email": "samarth@example.com",
                "password": "secret123",
                "role": "Admin"
            }
        }
    }


class UserLogin(BaseModel):
    """Schema for logging in."""
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "samarth",
                "password": "secret123"
            }
        }
    }


class UserResponse(BaseModel):
    """Schema for user response."""
    id: int
    username: str
    email: str
    role: str

    model_config = {
        "from_attributes": True
    }


# Employee Schemas

class EmployeeCreate(BaseModel):
    """Schema for creating a new employee."""
    name: str = Field(..., min_length=1)
    email: EmailStr = Field(..., description="Valid email address")
    department: str = Field(..., min_length=1)
    salary: float = Field(..., gt=0)

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