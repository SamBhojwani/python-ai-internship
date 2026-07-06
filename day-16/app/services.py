"""
services.py
-----------
Business logic for employee operations.
Routes call these functions instead of handling logic directly.
"""

from app.schemas import EmployeeCreate, EmployeeUpdate

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


def get_all_employees() -> list:
    """Return all employees."""
    return list(employees.values())


def get_employee_by_id(employee_id: str) -> dict | None:
    """Return a single employee by ID or None if not found."""
    return employees.get(employee_id)


def create_employee(data: EmployeeCreate) -> dict:
    """Create a new employee and return it."""
    employee_id = get_next_id()
    new_employee = {
        "employee_id": employee_id,
        **data.model_dump()
    }
    employees[employee_id] = new_employee
    return new_employee


def update_employee(employee_id: str, data: EmployeeUpdate) -> dict | None:
    """Update an existing employee and return it, or None if not found."""
    if employee_id not in employees:
        return None
    existing = employees[employee_id]
    update_data = data.model_dump(exclude_none=True)
    existing.update(update_data)
    employees[employee_id] = existing
    return existing


def delete_employee(employee_id: str) -> bool:
    """Delete an employee. Returns True if deleted, False if not found."""
    if employee_id not in employees:
        return False
    del employees[employee_id]
    return True


def search_employees_by_name(name: str) -> list:
    """Return employees whose name contains the search string."""
    return [
        emp for emp in employees.values()
        if name.lower() in emp["name"].lower()
    ]


def filter_employees_by_department(department: str) -> list:
    """Return employees belonging to a given department."""
    return [
        emp for emp in employees.values()
        if emp["department"].lower() == department.lower()
    ]