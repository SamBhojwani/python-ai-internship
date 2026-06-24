"""
expense.py
----------
Defines the Expense model class.
"""

from datetime import date


class Expense:
    def __init__(
        self,
        expense_id: str,
        title: str,
        category: str,
        amount: float,
        date: str,
    ):
        self.expense_id = expense_id
        self.title = title
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self) -> dict:
        """Convert Expense object to a dictionary for JSON serialization."""
        return {
            "expense_id": self.expense_id,
            "title": self.title,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """Create an Expense object from a dictionary."""
        return cls(
            expense_id=data["expense_id"],
            title=data["title"],
            category=data["category"],
            amount=data["amount"],
            date=data["date"],
        )

    def __str__(self) -> str:
        """Human-readable string representation."""
        return (
            f"ID: {self.expense_id} | {self.date} | {self.title} | "
            f"{self.category} | ₹{self.amount:,.2f}"
        )

    def __repr__(self) -> str:
        """Developer-friendly representation for debugging."""
        return (
            f"Expense(id={self.expense_id!r}, title={self.title!r}, "
            f"category={self.category!r}, amount={self.amount}, date={self.date!r})"
        )