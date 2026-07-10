"""
routes.py
---------
API endpoint definitions for the Employee API.
Routes handle HTTP only - all logic is in crud.py and auth.py.
"""

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserRegister, UserLogin, UserResponse, EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.dependencies import get_current_user
from app.models import User
from app import crud, auth, security
from app.logger import logger
from typing import List

router = APIRouter()


# Auth Endpoints

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Auth"],
    summary="Register a new user",
    responses={
        201: {"description": "User registered successfully"},
        400: {"description": "Username or email already exists"}
    }
)
def register(data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user with a username, email, password and role. Passwords are hashed before storage."""
    if auth.get_user_by_username(db, data.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists.")
    if auth.get_user_by_email(db, data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
    return auth.register_user(db, data)


@router.post(
    "/login",
    tags=["Auth"],
    summary="Login and receive a JWT token",
    responses={
        200: {"description": "Login successful, returns JWT token"},
        401: {"description": "Invalid username or password"}
    }
)
def login(data: UserLogin, db: Session = Depends(get_db)):
    """Login with username and password. Returns a JWT access token valid for 30 minutes."""
    user = auth.authenticate_user(db, data.username, data.password)
    if not user:
        logger.warning(f"Failed login attempt for username: {data.username}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password.")
    token = security.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@router.get(
    "/me",
    response_model=UserResponse,
    tags=["Auth"],
    summary="Get current logged in user",
    responses={
        200: {"description": "Returns current user info"},
        401: {"description": "Invalid or expired token"}
    }
)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Returns the profile of the currently authenticated user."""
    return current_user


# Employee Endpoints

@router.get(
    "/employees",
    response_model=List[EmployeeResponse],
    tags=["Employees"],
    summary="Get all employees",
    responses={
        200: {"description": "Returns paginated list of employees"}
    }
)
def get_all_employees(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    """Return all employees with pagination. Use page and size query parameters to control results."""
    return crud.get_all_employees(db, page, size)


@router.get(
    "/employees/search",
    response_model=List[EmployeeResponse],
    tags=["Employees"],
    summary="Search employees by name",
    responses={
        200: {"description": "Returns matching employees"},
        404: {"description": "No employees found matching the search"}
    }
)
def search_employees(name: str, db: Session = Depends(get_db)):
    """Search employees by name. Returns all employees whose name contains the search string."""
    employees = crud.search_employees_by_name(db, name)
    if not employees:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No employees found with name containing: {name}")
    return employees


@router.get(
    "/employees/filter",
    response_model=List[EmployeeResponse],
    tags=["Employees"],
    summary="Filter employees by department",
    responses={
        200: {"description": "Returns employees in the specified department"},
        404: {"description": "No employees found in the department"}
    }
)
def filter_employees(department: str, db: Session = Depends(get_db)):
    """Filter employees by department name. Case-insensitive matching."""
    employees = crud.get_employees_by_department(db, department)
    if not employees:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No employees found in department: {department}")
    return employees


@router.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    tags=["Employees"],
    summary="Get employee by ID",
    responses={
        200: {"description": "Returns the employee"},
        404: {"description": "Employee not found"}
    }
)
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    """Return a single employee by their employee ID (e.g. E001)."""
    employee = crud.get_employee_by_id(db, employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Employees"],
    summary="Create a new employee",
    responses={
        201: {"description": "Employee created successfully"},
        401: {"description": "Authentication required"}
    }
)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Create a new employee record. Requires authentication."""
    return crud.create_employee(db, data)


@router.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    tags=["Employees"],
    summary="Update an employee",
    responses={
        200: {"description": "Employee updated successfully"},
        401: {"description": "Authentication required"},
        404: {"description": "Employee not found"}
    }
)
def update_employee(employee_id: str, data: EmployeeUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Update an existing employee record. All fields are optional. Requires authentication."""
    employee = crud.update_employee(db, employee_id, data)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")
    return employee


@router.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Employees"],
    summary="Delete an employee",
    responses={
        204: {"description": "Employee deleted successfully"},
        401: {"description": "Authentication required"},
        404: {"description": "Employee not found"}
    }
)
def delete_employee(employee_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Delete an employee record by ID. Requires authentication."""
    deleted = crud.delete_employee(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee {employee_id} not found.")


@router.get(
    "/health",
    tags=["Health"],
    summary="Health check",
    responses={
        200: {"description": "API is running"}
    }
)
def health_check():
    """Check if the API is running. Returns application status and version."""
    return {
        "status": "UP",
        "application": "Employee API",
        "version": "5.0.0"
    }