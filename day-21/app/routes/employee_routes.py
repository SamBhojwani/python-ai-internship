"""
employee_routes.py
------------------
Employee management endpoints.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.dependencies import get_current_user
from app.models import User
from app.services import employee_service
from typing import List

router = APIRouter(tags=["Employees"])


@router.get(
    "/employees",
    response_model=List[EmployeeResponse],
    summary="Get all employees",
    responses={200: {"description": "Returns paginated list of employees"}}
)
def get_all_employees(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    """Return all employees with pagination."""
    return employee_service.get_all_employees(db, page, size)


@router.get(
    "/employees/search",
    response_model=List[EmployeeResponse],
    summary="Search employees by name",
    responses={
        200: {"description": "Returns matching employees"},
        404: {"description": "No employees found"}
    }
)
def search_employees(name: str, db: Session = Depends(get_db)):
    """Search employees by name. Case-insensitive partial match."""
    employees = employee_service.search_employees_by_name(db, name)
    if not employees:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No employees found with name containing: {name}")
    return employees


@router.get(
    "/employees/department/{department}",
    response_model=List[EmployeeResponse],
    summary="Filter employees by department",
    responses={
        200: {"description": "Returns employees in the department"},
        404: {"description": "No employees found in department"}
    }
)
def get_employees_by_department(department: str, db: Session = Depends(get_db)):
    """Filter employees by department name. Case-insensitive matching."""
    employees = employee_service.get_employees_by_department(db, department)
    if not employees:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No employees found in department: {department}")
    return employees


@router.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    summary="Get employee by ID",
    responses={
        200: {"description": "Returns the employee"},
        404: {"description": "Employee not found"}
    }
)
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    """Return a single employee by their employee ID."""
    employee = employee_service.get_employee_by_id(db, employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new employee",
    responses={
        201: {"description": "Employee created successfully"},
        401: {"description": "Authentication required"}
    }
)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Create a new employee record. Requires authentication."""
    return employee_service.create_employee(db, data)


@router.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    summary="Update an employee",
    responses={
        200: {"description": "Employee updated successfully"},
        401: {"description": "Authentication required"},
        404: {"description": "Employee not found"}
    }
)
def update_employee(employee_id: str, data: EmployeeUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Update an existing employee record. All fields optional. Requires authentication."""
    employee = employee_service.update_employee(db, employee_id, data)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an employee",
    responses={
        204: {"description": "Employee deleted successfully"},
        401: {"description": "Authentication required"},
        404: {"description": "Employee not found"}
    }
)
def delete_employee(employee_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Delete an employee record by ID. Requires authentication."""
    deleted = employee_service.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")