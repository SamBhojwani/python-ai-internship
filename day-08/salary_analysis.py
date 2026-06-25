"""
salary_analysis.py
------------------
Generates random salary data for 100 employees
and performs statistical analysis using NumPy.

Usage:
    python salary_analysis.py
"""

import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate random salaries between 30,000 and 150,000 for 100 employees
salaries = np.random.randint(30000, 150001, size=100)

def main() -> None:
    average = salaries.mean()
    maximum = salaries.max()
    minimum = salaries.min()
    std_dev = salaries.std()
    top_10 = np.sort(salaries)[-10:][::-1]

    print("\n" + "=" * 45)
    print("       EMPLOYEE SALARY ANALYSIS REPORT")
    print("=" * 45)
    print(f"  Total Employees    : {len(salaries)}")
    print(f"  Average Salary     : ₹{average:,.2f}")
    print(f"  Maximum Salary     : ₹{maximum:,}")
    print(f"  Minimum Salary     : ₹{minimum:,}")
    print(f"  Standard Deviation : ₹{std_dev:,.2f}")

    print("\n  Top 10 Highest Salaries:")
    for i, salary in enumerate(top_10, start=1):
        print(f"    {i:>2}. ₹{salary:,}")

    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()