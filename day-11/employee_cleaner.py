"""
employee_cleaner.py
-------------------
Cleans and prepares the employee dataset for Machine Learning.
- Removes duplicates
- Fills missing salary values
- Standardizes department names
- Creates Annual Salary column

Usage:
    python employee_cleaner.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/raw/employees_day9.csv"
OUTPUT_FILE = "datasets/cleaned/employee_cleaned.csv"


def load_data(filepath: str) -> pd.DataFrame:
    """Load raw employee dataset."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records.")
    return df


def inspect(df: pd.DataFrame) -> None:
    """Display dataset info before cleaning."""
    print("\n-- Before Cleaning --")
    print(f"Shape      : {df.shape}")
    print(f"Duplicates : {df.duplicated().sum()}")
    print(f"Missing Values:")
    print(df.isnull().sum().to_string())


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the employee dataset.
    - Remove duplicates
    - Fill missing salary with mean
    - Standardize department names to title case
    - Standardize city names to title case
    - Create annual salary column
    """
    df = df.copy()

    # remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"\nRemoved {before - len(df)} duplicate(s).")

    # fill missing salary with mean
    if df["salary"].isnull().sum() > 0:
        mean_salary = df["salary"].mean()
        df["salary"] = df["salary"].fillna(round(mean_salary, 2))
        print(f"Filled missing salary values with mean: {mean_salary:,.2f}")

    # standardize department and city to title case
    df["department"] = df["department"].str.strip().str.title()
    df["department"] = df["department"].str.replace("Hr", "HR")
    df["city"] = df["city"].str.strip().str.title()
    df["name"] = df["name"].str.strip().str.title()

    # create annual salary column
    df["annual_salary"] = df["salary"] * 12

    # rename columns to lowercase
    df.columns = df.columns.str.lower()

    return df


def inspect_after(df: pd.DataFrame) -> None:
    """Display dataset info after cleaning."""
    print("\n-- After Cleaning --")
    print(f"Shape      : {df.shape}")
    print(f"Duplicates : {df.duplicated().sum()}")
    print(f"Missing    : {df.isnull().sum().sum()}")
    print("\nSample Records:")
    print(df.head().to_string(index=False))


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