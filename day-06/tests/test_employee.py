"""
test_employee.py
----------------
Unit tests for the Employee Management System (Day 5).

Run:
    python -m unittest tests/test_employee.py
"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../day-05"))

from models.employee import Employee
from services.employee_service import EmployeeService


class TestEmployeeService(unittest.TestCase):

    def setUp(self):
        """Set up a fresh service and sample employee before each test."""
        self.service = EmployeeService()
        self.emp1 = Employee("E001", "Aman Sharma", "Engineering", 90000, "aman@example.com")
        self.emp2 = Employee("E002", "Bhumi Patel", "Data Science", 75000, "bhumi@example.com")
        self.emp3 = Employee("E003", "Chaitanya Rao", "Engineering", 85000, "chaitanya@example.com")
        self.service.add_employee(self.emp1)
        self.service.add_employee(self.emp2)
        self.service.add_employee(self.emp3)


    # ── Add Employee Tests ────────────────────────────────────

    def test_add_employee_success(self):
        """Adding a new employee should increase total count."""
        emp = Employee("E004", "Dhruv Mehta", "HR", 55000, "dhruv@example.com")
        self.service.add_employee(emp)
        self.assertEqual(self.service.total_employees(), 4)

    def test_add_duplicate_employee_raises_error(self):
        """Adding an employee with an existing ID should raise ValueError."""
        duplicate = Employee("E001", "Someone Else", "HR", 50000, "x@x.com")
        with self.assertRaises(ValueError):
            self.service.add_employee(duplicate)

    def test_add_employee_stored_correctly(self):
        """Added employee should be retrievable with correct data."""
        emp = self.service.get_employee("E001")
        self.assertEqual(emp.name, "Aman Sharma")
        self.assertEqual(emp.salary, 90000)
        self.assertEqual(emp.email, "aman@example.com")


    # ── Delete Employee Tests ─────────────────────────────────

    def test_delete_employee_success(self):
        """Deleting an employee should reduce total count."""
        self.service.delete_employee("E001")
        self.assertEqual(self.service.total_employees(), 2)

    def test_delete_nonexistent_employee_raises_error(self):
        """Deleting a non-existent employee should raise KeyError."""
        with self.assertRaises(KeyError):
            self.service.delete_employee("E999")

    def test_deleted_employee_not_retrievable(self):
        """Deleted employee should not be found."""
        self.service.delete_employee("E001")
        with self.assertRaises(KeyError):
            self.service.get_employee("E001")


    # ── Update Employee Tests ─────────────────────────────────

    def test_update_employee_name(self):
        """Updating name should reflect the new value."""
        self.service.update_employee("E001", "name", "Aman B")
        emp = self.service.get_employee("E001")
        self.assertEqual(emp.name, "Aman B")

    def test_update_employee_salary(self):
        """Updating salary should reflect the new value."""
        self.service.update_employee("E001", "salary", 95000)
        emp = self.service.get_employee("E001")
        self.assertEqual(emp.salary, 95000)

    def test_update_nonexistent_employee_raises_error(self):
        """Updating a non-existent employee should raise KeyError."""
        with self.assertRaises(KeyError):
            self.service.update_employee("E999", "name", "Nobody")

    def test_update_invalid_field_raises_error(self):
        """Updating a field that doesn't exist should raise AttributeError."""
        with self.assertRaises(AttributeError):
            self.service.update_employee("E001", "invalid_field", "value")


    # ── Search Employee Tests ─────────────────────────────────

    def test_search_by_id_success(self):
        """Searching by valid ID should return correct employee."""
        emp = self.service.get_employee("E002")
        self.assertEqual(emp.name, "Bhumi Patel")

    def test_search_by_id_not_found(self):
        """Searching by invalid ID should raise KeyError."""
        with self.assertRaises(KeyError):
            self.service.get_employee("E999")

    def test_search_by_name(self):
        """Searching by name should return matching employees."""
        results = self.service.search_by_name("Aman")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Aman Sharma")

    def test_search_by_name_no_results(self):
        """Searching by non-existent name should return empty list."""
        results = self.service.search_by_name("Zara")
        self.assertEqual(results, [])

    def test_search_by_department(self):
        """Searching by department should return all matching employees."""
        results = self.service.search_by_department("Engineering")
        self.assertEqual(len(results), 2)

    def test_search_by_department_no_results(self):
        """Searching by non-existent department should return empty list."""
        results = self.service.search_by_department("Finance")
        self.assertEqual(results, [])


    # ── Stats Tests ───────────────────────────────────────────

    def test_total_employees(self):
        """Total employees should match number added."""
        self.assertEqual(self.service.total_employees(), 3)

    def test_average_salary(self):
        """Average salary should be correct."""
        expected = round((90000 + 75000 + 85000) / 3, 2)
        self.assertEqual(self.service.average_salary(), expected)

    def test_highest_paid(self):
        """Highest paid should return employee with max salary."""
        top = self.service.highest_paid()
        self.assertEqual(top.name, "Aman Sharma")

    def test_average_salary_empty_raises_error(self):
        """Average salary on empty service should raise ValueError."""
        empty_service = EmployeeService()
        with self.assertRaises(ValueError):
            empty_service.average_salary()


if __name__ == "__main__":
    unittest.main()