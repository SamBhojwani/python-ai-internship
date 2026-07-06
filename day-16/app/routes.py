"""
routes.py
---------
API endpoint definitions for the Employee API.
Routes handle HTTP only - all logic is in services.py.
"""

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import Optional
from app.schemas import EmployeeCreate, EmployeeUpdate
from app.responses import success_response, error_response
import app.services as services

router = APIRouter()


# Employee Endpoints

@router.get(
    "/employees",
    summary="Get all employees",
    tags=["Employees"],
)
def get_all_employees():
    """Return a list of all employees."""
    data = services.get_all_employees()
    return success_response("Employees retrieved successfully", data)


@router.get(
    "/employees/search",
    summary="Search employees by name",
    tags=["Employees"],
)
def search_employees(name: str):
    """Search employees by name."""
    data = services.search_employees_by_name(name)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No employees found with name containing: {name}"
        )
    return success_response("Employees retrieved successfully", data)


@router.get(
    "/employees/filter",
    summary="Filter employees by department",
    tags=["Employees"],
)
def filter_employees(department: str):
    """Filter employees by department."""
    data = services.filter_employees_by_department(department)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No employees found in department: {department}"
        )
    return success_response("Employees retrieved successfully", data)


@router.get(
    "/employees/{employee_id}",
    summary="Get employee by ID",
    tags=["Employees"],
)
def get_employee(employee_id: str):
    """Return a single employee by ID."""
    data = services.get_employee_by_id(employee_id)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found."
        )
    return success_response("Employee retrieved successfully", data)


@router.post(
    "/employees",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new employee",
    tags=["Employees"],
)
def create_employee(employee: EmployeeCreate):
    """Create a new employee record."""
    data = services.create_employee(employee)
    return success_response("Employee created successfully", data)


@router.put(
    "/employees/{employee_id}",
    summary="Update an employee",
    tags=["Employees"],
)
def update_employee(employee_id: str, updates: EmployeeUpdate):
    """Update an existing employee record."""
    data = services.update_employee(employee_id, updates)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found."
        )
    return success_response("Employee updated successfully", data)


@router.delete(
    "/employees/{employee_id}",
    summary="Delete an employee",
    tags=["Employees"],
)
def delete_employee(employee_id: str):
    """Delete an employee record by ID."""
    deleted = services.delete_employee(employee_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found."
        )
    return success_response("Employee deleted successfully")


# Health Check

@router.get(
    "/health",
    summary="Health check",
    tags=["Health"],
)
def health_check():
    """Check if the API is running."""
    return success_response("API is running", {
        "status": "UP",
        "application": "Employee API",
        "version": "1.0.0"
    })