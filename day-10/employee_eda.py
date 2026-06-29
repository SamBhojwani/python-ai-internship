"""
employee_eda.py
---------------
Exploratory Data Analysis on employee dataset.
Exports summary report to CSV.

Usage:
    python employee_eda.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/employees_day9.csv"
REPORT_FILE = "reports/employee_summary.csv"


def load_data(filepath: str) -> pd.DataFrame:
    """Load employee dataset."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records.")
    return df


def analyze(df: pd.DataFrame) -> None:
    """Perform EDA and display insights."""

    print("\n" + "=" * 55)
    print("          EMPLOYEE INSIGHTS REPORT")
    print("=" * 55)

    # Basic stats
    print(f"\nTotal Employees     : {len(df)}")
    print(f"Total Departments   : {df['department'].nunique()}")

    # Employees by department
    print("\nEmployees by Department:")
    dept_counts = df.groupby("department")["name"].count().sort_values(ascending=False)
    for dept, count in dept_counts.items():
        print(f"  {dept:<20} {count} employees")

    # Average salary by department
    print("\nAverage Salary by Department:")
    dept_salary = df.groupby("department")["salary"].mean().sort_values(ascending=False)
    for dept, avg in dept_salary.items():
        print(f"  {dept:<20} Rs.{avg:,.2f}")

    # Highest and lowest paid
    highest = df.loc[df["salary"].idxmax()]
    lowest = df.loc[df["salary"].idxmin()]
    print(f"\nHighest Paid : {highest['name']} - Rs.{highest['salary']:,} ({highest['department']})")
    print(f"Lowest Paid  : {lowest['name']} - Rs.{lowest['salary']:,} ({lowest['department']})")

    # Salary distribution
    print(f"\nSalary Distribution:")
    print(f"  Mean   : Rs.{df['salary'].mean():,.2f}")
    print(f"  Median : Rs.{df['salary'].median():,.2f}")
    print(f"  Std Dev: Rs.{df['salary'].std():,.2f}")
    print(f"  Min    : Rs.{df['salary'].min():,}")
    print(f"  Max    : Rs.{df['salary'].max():,}")

    # Top 10 highest salaries
    print("\nTop 10 Highest Salaries:")
    top10 = df.nlargest(10, "salary")[["name", "department", "salary"]]
    for i, (_, row) in enumerate(top10.iterrows(), start=1):
        print(f"  {i:>2}. {row['name']:<20} {row['department']:<15} Rs.{row['salary']:,}")

    print("=" * 55)


def export_report(df: pd.DataFrame, output_path: str) -> None:
    """Export EDA summary to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    dept_summary = df.groupby("department").agg(
        total_employees=("name", "count"),
        average_salary=("salary", "mean"),
        highest_salary=("salary", "max"),
        lowest_salary=("salary", "min"),
    ).reset_index()

    dept_summary["average_salary"] = dept_summary["average_salary"].round(2)
    dept_summary.to_csv(output_path, index=False)
    print(f"\nReport exported to {output_path}")


def main() -> None:
    df = load_data(INPUT_FILE)
    analyze(df)
    export_report(df, REPORT_FILE)


if __name__ == "__main__":
    main()