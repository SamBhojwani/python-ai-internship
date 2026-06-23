"""
employee.py
-----------
Defines the Employee model class.
"""


class Employee:
    def __init__(
        self,
        employee_id: str,
        name: str,
        department: str,
        salary: float,
        email: str,
    ):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.email = email

    def to_dict(self) -> dict:
        """Convert Employee object to a dictionary for JSON serialization."""
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "department": self.department,
            "salary": self.salary,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Employee":
        """Create an Employee object from a dictionary."""
        return cls(
            employee_id=data["employee_id"],
            name=data["name"],
            department=data["department"],
            salary=data["salary"],
            email=data["email"],
        )

    def __str__(self) -> str:
        """Human-readable string representation."""
        return (
            f"ID: {self.employee_id} | Name: {self.name} | "
            f"Department: {self.department} | Salary: ₹{self.salary:,} | "
            f"Email: {self.email}"
        )

    def __repr__(self) -> str:
        """Developer-friendly representation for debugging."""
        return (
            f"Employee(id={self.employee_id!r}, name={self.name!r}, "
            f"department={self.department!r}, salary={self.salary}, "
            f"email={self.email!r})"
        )