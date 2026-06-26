"""
employee_analysis.py
--------------------
Analyzes employee dataset using Pandas.
Exports summary to a CSV report.

Usage:
    python employee_analysis.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/employees_day9.csv"
REPORT_FILE = "reports/employee_summary.csv"


def load_data(filepath: str) -> pd.DataFrame:
    """Load employee dataset from CSV."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records from {filepath}")
    return df


def analyze(df: pd.DataFrame) -> None:
    """Generate and display employee analysis report."""

    print("\n" + "=" * 50)
    print("        EMPLOYEE DATASET ANALYSIS")
    print("=" * 50)

    # Basic stats
    print(f"\nTotal Employees  : {len(df)}")
    print(f"Average Salary   : Rs.{df['salary'].mean():,.2f}")
    print(f"Highest Salary   : Rs.{df['salary'].max():,}")
    print(f"Lowest Salary    : Rs.{df['salary'].min():,}")

    # Employees by department
    print("\nEmployees by Department:")
    dept_counts = df.groupby("department")["name"].count()
    for dept, count in dept_counts.items():
        print(f"  {dept:<20} {count} employees")

    # Average salary by department
    print("\nAverage Salary by Department:")
    dept_salary = df.groupby("department")["salary"].mean()
    for dept, avg in dept_salary.items():
        print(f"  {dept:<20} Rs.{avg:,.2f}")

    # Top 5 highest paid
    print("\nTop 5 Highest Paid Employees:")
    top5 = df.nlargest(5, "salary")[["name", "department", "salary"]]
    for _, row in top5.iterrows():
        print(f"  {row['name']:<20} {row['department']:<15} Rs.{row['salary']:,}")

    print("=" * 50)


def export_summary(df: pd.DataFrame, output_path: str) -> None:
    """Export summary statistics to a CSV file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    summary = pd.DataFrame({
        "Metric": [
            "Total Employees",
            "Average Salary",
            "Highest Salary",
            "Lowest Salary",
        ],
        "Value": [
            len(df),
            round(df["salary"].mean(), 2),
            df["salary"].max(),
            df["salary"].min(),
        ]
    })

    dept_summary = df.groupby("department").agg(
        Total_Employees=("name", "count"),
        Average_Salary=("salary", "mean"),
        Highest_Salary=("salary", "max"),
    ).reset_index()

    summary.to_csv(output_path, index=False)
    dept_summary.to_csv(output_path.replace(".csv", "_by_dept.csv"), index=False)
    print(f"\nSummary exported to {output_path}")


def main() -> None:
    df = load_data(INPUT_FILE)

    print("\nDataset Overview:")
    print(df.head())
    print(f"\nShape: {df.shape}")
    print(f"\nColumn Info:")
    print(df.info())
    print(f"\nStatistical Summary:")
    print(df.describe())

    analyze(df)
    export_summary(df, REPORT_FILE)


if __name__ == "__main__":
    main()