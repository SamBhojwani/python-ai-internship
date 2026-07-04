"""
models.py
---------
Internal data models representing the Employee entity.
"""


class Employee:
    def __init__(self, employee_id: str, name: str, department: str, salary: float, email: str):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.email = email

    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "email": self.email,
        }