"""
test_expense.py
---------------
Unit tests for the Personal Finance Tracker.

Run:
    python -m unittest tests/test_expense.py
"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from models.expense import Expense
from services.expense_service import ExpenseService


class TestExpenseService(unittest.TestCase):

    def setUp(self):
        """Set up a fresh service with sample expenses before each test."""
        self.service = ExpenseService()
        self.exp1 = Expense("E001", "Lunch", "Food", 150.0, "2026-06-20")
        self.exp2 = Expense("E002", "Uber", "Travel", 80.0, "2026-06-21")
        self.exp3 = Expense("E003", "Groceries", "Food", 500.0, "2026-06-22")
        self.exp4 = Expense("E004", "Electricity", "Bills", 1200.0, "2026-06-22")
        self.service.add_expense(self.exp1)
        self.service.add_expense(self.exp2)
        self.service.add_expense(self.exp3)
        self.service.add_expense(self.exp4)


    # ── Add Expense Tests ─────────────────────────────────────

    def test_add_expense_success(self):
        """Adding a new expense should increase total count."""
        exp = Expense("E005", "Movie", "Entertainment", 250.0, "2026-06-23")
        self.service.add_expense(exp)
        self.assertEqual(len(self.service.expenses), 5)

    def test_add_duplicate_expense_raises_error(self):
        """Adding an expense with existing ID should raise ValueError."""
        duplicate = Expense("E001", "Dinner", "Food", 300.0, "2026-06-23")
        with self.assertRaises(ValueError):
            self.service.add_expense(duplicate)

    def test_add_expense_stored_correctly(self):
        """Added expense should be retrievable with correct data."""
        exp = self.service.get_expense("E001")
        self.assertEqual(exp.title, "Lunch")
        self.assertEqual(exp.amount, 150.0)
        self.assertEqual(exp.category, "Food")


    # ── Delete Expense Tests ──────────────────────────────────

    def test_delete_expense_success(self):
        """Deleting an expense should reduce total count."""
        self.service.delete_expense("E001")
        self.assertEqual(len(self.service.expenses), 3)

    def test_delete_nonexistent_expense_raises_error(self):
        """Deleting a non-existent expense should raise KeyError."""
        with self.assertRaises(KeyError):
            self.service.delete_expense("E999")

    def test_deleted_expense_not_retrievable(self):
        """Deleted expense should not be found."""
        self.service.delete_expense("E001")
        with self.assertRaises(KeyError):
            self.service.get_expense("E001")


    # ── Total Expense Tests ───────────────────────────────────

    def test_total_expenses(self):
        """Total should be sum of all expense amounts."""
        expected = 150.0 + 80.0 + 500.0 + 1200.0
        self.assertAlmostEqual(self.service.total_expenses(), expected, places=2)

    def test_total_expenses_empty(self):
        """Total of empty service should be zero."""
        empty_service = ExpenseService()
        self.assertEqual(empty_service.total_expenses(), 0)

    def test_total_after_delete(self):
        """Total should update correctly after deletion."""
        self.service.delete_expense("E001")
        expected = 80.0 + 500.0 + 1200.0
        self.assertAlmostEqual(self.service.total_expenses(), expected, places=2)


    # ── Search Expense Tests ──────────────────────────────────

    def test_search_by_title(self):
        """Searching by title keyword should return matching expenses."""
        results = self.service.search_expenses("lunch")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Lunch")

    def test_search_by_category(self):
        """Searching by category should return all matching expenses."""
        results = self.service.search_expenses("food")
        self.assertEqual(len(results), 2)

    def test_search_case_insensitive(self):
        """Search should be case insensitive."""
        results = self.service.search_expenses("TRAVEL")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Uber")

    def test_search_no_results(self):
        """Searching for non-existent keyword should return empty list."""
        results = self.service.search_expenses("xyz123")
        self.assertEqual(results, [])


    # ── Report Tests ──────────────────────────────────────────

    def test_highest_expense(self):
        """Should return expense with highest amount."""
        highest = self.service.highest_expense()
        self.assertEqual(highest.title, "Electricity")
        self.assertEqual(highest.amount, 1200.0)

    def test_lowest_expense(self):
        """Should return expense with lowest amount."""
        lowest = self.service.lowest_expense()
        self.assertEqual(lowest.title, "Uber")
        self.assertEqual(lowest.amount, 80.0)

    def test_category_summary(self):
        """Category summary should show correct totals per category."""
        summary = self.service.category_summary()
        self.assertAlmostEqual(summary["Food"], 650.0, places=2)
        self.assertAlmostEqual(summary["Travel"], 80.0, places=2)
        self.assertAlmostEqual(summary["Bills"], 1200.0, places=2)

    def test_highest_expense_empty_raises_error(self):
        """Highest expense on empty service should raise ValueError."""
        empty_service = ExpenseService()
        with self.assertRaises(ValueError):
            empty_service.highest_expense()

    def test_lowest_expense_empty_raises_error(self):
        """Lowest expense on empty service should raise ValueError."""
        empty_service = ExpenseService()
        with self.assertRaises(ValueError):
            empty_service.lowest_expense()


if __name__ == "__main__":
    unittest.main()