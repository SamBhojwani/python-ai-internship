"""
sales_cleaner.py
----------------
Cleans and prepares the sales dataset for Machine Learning.
- Creates Total Revenue, Profit, Profit Percentage
- Assigns Quarter and Financial Year

Usage:
    python3 sales_cleaner.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/raw/sales_day10.csv"
OUTPUT_FILE = "datasets/cleaned/sales_cleaned.csv"

COST_PRICE_MAP = {
    "Laptop": 40000,
    "Phone": 18000,
    "Desk": 5000,
    "Chair": 3000,
}

MONTH_TO_QUARTER = {
    "January": "Q3", "February": "Q3", "March": "Q3",
    "April": "Q4", "May": "Q4", "June": "Q4",
    "July": "Q1", "August": "Q1", "September": "Q1",
    "October": "Q2", "November": "Q2", "December": "Q2",
}

MONTH_TO_FY = {
    "January": "FY2025-26", "February": "FY2025-26", "March": "FY2025-26",
    "April": "FY2026-27", "May": "FY2026-27", "June": "FY2026-27",
    "July": "FY2026-27", "August": "FY2026-27", "September": "FY2026-27",
    "October": "FY2026-27", "November": "FY2026-27", "December": "FY2026-27",
}


def load_data(filepath: str) -> pd.DataFrame:
    """Load raw sales dataset."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records.")
    return df


def inspect(df: pd.DataFrame) -> None:
    """Display dataset info before cleaning."""
    print("\n-- Before Cleaning --")
    print(f"Shape      : {df.shape}")
    print(f"Duplicates : {df.duplicated().sum()}")
    print("Missing Values:")
    print(df.isnull().sum().to_string())


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and engineer features in the sales dataset.
    - Remove duplicates
    - Standardize text columns
    - Create cost, profit and profit percentage columns
    - Assign quarter and financial year
    """
    df = df.copy()

    # remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"\nRemoved {before - len(df)} duplicate(s).")

    # standardize text columns
    df["month"] = df["month"].str.strip().str.title()
    df["product"] = df["product"].str.strip().str.title()
    df["category"] = df["category"].str.strip().str.title()

    # create cost price column
    df["cost_price"] = df["product"].map(COST_PRICE_MAP)

    # create total cost
    df["total_cost"] = df["cost_price"] * df["units_sold"]

    # create profit
    df["profit"] = df["revenue"] - df["total_cost"]

    # create profit percentage
    df["profit_pct"] = ((df["profit"] / df["revenue"]) * 100).round(2)

    # assign quarter
    df["quarter"] = df["month"].map(MONTH_TO_QUARTER)

    # assign financial year
    df["financial_year"] = df["month"].map(MONTH_TO_FY)

    return df


def inspect_after(df: pd.DataFrame) -> None:
    """Display dataset info after cleaning."""
    print("\n-- After Cleaning --")
    print(f"Shape      : {df.shape}")
    print(f"Duplicates : {df.duplicated().sum()}")
    print(f"Missing    : {df.isnull().sum().sum()}")

    print("\nQuarter-wise Revenue:")
    quarter_revenue = df.groupby("quarter")["revenue"].sum().sort_index()
    for quarter, revenue in quarter_revenue.items():
        print(f"  {quarter}: Rs.{revenue:,}")

    print("\nSample Records:")
    print(df[["month", "product", "revenue", "profit", "profit_pct", "quarter"]].head().to_string(index=False))


def export(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned dataset to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved to {output_path}")


def main() -> None:
    df = load_data(INPUT_FILE)
    inspect(df)
    cleaned_df = clean(df)
    inspect_after(cleaned_df)
    export(cleaned_df, OUTPUT_FILE)


if __name__ == "__main__":
    main()