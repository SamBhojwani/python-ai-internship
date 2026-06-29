"""
sales_eda.py
------------
Exploratory Data Analysis on sales dataset.
Exports summary report to CSV.

Usage:
    python sales_eda.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/sales_day10.csv"
REPORT_FILE = "reports/sales_summary.csv"

MONTH_ORDER = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


def load_data(filepath: str) -> pd.DataFrame:
    """Load sales dataset."""
    df = pd.read_csv(filepath)
    df["month"] = pd.Categorical(df["month"], categories=MONTH_ORDER, ordered=True)
    print(f"Loaded {len(df)} records.")
    return df


def analyze(df: pd.DataFrame) -> None:
    """Perform EDA and display sales insights."""

    # Monthly totals
    monthly_sales = df.groupby("month", observed=True)["revenue"].sum().reset_index()
    best_month = monthly_sales.loc[monthly_sales["revenue"].idxmax()]
    worst_month = monthly_sales.loc[monthly_sales["revenue"].idxmin()]

    # Product totals
    product_sales = df.groupby("product")["revenue"].sum().sort_values(ascending=False)

    # Category totals
    category_sales = df.groupby("category")["revenue"].sum().sort_values(ascending=False)

    print("\n" + "=" * 55)
    print("          SALES PERFORMANCE REPORT")
    print("=" * 55)

    print(f"\nTotal Annual Revenue  : Rs.{df['revenue'].sum():,}")
    print(f"Average Monthly Sales : Rs.{monthly_sales['revenue'].mean():,.2f}")
    print(f"Best Month            : {best_month['month']} - Rs.{best_month['revenue']:,}")
    print(f"Worst Month           : {worst_month['month']} - Rs.{worst_month['revenue']:,}")

    # Monthly summary with bar chart
    print("\nMonthly Revenue Summary:")
    for _, row in monthly_sales.iterrows():
        bar = "█" * (int(row["revenue"]) // 1000000)
        print(f"  {str(row['month']):<12} Rs.{row['revenue']:>12,}  {bar}")

    # Top 5 products
    print("\nTop 5 Products by Revenue:")
    for i, (product, revenue) in enumerate(product_sales.head(5).items(), start=1):
        print(f"  {i}. {product:<20} Rs.{revenue:,}")

    # Category breakdown
    print("\nRevenue by Category:")
    for category, revenue in category_sales.items():
        pct = (revenue / df["revenue"].sum()) * 100
        print(f"  {category:<20} Rs.{revenue:,} ({pct:.1f}%)")

    print("=" * 55)


def export_report(df: pd.DataFrame, output_path: str) -> None:
    """Export sales summary to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    monthly_summary = df.groupby("month", observed=True).agg(
        total_revenue=("revenue", "sum"),
        total_units=("units_sold", "sum"),
        avg_revenue=("revenue", "mean"),
    ).reset_index()

    monthly_summary["avg_revenue"] = monthly_summary["avg_revenue"].round(2)
    monthly_summary.to_csv(output_path, index=False)
    print(f"\nReport exported to {output_path}")


def main() -> None:
    df = load_data(INPUT_FILE)
    analyze(df)
    export_report(df, REPORT_FILE)


if __name__ == "__main__":
    main()