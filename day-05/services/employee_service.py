"""
employee_service.py
-------------------
Handles all business logic for managing employee records.
"""

import logging
from models.employee import Employee

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class EmployeeService:
    def __init__(self):
        self.employees: dict[str, Employee] = {}

    def add_employee(self, employee: Employee) -> None:
        """
        Add a new employee record.

        Args:
            employee: Employee object to add.

        Raises:
            ValueError: If employee ID already exists.
        """
        if employee.employee_id in self.employees:
            raise ValueError(f"Employee with ID {employee.employee_id} already exists.")
        self.employees[employee.employee_id] = employee
        logger.info(f"Employee {employee.name} added.")

    def get_employee(self, employee_id: str) -> Employee:
        """
        Get an employee by ID.

        Args:
            employee_id: ID of the employee to retrieve.

        Returns:
            Employee object.

        Raises:
            KeyError: If employee ID does not exist.
        """
        if employee_id not in self.employees:
            raise KeyError(f"No employee found with ID {employee_id}.")
        return self.employees[employee_id]

    def update_employee(self, employee_id: str, field: str, value) -> None:
        """
        Update a specific field of an employee record.

        Args:
            employee_id: ID of the employee to update.
            field: Field name to update.
            value: New value for the field.

        Raises:
            KeyError: If employee ID does not exist.
            AttributeError: If field does not exist on Employee.
        """
        employee = self.get_employee(employee_id)
        if not hasattr(employee, field):
            raise AttributeError(f"Employee has no field '{field}'.")
        setattr(employee, field, value)
        logger.info(f"Employee {employee_id} {field} updated.")

    def delete_employee(self, employee_id: str) -> None:
        """
        Delete an employee record by ID.

        Args:
            employee_id: ID of the employee to delete.

        Raises:
            KeyError: If employee ID does not exist.
        """
        employee = self.get_employee(employee_id)
        del self.employees[employee_id]
        logger.info(f"Employee {employee.name} deleted.")

    def list_employees(self) -> list[Employee]:
        """Return a list of all employees."""
        return list(self.employees.values())