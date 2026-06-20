"""
employee_processor.py
---------------------
Reads employee data from a CSV file, calculates salary statistics,
groups employees by department, and generates a summary report.
Logs application events to both terminal and app.log file.
Configuration is loaded from config.json.

Usage:
    python employee_processor.py
"""

import csv
import json
import logging
import os


def load_config(config_path: str = "config.json") -> dict:
    """
    Load configuration from a JSON file.

    Args:
        config_path: Path to the config file.

    Returns:
        Config dict.

    Raises:
        FileNotFoundError: If config file doesn't exist.
        ValueError: If config file contains invalid JSON.
    """
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_path}")
    except json.JSONDecodeError:
        raise ValueError("Config file contains invalid JSON.")


# load config first
config = load_config()

INPUT_FILE = config["input_file"]
REPORT_FILE = config["report_file"]
LOG_FILE = config["log_file"]

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_employees(filepath: str) -> list[dict]:
    """
    Read employee data from a CSV file.

    Args:
        filepath: Path to the CSV file.

    Returns:
        List of employee dicts.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If required columns are missing.
    """
    logger.info(f"Loading employee data from: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            employees = list(reader)

        if not employees:
            raise ValueError("CSV file is empty.")

        required = {"employee_id", "name", "department", "salary"}
        if not required.issubset(employees[0].keys()):
            raise ValueError(f"CSV must contain columns: {required}")

        for emp in employees:
            emp["salary"] = float(emp["salary"])

        logger.info(f"Loaded {len(employees)} employee records.")
        return employees

    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise


def calculate_stats(employees: list[dict]) -> dict:
    """
    Calculate overall salary statistics.

    Args:
        employees: List of employee dicts.

    Returns:
        Dict with total, average, highest and lowest salary stats.
    """
    salaries = [e["salary"] for e in employees]
    highest = max(employees, key=lambda e: e["salary"])
    lowest = min(employees, key=lambda e: e["salary"])

    return {
        "total_employees": len(employees),
        "average_salary": round(sum(salaries) / len(salaries), 2),
        "highest_salary": {"name": highest["name"], "salary": highest["salary"]},
        "lowest_salary": {"name": lowest["name"], "salary": lowest["salary"]},
    }


def group_by_department(employees: list[dict]) -> dict:
    """
    Group employees by department and calculate per-department stats.

    Args:
        employees: List of employee dicts.

    Returns:
        Dict of department name to stats.
    """
    departments: dict[str, list] = {}
    for emp in employees:
        dept = emp["department"]
        if dept not in departments:
            departments[dept] = []
        departments[dept].append(emp)

    summary = {}
    for dept, members in departments.items():
        salaries = [m["salary"] for m in members]
        summary[dept] = {
            "total_employees": len(members),
            "average_salary": round(sum(salaries) / len(salaries), 2),
            "highest_salary": max(salaries),
            "lowest_salary": min(salaries),
            "employees": [{"id": m["employee_id"], "name": m["name"], "salary": m["salary"]} for m in members],
        }

    return summary


def save_report(report: dict, output_path: str) -> None:
    """
    Save the report to a JSON file.

    Args:
        report: Report dict to save.
        output_path: Path to save the JSON file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    logger.info(f"Report saved to: {output_path}")


def display_summary(stats: dict, departments: dict) -> None:
    """Print a summary to the terminal."""
    print("\n" + "=" * 50)
    print("        EMPLOYEE REPORT SUMMARY")
    print("=" * 50)
    print(f"Total Employees : {stats['total_employees']}")
    print(f"Average Salary  : ₹{stats['average_salary']:,}")
    print(f"Highest Salary  : {stats['highest_salary']['name']} — ₹{stats['highest_salary']['salary']:,}")
    print(f"Lowest Salary   : {stats['lowest_salary']['name']} — ₹{stats['lowest_salary']['salary']:,}")

    print("\nBy Department:")
    for dept, info in departments.items():
        print(f"\n  {dept}")
        print(f"    Employees    : {info['total_employees']}")
        print(f"    Avg Salary   : ₹{info['average_salary']:,}")
        print(f"    Highest      : ₹{info['highest_salary']:,}")
        print(f"    Lowest       : ₹{info['lowest_salary']:,}")
    print("\n" + "=" * 50)


def main() -> None:
    logger.info("Application started.")

    try:
        employees = read_employees(INPUT_FILE)
        stats = calculate_stats(employees)
        departments = group_by_department(employees)
        display_summary(stats, departments)

        report = {"summary": stats, "departments": departments}
        save_report(report, REPORT_FILE)
        logger.info("Report generation complete.")

    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Processing failed: {e}")


if __name__ == "__main__":
    main()