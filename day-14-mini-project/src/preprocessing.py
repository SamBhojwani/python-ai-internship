"""
preprocessing.py
----------------
Handles data loading, inspection and cleaning for the
Employee Salary Prediction System.
"""

import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)


def load_raw_data(filepath: str) -> pd.DataFrame:
    """
    Load raw employee dataset.

    Args:
        filepath: Path to the raw CSV file.

    Returns:
        Raw DataFrame.

    Raises:
        FileNotFoundError: If file does not exist.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(filepath)
    logger.info(f"Loaded {len(df)} records from {filepath}")
    return df


def inspect_dataset(df: pd.DataFrame) -> None:
    """Display dataset overview before cleaning."""
    print("\n" + "=" * 55)
    print("            DATASET OVERVIEW")
    print("=" * 55)
    print(f"Shape          : {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"Duplicate Rows : {df.duplicated().sum()}")
    print(f"Total Missing  : {df.isnull().sum().sum()}")

    print("\nColumn Info:")
    for col in df.columns:
        dtype = df[col].dtype
        missing = df[col].isnull().sum()
        print(f"  {col:<20} {str(dtype):<10} {missing} missing")

    print("\nStatistical Summary:")
    print(df.describe().round(2).to_string())
    print("=" * 55)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the employee dataset.
    - Remove duplicates
    - Fill missing numeric values with mean
    - Fill missing string values with Unknown
    - Standardize text columns

    Args:
        df: Raw DataFrame.

    Returns:
        Cleaned DataFrame.
    """
    df = df.copy()

    # remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    logger.info(f"Removed {before - len(df)} duplicate(s).")

    # fill missing numeric values with mean
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            mean_val = df[col].mean()
            df[col] = df[col].fillna(round(mean_val, 2))
            logger.info(f"Filled missing '{col}' with mean: {mean_val:.2f}")

    # fill missing string values with Unknown
    string_cols = df.select_dtypes(include="str").columns
    for col in string_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna("Unknown")

    # standardize text columns
    df["name"] = df["name"].str.strip().str.title()
    df["department"] = df["department"].str.strip().str.title()
    df["department"] = df["department"].str.replace("Hr", "HR")
    df["city"] = df["city"].str.strip().str.title()

    logger.info("Data cleaning complete.")
    return df


def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned dataset to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.info(f"Cleaned dataset saved to {output_path}")