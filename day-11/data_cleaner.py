"""
data_cleaner.py
---------------
A reusable DataCleaner class that works with any CSV dataset.

Usage:
    python3 data_cleaner.py
"""

import pandas as pd
import os


class DataCleaner:
    def __init__(self):
        self.df: pd.DataFrame = None
        self.filepath: str = None

    def load_dataset(self, filepath: str) -> None:
        """
        Load a CSV dataset.

        Args:
            filepath: Path to the CSV file.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is empty.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        self.df = pd.read_csv(filepath)
        self.filepath = filepath

        if self.df.empty:
            raise ValueError("Dataset is empty.")

        print(f"Loaded {len(self.df)} records with {len(self.df.columns)} columns.")

    def remove_duplicates(self) -> None:
        """Remove duplicate rows from the dataset."""
        self._check_loaded()
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        removed = before - len(self.df)
        print(f"Removed {removed} duplicate(s). Remaining: {len(self.df)} records.")

    def handle_missing_values(self) -> None:
        """
        Handle missing values:
        - Fill numeric columns with column mean
        - Fill string columns with 'Unknown'
        """
        self._check_loaded()
        total_missing = self.df.isnull().sum().sum()

        if total_missing == 0:
            print("No missing values found.")
            return

        # fill numeric columns with mean
        numeric_cols = self.df.select_dtypes(include="number").columns
        for col in numeric_cols:
            if self.df[col].isnull().sum() > 0:
                mean_val = self.df[col].mean()
                self.df[col] = self.df[col].fillna(round(mean_val, 2))
                print(f"Filled '{col}' missing values with mean: {mean_val:.2f}")

        # fill string columns with Unknown
        string_cols = self.df.select_dtypes(include="str").columns
        for col in string_cols:
            if self.df[col].isnull().sum() > 0:
                self.df[col] = self.df[col].fillna("Unknown")
                print(f"Filled '{col}' missing values with 'Unknown'")

    def normalize_columns(self) -> None:
        """
        Normalize column names and string values:
        - Column names to lowercase with underscores
        - String values to title case
        """
        self._check_loaded()

        # normalize column names
        self.df.columns = self.df.columns.str.lower().str.replace(" ", "_")
        print("Column names normalized to lowercase.")

        # normalize string values to title case
        string_cols = self.df.select_dtypes(include="str").columns
        for col in string_cols:
            self.df[col] = self.df[col].str.strip().str.title()
        print(f"String values normalized to title case in {len(string_cols)} column(s).")

    def feature_engineering(self, operations: list[dict]) -> None:
        """
        Create new columns based on provided operations.

        Args:
            operations: List of dicts with keys:
                - new_col: Name of the new column
                - formula: Lambda function to apply

        Example:
            operations = [
                {"new_col": "annual_salary", "formula": lambda df: df["salary"] * 12}
            ]
        """
        self._check_loaded()

        for op in operations:
            col_name = op["new_col"]
            formula = op["formula"]
            self.df[col_name] = formula(self.df)
            print(f"Created new column: '{col_name}'")

    def export_dataset(self, output_path: str) -> None:
        """
        Export cleaned dataset to CSV.

        Args:
            output_path: Path to save the cleaned CSV.
        """
        self._check_loaded()
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path, index=False)
        print(f"Dataset exported to {output_path}")

    def summary(self) -> None:
        """Display current dataset summary."""
        self._check_loaded()
        print(f"\nShape      : {self.df.shape}")
        print(f"Duplicates : {self.df.duplicated().sum()}")
        print(f"Missing    : {self.df.isnull().sum().sum()}")
        print("\nSample:")
        print(self.df.head(3).to_string(index=False))

    def _check_loaded(self) -> None:
        """Check if dataset is loaded."""
        if self.df is None:
            raise RuntimeError("No dataset loaded. Call load_dataset() first.")


def main() -> None:
    cleaner = DataCleaner()

    print("-- Cleaning Employee Dataset --")
    cleaner.load_dataset("datasets/raw/employees_day9.csv")
    cleaner.remove_duplicates()
    cleaner.handle_missing_values()
    cleaner.normalize_columns()
    cleaner.feature_engineering([
        {"new_col": "annual_salary", "formula": lambda df: df["salary"] * 12},
    ])
    cleaner.summary()
    cleaner.export_dataset("datasets/cleaned/employee_data_cleaner.csv")

    print("\n-- Cleaning Sales Dataset --")
    cleaner.load_dataset("datasets/raw/sales_day10.csv")
    cleaner.remove_duplicates()
    cleaner.handle_missing_values()
    cleaner.normalize_columns()
    cleaner.feature_engineering([
        {"new_col": "profit", "formula": lambda df: df["revenue"] - (df["units_sold"] * df["unit_price"] * 0.7)},
        {"new_col": "profit_pct", "formula": lambda df: ((df["profit"] / df["revenue"]) * 100).round(2)},
    ])
    cleaner.summary()
    cleaner.export_dataset("datasets/cleaned/sales_data_cleaner.csv")


if __name__ == "__main__":
    main()