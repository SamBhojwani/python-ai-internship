"""
crud.py
-------
Database operations for the Employee API.
All functions take a SQLAlchemy session and return model instances.
"""

from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate


def get_next_employee_id(db: Session) -> str:
    """Generate the next sequential employee ID."""
    last = db.query(Employee).order_by(Employee.id.desc()).first()
    if not last:
        return "E001"
    num = int(last.employee_id.replace("E", "")) + 1
    return f"E{num:03d}"


def get_all_employees(db: Session, page: int = 1, size: int = 10) -> list:
    """Return paginated employees from the database."""
    offset = (page - 1) * size
    return db.query(Employee).offset(offset).limit(size).all()


def get_employee_by_id(db: Session, employee_id: str) -> Employee | None:
    """Return a single employee by employee_id or None if not found."""
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()


def create_employee(db: Session, data: EmployeeCreate) -> Employee:
    """Create a new employee record in the database."""
    employee_id = get_next_employee_id(db)
    employee = Employee(
        employee_id=employee_id,
        name=data.name,
        email=data.email,
        department=data.department,
        salary=data.salary
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def update_employee(db: Session, employee_id: str, data: EmployeeUpdate) -> Employee | None:
    """Update an existing employee record. Returns None if not found."""
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        return None
    update_data = data.model_dump(exclude_none=True)
    for key, value in update_data.items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: str) -> bool:
    """Delete an employee. Returns True if deleted, False if not found."""
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        return False
    db.delete(employee)
    db.commit()
    return True

def get_employees_by_department(db: Session, department: str) -> list:
    """Return all employees in a given department."""
    return db.query(Employee).filter(
        Employee.department.ilike(f"%{department}%")
    ).all()