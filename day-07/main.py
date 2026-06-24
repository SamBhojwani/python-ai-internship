"""
main.py
-------
CLI interface for the Personal Finance Tracker.

Usage:
    python main.py
"""

import logging
import os
from datetime import datetime
from models.expense import Expense
from services.expense_service import ExpenseService

# ── Logging Setup ─────────────────────────────────────────────
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("logs/app.log", mode="a", encoding="utf-8")
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))
logging.getLogger().addHandler(file_handler)

# ── Constants ─────────────────────────────────────────────────
DATA_FILE = "data/expenses.json"
service = ExpenseService()


# ── Helper ────────────────────────────────────────────────────
def get_next_id() -> str:
    """Generate the next expense ID."""
    existing = [int(eid.replace("E", "")) for eid in service.expenses.keys() if eid.startswith("E")]
    next_num = max(existing) + 1 if existing else 1
    return f"E{next_num:03d}"


def is_valid_date(date_str: str) -> bool:
    """Validate date format YYYY-MM-DD."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ── Menu Functions ────────────────────────────────────────────
def add_expense() -> None:
    """Collect input and add a new expense."""
    print("\n-- Add Expense --")

    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    category = input("Category (e.g. Food, Travel, Shopping): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Amount: ").strip())
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
    except ValueError as e:
        print(f"Invalid amount: {e}")
        return

    date_str = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    elif not is_valid_date(date_str):
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    expense_id = get_next_id()

    try:
        expense = Expense(expense_id, title, category, amount, date_str)
        service.add_expense(expense)
        service.save_to_json(DATA_FILE)
        print(f"Expense '{title}' added successfully with ID {expense_id}.")
    except ValueError as e:
        print(f"Error: {e}")


def view_expenses() -> None:
    """Display all expenses."""
    print("\n-- All Expenses --")
    expenses = service.list_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<8} {'Date':<14} {'Title':<20} {'Category':<15} {'Amount'}")
    print("=" * 70)
    for e in expenses:
        print(f"{e.expense_id:<8} {e.date:<14} {e.title:<20} {e.category:<15} ₹{e.amount:,.2f}")
    print("=" * 70)
    print(f"Total: {len(expenses)} expenses\n")


def delete_expense() -> None:
    """Delete an expense by ID."""
    print("\n-- Delete Expense --")
    expense_id = input("Enter Expense ID: ").strip()

    try:
        service.delete_expense(expense_id)
        service.save_to_json(DATA_FILE)
        print(f"Expense {expense_id} deleted successfully.")
    except KeyError as e:
        print(f"Error: {e}")


def search_expenses() -> None:
    """Search expenses by title or category."""
    print("\n-- Search Expenses --")
    keyword = input("Enter keyword (title or category): ").strip()

    if not keyword:
        print("Keyword cannot be empty.")
        return

    results = service.search_expenses(keyword)

    if not results:
        print("No expenses found.")
        return

    print(f"\nFound {len(results)} result(s):")
    print("-" * 60)
    for e in results:
        print(e)
    print("-" * 60)


def generate_report() -> None:
    """Generate and display financial summary report."""
    print("\n-- Financial Report --")

    if not service.expenses:
        print("No expenses found.")
        return

    try:
        total = service.total_expenses()
        highest = service.highest_expense()
        lowest = service.lowest_expense()
        summary = service.category_summary()

        print("\n" + "=" * 45)
        print("       FINANCIAL SUMMARY REPORT")
        print("=" * 45)
        print(f"Total Expenses  : ₹{total:,.2f}")
        print(f"Highest Expense : {highest.title} — ₹{highest.amount:,.2f}")
        print(f"Lowest Expense  : {lowest.title} — ₹{lowest.amount:,.2f}")

        print("\nCategory-wise Summary:")
        for category, amount in sorted(summary.items()):
            print(f"  {category:<20} ₹{amount:,.2f}")
        print("=" * 45)

        logger.info("Report Generated")

    except ValueError as e:
        print(f"Error: {e}")


def main() -> None:
    """Main loop — load expenses and show menu."""
    logger.info("Application Started")
    service.load_from_json(DATA_FILE)
    print("Welcome to Personal Finance Tracker")

    try:
        while True:
            print("\n--- Menu ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Delete Expense")
            print("4. Search Expenses")
            print("5. Generate Report")
            print("6. Exit")

            choice = input("\nEnter choice: ").strip()

            if choice == "1":
                add_expense()
            elif choice == "2":
                view_expenses()
            elif choice == "3":
                delete_expense()
            elif choice == "4":
                search_expenses()
            elif choice == "5":
                generate_report()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-6.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    main()