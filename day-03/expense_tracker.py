"""
expense_tracker.py
------------------
A CLI-based expense tracker that persists data using a JSON file.

Usage:
    python expense_tracker.py
"""

import json
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

DATA_FILE = "data/expenses.json"


def load_expenses() -> list:
    """
    Load expenses from the JSON file.

    Returns:
        List of expense dicts. Returns empty list if file doesn't exist.
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.info("No existing expenses file found. Starting fresh.")
        return []
    except json.JSONDecodeError:
        logger.error("Expenses file is corrupted. Starting fresh.")
        return []


def save_expenses(expenses: list) -> None:
    """
    Save expenses to the JSON file.

    Args:
        expenses: List of expense dicts to save.
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4)
    logger.info("Expenses saved.")


def add_expense(expenses: list) -> None:
    """Add a new expense record."""
    title = input("Enter Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    try:
        amount = float(input("Enter Amount: ").strip())
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return

    category = input("Enter Category (e.g. Food, Travel, Bills): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "title": title,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense '{title}' added successfully.")


def view_expenses(expenses: list) -> None:
    """Display all expenses."""
    if not expenses:
        print("No expenses found.")
        return

    print("\n" + "=" * 55)
    print(f"{'#':<5} {'Title':<20} {'Category':<15} {'Amount'}")
    print("=" * 55)
    for i, e in enumerate(expenses, start=1):
        print(f"{i:<5} {e['title']:<20} {e['category']:<15} ₹{e['amount']:.2f}")
    print("=" * 55)


def calculate_total(expenses: list) -> None:
    """Calculate and display total expenses."""
    if not expenses:
        print("No expenses to calculate.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")

    categories: dict[str, float] = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

    print("\nBreakdown by Category:")
    for cat, amount in categories.items():
        print(f"  {cat:<15} ₹{amount:.2f}")


def main() -> None:
    """Main loop — load expenses and show menu."""
    expenses = load_expenses()
    print("Welcome to Expense Tracker")

    try:
        while True:
            print("\n--- Menu ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Calculate Total")
            print("4. Exit")

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                add_expense(expenses)
            elif choice == "2":
                view_expenses(expenses)
            elif choice == "3":
                calculate_total(expenses)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    main()