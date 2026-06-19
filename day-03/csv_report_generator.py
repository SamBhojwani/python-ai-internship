"""
csv_report_generator.py
-----------------------
Reads employee data from a CSV file, calculates salary statistics,
and exports a summary report as a JSON file.

Usage:
    python csv_report_generator.py <input_csv> <output_json>

Example:
    python csv_report_generator.py data/employees.csv data/report.json
"""

import sys
import json
import logging
import csv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def read_csv(filepath: str) -> list[dict]:
    """
    Read employee data from a CSV file.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of employee dicts.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or missing required columns.
    """
    logger.info(f"Reading CSV: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            employees = list(reader)

        if not employees:
            raise ValueError("CSV file is empty.")

        required_columns = {"name", "salary"}
        if not required_columns.issubset(employees[0].keys()):
            raise ValueError(f"CSV must contain columns: {required_columns}")

        # convert salary to float
        for emp in employees:
            try:
                emp["salary"] = float(emp["salary"])
            except ValueError:
                raise ValueError(f"Invalid salary for employee: {emp['name']}")

        logger.info(f"Loaded {len(employees)} employee records.")
        return employees

    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise


def generate_report(employees: list[dict]) -> dict:
    """
    Generate a salary summary report from employee data.

    Args:
        employees: List of employee dicts with name and salary.

    Returns:
        Summary report as a dict.
    """
    salaries = [e["salary"] for e in employees]
    highest = max(employees, key=lambda e: e["salary"])
    lowest = min(employees, key=lambda e: e["salary"])

    return {
        "total_employees": len(employees),
        "average_salary": round(sum(salaries) / len(salaries), 2),
        "highest_salary": {
            "name": highest["name"],
            "salary": highest["salary"]
        },
        "lowest_salary": {
            "name": lowest["name"],
            "salary": lowest["salary"]
        },
        "all_employees": sorted(employees, key=lambda e: e["salary"], reverse=True)
    }


def save_report(report: dict, output_path: str) -> None:
    """
    Save the report to a JSON file.

    Args:
        report: Summary report dict.
        output_path: Path to save the JSON file.
    """
    logger.info(f"Saving report to: {output_path}")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        logger.info("Report saved successfully.")
    except OSError as e:
        logger.error(f"Failed to save report: {e}")
        raise


def display_summary(report: dict) -> None:
    """Print a summary of the report to the terminal."""
    print("\n" + "=" * 45)
    print("        CSV REPORT SUMMARY")
    print("=" * 45)
    print(f"Total Employees : {report['total_employees']}")
    print(f"Average Salary  : ₹{report['average_salary']:,}")
    print(f"Highest Salary  : {report['highest_salary']['name']} — ₹{report['highest_salary']['salary']:,}")
    print(f"Lowest Salary   : {report['lowest_salary']['name']} — ₹{report['lowest_salary']['salary']:,}")
    print("\nAll Employees (High → Low):")
    for emp in report["all_employees"]:
        print(f"  {emp['name']:<20} ₹{emp['salary']:,}")
    print("=" * 45 + "\n")


def main() -> None:
    """Entry point: read CSV, generate report, save as JSON."""
    if len(sys.argv) != 3:
        print("Usage: python csv_report_generator.py <input_csv> <output_json>")
        sys.exit(1)

    input_csv: str = sys.argv[1]
    output_json: str = sys.argv[2]

    try:
        employees = read_csv(input_csv)
        report = generate_report(employees)
        display_summary(report)
        save_report(report, output_json)
        print(f"Report saved to '{output_json}'.")
    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()