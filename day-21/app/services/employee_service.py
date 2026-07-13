"""
employee_service.py
-------------------
Business logic for employee CRUD operations.
"""

from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate
from app.logger import logger
from app.utils.id_generator import generate_employee_id


def get_all_employees(db: Session, page: int = 1, size: int = 10) -> list:
    """Return paginated employees from the database."""
    offset = (page - 1) * size
    return db.query(Employee).offset(offset).limit(size).all()


def get_employee_by_id(db: Session, employee_id: str) -> Employee | None:
    """Return a single employee by employee_id or None if not found."""
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()


def create_employee(db: Session, data: EmployeeCreate) -> Employee:
    """Create a new employee record in the database."""
    employee_id = generate_employee_id(db)
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
    logger.info(f"Employee created: {employee_id} - {data.name} ({data.department})")
    return employee


def update_employee(db: Session, employee_id: str, data: EmployeeUpdate) -> Employee | None:
    """Update an existing employee record."""
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        logger.error(f"Employee not found for update: {employee_id}")
        return None
    update_data = data.model_dump(exclude_none=True)
    for key, value in update_data.items():
        setattr(employee, key, value)
    db.commit()
    db.refresh(employee)
    logger.info(f"Employee updated: {employee_id}")
    return employee


def delete_employee(db: Session, employee_id: str) -> bool:
    """Delete an employee. Returns True if deleted, False if not found."""
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        logger.error(f"Employee not found for deletion: {employee_id}")
        return False
    db.delete(employee)
    db.commit()
    logger.info(f"Employee deleted: {employee_id}")
    return True


def search_employees_by_name(db: Session, name: str) -> list:
    """Return employees whose name contains the search string."""
    return db.query(Employee).filter(
        Employee.name.ilike(f"%{name}%")
    ).all()


def get_employees_by_department(db: Session, department: str) -> list:
    """Return all employees in a given department."""
    return db.query(Employee).filter(
        Employee.department.ilike(f"%{department}%")
    ).all()