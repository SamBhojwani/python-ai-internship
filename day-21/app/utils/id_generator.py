"""
id_generator.py
---------------
Utility functions for generating unique identifiers.
"""

from sqlalchemy.orm import Session
from app.models import Employee


def generate_employee_id(db: Session) -> str:
    """Generate the next sequential employee ID (e.g. E001, E002)."""
    last = db.query(Employee).order_by(Employee.id.desc()).first()
    if not last:
        return "E001"
    num = int(last.employee_id.replace("E", "")) + 1
    return f"E{num:03d}"