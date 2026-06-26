"""
dataset_cleaner.py
------------------
Cleans a messy dataset by handling missing values,
filling numeric gaps and removing duplicates.

Usage:
    python dataset_cleaner.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/messy_data_day9.csv"
OUTPUT_FILE = "reports/cleaned_dataset.csv"


def load_data(filepath: str) -> pd.DataFrame:
    """Load messy dataset from CSV."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records from {filepath}")
    return df


def inspect(df: pd.DataFrame) -> None:
    """Display missing values and duplicates before cleaning."""
    print("\n-- Before Cleaning --")
    print(f"Shape            : {df.shape}")
    print(f"Duplicate Rows   : {df.duplicated().sum()}")
    print("\nMissing Values:")
    missing = df.isnull().sum()
    for col, count in missing.items():
        if count > 0:
            print(f"  {col:<15} {count} missing")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset:
    - Fill missing numeric values with column average
    - Fill missing string values with 'Unknown'
    - Remove duplicate rows
    """
    df = df.copy()

    # fill missing numeric values with column mean
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        mean_val = df[col].mean()
        df[col] = df[col].fillna(round(mean_val, 2))

    # fill missing string values with Unknown
    string_cols = df.select_dtypes(include="object").columns
    for col in string_cols:
        df[col] = df[col].fillna("Unknown")

    # remove duplicate rows
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"\nRemoved {before - after} duplicate row(s).")

    return df


def inspect_after(df: pd.DataFrame) -> None:
    """Display dataset info after cleaning."""
    print("\n-- After Cleaning --")
    print(f"Shape            : {df.shape}")
    print(f"Duplicate Rows   : {df.duplicated().sum()}")
    print(f"Missing Values   : {df.isnull().sum().sum()}")
    print("\nCleaned Dataset:")
    print(df.to_string(index=False))


def save_cleaned(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned dataset to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved to {output_path}")


def main() -> None:
    df = load_data(INPUT_FILE)
    inspect(df)
    cleaned_df = clean(df)
    inspect_after(cleaned_df)
    save_cleaned(cleaned_df, OUTPUT_FILE)


if __name__ == "__main__":
    main()