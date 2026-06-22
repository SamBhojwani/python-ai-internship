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

    def total_employees(self) -> int:
        """Return total number of employees."""
        return len(self.employees)

    def average_salary(self) -> float:
        """
        Return average salary across all employees.

        Raises:
            ValueError: If no employees exist.
        """
        if not self.employees:
            raise ValueError("No employees found.")
        salaries = [emp.salary for emp in self.employees.values()]
        return round(sum(salaries) / len(salaries), 2)

    def highest_paid(self) -> Employee:
        """
        Return the highest paid employee.

        Raises:
            ValueError: If no employees exist.
        """
        if not self.employees:
            raise ValueError("No employees found.")
        return max(self.employees.values(), key=lambda e: e.salary)

    def group_by_department(self) -> dict[str, list[Employee]]:
        """Group employees by department."""
        departments: dict[str, list[Employee]] = {}
        for emp in self.employees.values():
            if emp.department not in departments:
                departments[emp.department] = []
            departments[emp.department].append(emp)
        return departments
    
    def save_to_json(self, filepath: str) -> None:
        """
        Save all employee records to a JSON file.

        Args:
            filepath: Path to the JSON file.
        """
        import json
        import os
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data = [emp.to_dict() for emp in self.employees.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logger.info(f"Employees saved to {filepath}")

    def load_from_json(self, filepath: str) -> None:
        """
        Load employee records from a JSON file.

        Args:
            filepath: Path to the JSON file.
        """
        import json
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.employees = {
                emp["employee_id"]: Employee.from_dict(emp) for emp in data
            }
            logger.info(f"Loaded {len(self.employees)} employees from {filepath}")
        except FileNotFoundError:
            logger.info("No existing data file found. Starting fresh.")
        except json.JSONDecodeError:
            logger.error("Data file is corrupted. Starting fresh.")
    
