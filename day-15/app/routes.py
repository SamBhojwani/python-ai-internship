"""
routes.py
---------
All API endpoints for the Employee API.
"""

from fastapi import APIRouter, HTTPException, status
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from typing import List

router = APIRouter()

# in-memory employee store
employees: dict[str, dict] = {
    "E001": {"employee_id": "E001", "name": "Aman Sharma", "department": "Engineering", "salary": 90000, "email": "aman@example.com"},
    "E002": {"employee_id": "E002", "name": "Bhumi Patel", "department": "Data Science", "salary": 75000, "email": "bhumi@example.com"},
    "E003": {"employee_id": "E003", "name": "Chaitanya Rao", "department": "HR", "salary": 55000, "email": "chaitanya@example.com"},
}


def get_next_id() -> str:
    """Generate the next sequential employee ID."""
    existing = [int(eid.replace("E", "")) for eid in employees.keys()]
    next_num = max(existing) + 1 if existing else 1
    return f"E{next_num:03d}"


# Employee Endpoints

@router.get(
    "/employees",
    response_model=List[EmployeeResponse],
    summary="Get all employees",
    tags=["Employees"],
)
def get_all_employees():
    """Return a list of all employees."""
    return list(employees.values())


@router.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    summary="Get employee by ID",
    tags=["Employees"],
)
def get_employee(employee_id: str):
    """Return a single employee by ID."""
    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found."
        )
    return employees[employee_id]


@router.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new employee",
    tags=["Employees"],
)
def create_employee(employee: EmployeeCreate):
    """Create a new employee record."""
    employee_id = get_next_id()
    new_employee = {
        "employee_id": employee_id,
        **employee.model_dump()
    }
    employees[employee_id] = new_employee
    return new_employee


@router.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    summary="Update an employee",
    tags=["Employees"],
)
def update_employee(employee_id: str, updates: EmployeeUpdate):
    """Update an existing employee record."""
    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found."
        )
    existing = employees[employee_id]
    update_data = updates.model_dump(exclude_none=True)
    existing.update(update_data)
    employees[employee_id] = existing
    return existing


@router.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an employee",
    tags=["Employees"],
)
def delete_employee(employee_id: str):
    """Delete an employee record by ID."""
    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found."
        )
    del employees[employee_id]


# Health Check

@router.get(
    "/health",
    summary="Health check",
    tags=["Health"],
)
def health_check():
    """Check if the API is running."""
    return {
        "status": "UP",
        "application": "Employee API",
        "version": "1.0.0"
    }


# Optional Challenge

@router.get(
    "/employees/department/{department}",
    response_model=List[EmployeeResponse],
    summary="Get employees by department",
    tags=["Employees"],
)
def get_employees_by_department(department: str):
    """Return all employees in a given department."""
    results = [
        emp for emp in employees.values()
        if emp["department"].lower() == department.lower()
    ]
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No employees found in department: {department}"
        )
    return results