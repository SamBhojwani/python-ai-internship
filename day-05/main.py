"""
main.py
-------
CLI interface for the Employee Management System.

Usage:
    python main.py
"""

import logging
from models.employee import Employee
from services.employee_service import EmployeeService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

service = EmployeeService()


def add_employee() -> None:
    """Collect input and add a new employee."""
    print("\n-- Add Employee --")
    employee_id = input("Employee ID: ").strip()
    name = input("Name: ").strip()
    department = input("Department: ").strip()

    try:
        salary = float(input("Salary: ").strip())
        if salary <= 0:
            raise ValueError("Salary must be greater than zero.")
    except ValueError as e:
        print(f"Invalid salary: {e}")
        return

    email = input("Email: ").strip()

    if not employee_id or not name or not department or not email:
        print("All fields are required.")
        return

    try:
        employee = Employee(employee_id, name, department, salary, email)
        service.add_employee(employee)
        print(f"Employee {name} added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def view_employee() -> None:
    """Search and display a single employee by ID."""
    print("\n-- View Employee --")
    employee_id = input("Enter Employee ID: ").strip()

    try:
        emp = service.get_employee(employee_id)
        print("\n" + "-" * 50)
        print(emp)
        print("-" * 50)
    except KeyError as e:
        print(f"Error: {e}")


def update_employee() -> None:
    """Update a specific field of an employee."""
    print("\n-- Update Employee --")
    employee_id = input("Enter Employee ID: ").strip()

    try:
        service.get_employee(employee_id)
    except KeyError as e:
        print(f"Error: {e}")
        return

    print("Which field to update?")
    print("1. Name")
    print("2. Department")
    print("3. Salary")
    print("4. Email")
    choice = input("Enter choice: ").strip()

    field_map = {"1": "name", "2": "department", "3": "salary", "4": "email"}
    if choice not in field_map:
        print("Invalid choice.")
        return

    field = field_map[choice]
    value = input(f"Enter new {field}: ").strip()

    if field == "salary":
        try:
            value = float(value)
            if value <= 0:
                raise ValueError("Salary must be greater than zero.")
        except ValueError as e:
            print(f"Invalid salary: {e}")
            return

    try:
        service.update_employee(employee_id, field, value)
        print(f"{field.capitalize()} updated successfully.")
    except (KeyError, AttributeError) as e:
        print(f"Error: {e}")


def delete_employee() -> None:
    """Delete an employee by ID."""
    print("\n-- Delete Employee --")
    employee_id = input("Enter Employee ID: ").strip()

    try:
        service.delete_employee(employee_id)
        print(f"Employee {employee_id} deleted successfully.")
    except KeyError as e:
        print(f"Error: {e}")


def list_employees() -> None:
    """Display all employees."""
    print("\n-- All Employees --")
    employees = service.list_employees()

    if not employees:
        print("No employees found.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<10} {'Name':<20} {'Department':<15} {'Salary':<12} {'Email'}")
    print("=" * 70)
    for emp in employees:
        print(f"{emp.employee_id:<10} {emp.name:<20} {emp.department:<15} ₹{emp.salary:<11,.0f} {emp.email}")
    print("=" * 70)
    print(f"Total: {len(employees)} employees")

def department_stats() -> None:
    """Display department statistics."""
    print("\n-- Department Statistics --")

    try:
        print(f"\nTotal Employees : {service.total_employees()}")
        print(f"Average Salary  : ₹{service.average_salary():,}")

        top = service.highest_paid()
        print(f"Highest Paid    : {top.name} — ₹{top.salary:,}")

        print("\nBy Department:")
        for dept, members in service.group_by_department().items():
            salaries = [m.salary for m in members]
            print(f"\n  {dept}")
            print(f"    Employees  : {len(members)}")
            print(f"    Avg Salary : ₹{round(sum(salaries)/len(salaries), 2):,}")
    except ValueError as e:
        print(f"Error: {e}")
    print()


def main() -> None:
    """Main loop — show menu and handle user input."""
    print("Welcome to Employee Management System")

    try:
        while True:
            print("1. Add Employee")
            print("2. View Employee")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. List All Employees")
            print("6. Department Statistics")
            print("7. Exit")

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                add_employee()
            elif choice == "2":
                view_employee()
            elif choice == "3":
                update_employee()
            elif choice == "4":
                delete_employee()
            elif choice == "5":
                list_employees()
            elif choice == "6":
                department_stats()
            elif choice == "7":
                print("Goodbye!")
                break   
            else:
                print("Invalid choice. Please enter 1-7.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    main()