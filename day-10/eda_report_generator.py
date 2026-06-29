"""
eda_report_generator.py
-----------------------
A reusable EDAReportGenerator class that works with any CSV dataset.

Usage:
    python eda_report_generator.py
"""

import pandas as pd
import os


class EDAReportGenerator:
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

    def dataset_info(self) -> None:
        """Display basic dataset information."""
        self._check_loaded()

        print("\n" + "=" * 50)
        print("            DATASET INFO")
        print("=" * 50)
        print(f"File       : {self.filepath}")
        print(f"Rows       : {self.df.shape[0]}")
        print(f"Columns    : {self.df.shape[1]}")
        print(f"Duplicates : {self.df.duplicated().sum()}")
        print(f"Missing    : {self.df.isnull().sum().sum()}")

        print("\nColumns and Types:")
        for col, dtype in self.df.dtypes.items():
            missing = self.df[col].isnull().sum()
            print(f"  {col:<20} {str(dtype):<10} {missing} missing")
        print("=" * 50)

    def descriptive_statistics(self) -> None:
        """Display descriptive statistics for numeric columns."""
        self._check_loaded()

        numeric_df = self.df.select_dtypes(include="number")
        if numeric_df.empty:
            print("No numeric columns found.")
            return

        print("\n" + "=" * 50)
        print("        DESCRIPTIVE STATISTICS")
        print("=" * 50)
        print(numeric_df.describe().round(2).to_string())
        print("=" * 50)

    def group_analysis(self, group_col: str, value_col: str) -> None:
        """
        Perform group analysis on a dataset.

        Args:
            group_col: Column to group by.
            value_col: Numeric column to aggregate.

        Raises:
            ValueError: If columns don't exist in dataset.
        """
        self._check_loaded()

        if group_col not in self.df.columns:
            raise ValueError(f"Column '{group_col}' not found in dataset.")
        if value_col not in self.df.columns:
            raise ValueError(f"Column '{value_col}' not found in dataset.")

        print("\n" + "=" * 50)
        print(f"   GROUP ANALYSIS: {value_col} by {group_col}")
        print("=" * 50)

        grouped = self.df.groupby(group_col)[value_col].agg(
            count="count",
            mean="mean",
            max="max",
            min="min",
        ).round(2)

        print(grouped.to_string())
        print("=" * 50)

    def export_summary(self, output_path: str) -> None:
        """
        Export descriptive statistics to a CSV file.

        Args:
            output_path: Path to save the report.
        """
        self._check_loaded()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        summary = self.df.describe().round(2).reset_index()
        summary.to_csv(output_path, index=False)
        print(f"\nSummary exported to {output_path}")

    def _check_loaded(self) -> None:
        """Check if dataset is loaded before performing operations."""
        if self.df is None:
            raise RuntimeError("No dataset loaded. Call load_dataset() first.")


def main() -> None:
    eda = EDAReportGenerator()

    print("-- Employee Dataset EDA --")
    eda.load_dataset("datasets/employees_day9.csv")
    eda.dataset_info()
    eda.descriptive_statistics()
    eda.group_analysis("department", "salary")
    eda.export_summary("reports/eda_employee_report.csv")

    print("\n-- Sales Dataset EDA --")
    eda.load_dataset("datasets/sales_day10.csv")
    eda.dataset_info()
    eda.descriptive_statistics()
    eda.group_analysis("category", "revenue")
    eda.export_summary("reports/eda_sales_report.csv")


if __name__ == "__main__":
    main()