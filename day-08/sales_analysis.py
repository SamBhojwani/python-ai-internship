"""
sales_analysis.py
-----------------
Analyzes monthly sales data using NumPy.

Usage:
    python sales_analysis.py
"""

import numpy as np

# Monthly sales data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

sales = np.array([
    12000, 15000, 18000, 17000,
    22000, 21000, 24000, 25000,
    23000, 26000, 28000, 30000
])


def main() -> None:
    total = sales.sum()
    average = sales.mean()
    highest = sales.max()
    lowest = sales.min()
    highest_month = months[np.argmax(sales)]
    lowest_month = months[np.argmin(sales)]

    print("\n" + "=" * 45)
    print("       MONTHLY SALES ANALYSIS REPORT")
    print("=" * 45)

    print("\nMonth-wise Sales:")
    for month, amount in zip(months, sales):
        bar = "█" * (amount // 2000)
        print(f"  {month:<12} ₹{amount:>8,}  {bar}")

    print("\n" + "-" * 45)
    print(f"  Total Annual Sales   : ₹{total:,}")
    print(f"  Average Monthly Sales: ₹{average:,.1f}")
    print(f"  Highest Sales        : ₹{highest:,} ({highest_month})")
    print(f"  Lowest Sales         : ₹{lowest:,} ({lowest_month})")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()