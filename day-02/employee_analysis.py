"""
employee_analysis.py
--------------------
Processes a list of employee records using list comprehensions,
lambda functions, and built-in functions.

Usage:
    python employee_analysis.py
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

employees = [
    {"name": "Aman", "salary": 50000},
    {"name": "Bhumi", "salary": 75000},
    {"name": "Chaitanya", "salary": 60000},
    {"name": "Dhruv", "salary": 90000},
    {"name": "Ekta", "salary": 45000},
]


def find_highest_salary(employees: list[dict]) -> dict:
    """Return the employee with the highest salary."""
    return max(employees, key=lambda e: e["salary"])


def find_average_salary(employees: list[dict]) -> float:
    """Return the average salary across all employees."""
    total = sum(e["salary"] for e in employees)
    return round(total / len(employees), 2)


def sort_by_salary(employees: list[dict], descending: bool = False) -> list[dict]:
    """Return employees sorted by salary."""
    return sorted(employees, key=lambda e: e["salary"], reverse=descending)


def get_names(employees: list[dict]) -> list[str]:
    """Return a list of employee names using list comprehension."""
    return [e["name"] for e in employees]


def main() -> None:
    logger.info("Starting employee analysis.")

    print("\n" + "=" * 45)
    print("        EMPLOYEE ANALYSIS REPORT")
    print("=" * 45)

    # All employees
    print("\nAll Employees:")
    for e in employees:
        print(f"  {e['name']:<12} ₹{e['salary']:,}")

    # Highest salary
    top = find_highest_salary(employees)
    print(f"\nHighest Salary : {top['name']} — ₹{top['salary']:,}")

    # Average salary
    avg = find_average_salary(employees)
    print(f"Average Salary : ₹{avg:,}")

    # Sorted ascending
    print("\nSorted by Salary (Low → High):")
    for e in sort_by_salary(employees):
        print(f"  {e['name']:<12} ₹{e['salary']:,}")

    # Sorted descending
    print("\nSorted by Salary (High → Low):")
    for e in sort_by_salary(employees, descending=True):
        print(f"  {e['name']:<12} ₹{e['salary']:,}")

    # Names only
    print(f"\nEmployee Names : {get_names(employees)}")

    print("\n" + "=" * 45)
    logger.info("Analysis complete.")


if __name__ == "__main__":
    main()