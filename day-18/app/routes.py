"""
routes.py
---------
API endpoint definitions for the Employee API with authentication.
"""
from app.dependencies import get_current_user
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.models import User
from app import crud
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserRegister, UserLogin, UserResponse
from app import auth
from app import auth, security

router = APIRouter()


# Auth Endpoints

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Auth"])
def register(data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user."""
    if auth.get_user_by_username(db, data.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists."
        )
    if auth.get_user_by_email(db, data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    return auth.register_user(db, data)


@router.post("/login", tags=["Auth"])
def login(data: UserLogin, db: Session = Depends(get_db)):
    """Login with username and password and receive a JWT token."""
    user = auth.authenticate_user(db, data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )
    token = security.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse, tags=["Auth"])
def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Return the currently logged in user's information."""
    return current_user

# Employee Endpoints

@router.get("/employees", response_model=List[EmployeeResponse], tags=["Employees"])
def get_all_employees(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    """Return all employees - public endpoint."""
    return crud.get_all_employees(db, page, size)


@router.get("/employees/department/{department}", response_model=List[EmployeeResponse], tags=["Employees"])
def get_employees_by_department(department: str, db: Session = Depends(get_db)):
    """Return employees by department - public endpoint."""
    employees = crud.get_employees_by_department(db, department)
    if not employees:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No employees found in department: {department}")
    return employees


@router.get("/employees/{employee_id}", response_model=EmployeeResponse, tags=["Employees"])
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    """Return a single employee by ID - public endpoint."""
    employee = crud.get_employee_by_id(db, employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED, tags=["Employees"])
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Create a new employee - requires authentication."""
    return crud.create_employee(db, data)


@router.put("/employees/{employee_id}", response_model=EmployeeResponse, tags=["Employees"])
def update_employee(employee_id: str, data: EmployeeUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Update an employee - requires authentication."""
    employee = crud.update_employee(db, employee_id, data)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Employees"])
def delete_employee(employee_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Delete an employee - requires authentication."""
    deleted = crud.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")