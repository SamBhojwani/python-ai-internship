"""
routes.py
---------
API endpoint definitions for the Employee API.
Routes handle HTTP only - all logic is in crud.py.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app import crud
from typing import List

router = APIRouter()


@router.get("/employees", response_model=List[EmployeeResponse], tags=["Employees"])
def get_all_employees(db: Session = Depends(get_db)):
    """Return all employees."""
    return crud.get_all_employees(db)


@router.get("/employees/{employee_id}", response_model=EmployeeResponse, tags=["Employees"])
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    """Return a single employee by ID."""
    employee = crud.get_employee_by_id(db, employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED, tags=["Employees"])
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee."""
    return crud.create_employee(db, data)


@router.put("/employees/{employee_id}", response_model=EmployeeResponse, tags=["Employees"])
def update_employee(employee_id: str, data: EmployeeUpdate, db: Session = Depends(get_db)):
    """Update an existing employee."""
    employee = crud.update_employee(db, employee_id, data)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Employees"])
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    """Delete an employee."""
    deleted = crud.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")