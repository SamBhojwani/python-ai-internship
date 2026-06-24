"""
expense_service.py
------------------
Handles all business logic for managing expense records.
"""

import json
import logging
import os

from models.expense import Expense

logger = logging.getLogger(__name__)


class ExpenseService:
    def __init__(self):
        self.expenses: dict[str, Expense] = {}

    def add_expense(self, expense: Expense) -> None:
        """
        Add a new expense record.

        Args:
            expense: Expense object to add.

        Raises:
            ValueError: If expense ID already exists.
        """
        if expense.expense_id in self.expenses:
            raise ValueError(f"Expense with ID {expense.expense_id} already exists.")
        self.expenses[expense.expense_id] = expense
        logger.info(f"Expense Added: {expense.title} - ₹{expense.amount}")

    def delete_expense(self, expense_id: str) -> None:
        """
        Delete an expense record by ID.

        Args:
            expense_id: ID of the expense to delete.

        Raises:
            KeyError: If expense ID does not exist.
        """
        if expense_id not in self.expenses:
            raise KeyError(f"No expense found with ID {expense_id}.")
        title = self.expenses[expense_id].title
        del self.expenses[expense_id]
        logger.info(f"Expense Deleted: {title}")

    def get_expense(self, expense_id: str) -> Expense:
        """
        Get an expense by ID.

        Args:
            expense_id: ID of the expense to retrieve.

        Returns:
            Expense object.

        Raises:
            KeyError: If expense ID does not exist.
        """
        if expense_id not in self.expenses:
            raise KeyError(f"No expense found with ID {expense_id}.")
        return self.expenses[expense_id]

    def list_expenses(self) -> list[Expense]:
        """Return all expenses sorted by date."""
        return sorted(self.expenses.values(), key=lambda e: e.date)

    def search_expenses(self, keyword: str) -> list[Expense]:
        """
        Search expenses by title or category.

        Args:
            keyword: Search keyword (case-insensitive).

        Returns:
            List of matching expenses.
        """
        keyword = keyword.lower()
        return [
            e for e in self.expenses.values()
            if keyword in e.title.lower() or keyword in e.category.lower()
        ]

    def total_expenses(self) -> float:
        """Return total amount of all expenses."""
        return sum(e.amount for e in self.expenses.values())

    def highest_expense(self) -> Expense:
        """
        Return the expense with the highest amount.

        Raises:
            ValueError: If no expenses exist.
        """
        if not self.expenses:
            raise ValueError("No expenses found.")
        return max(self.expenses.values(), key=lambda e: e.amount)

    def lowest_expense(self) -> Expense:
        """
        Return the expense with the lowest amount.

        Raises:
            ValueError: If no expenses exist.
        """
        if not self.expenses:
            raise ValueError("No expenses found.")
        return min(self.expenses.values(), key=lambda e: e.amount)

    def category_summary(self) -> dict[str, float]:
        """
        Return total spending per category.

        Returns:
            Dict of category to total amount.
        """
        summary: dict[str, float] = {}
        for e in self.expenses.values():
            summary[e.category] = summary.get(e.category, 0) + e.amount
        return summary

    def save_to_json(self, filepath: str) -> None:
        """
        Save all expenses to a JSON file.

        Args:
            filepath: Path to the JSON file.
        """
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        data = [e.to_dict() for e in self.expenses.values()]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logger.info("Expenses saved to file.")

    def load_from_json(self, filepath: str) -> None:
        """
        Load expenses from a JSON file.

        Args:
            filepath: Path to the JSON file.
        """
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.expenses = {
                e["expense_id"]: Expense.from_dict(e) for e in data
            }
            logger.info(f"Loaded {len(self.expenses)} expenses from file.")
        except FileNotFoundError:
            logger.info("No existing data file found. Starting fresh.")
        except json.JSONDecodeError:
            logger.error("Data file is corrupted. Starting fresh.")