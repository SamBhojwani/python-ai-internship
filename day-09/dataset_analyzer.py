"""
dataset_analyzer.py
-------------------
A reusable DatasetAnalyzer class that works with any CSV dataset.

Usage:
    python dataset_analyzer.py
"""

import pandas as pd
import os


class DatasetAnalyzer:
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
        print(f"Columns: {list(self.df.columns)}")

    def dataset_summary(self) -> None:
        """Display a full summary of the dataset."""
        self._check_loaded()

        print("\n" + "=" * 50)
        print("          DATASET SUMMARY")
        print("=" * 50)
        print(f"Shape      : {self.df.shape[0]} rows x {self.df.shape[1]} columns")
        print(f"Duplicates : {self.df.duplicated().sum()}")

        print("\nColumn Types:")
        for col, dtype in self.df.dtypes.items():
            print(f"  {col:<20} {dtype}")

        print("\nStatistical Summary:")
        print(self.df.describe().to_string())
        print("=" * 50)

    def missing_values(self) -> None:
        """Display missing values per column."""
        self._check_loaded()

        print("\n" + "=" * 40)
        print("          MISSING VALUES")
        print("=" * 40)
        missing = self.df.isnull().sum()
        total_missing = missing.sum()

        if total_missing == 0:
            print("No missing values found.")
        else:
            for col, count in missing.items():
                pct = (count / len(self.df)) * 100
                print(f"  {col:<20} {count} missing ({pct:.1f}%)")
        print(f"\nTotal missing values: {total_missing}")
        print("=" * 40)

    def export_report(self, output_path: str) -> None:
        """
        Export dataset summary statistics to a CSV file.

        Args:
            output_path: Path to save the report CSV.
        """
        self._check_loaded()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        report = self.df.describe().reset_index()
        report.to_csv(output_path, index=False)
        print(f"\nReport exported to {output_path}")

    def _check_loaded(self) -> None:
        """Check if dataset is loaded before performing operations."""
        if self.df is None:
            raise RuntimeError("No dataset loaded. Call load_dataset() first.")


def main() -> None:
    analyzer = DatasetAnalyzer()

    print("-- Analyzing Employee Dataset --")
    analyzer.load_dataset("datasets/employees_day9.csv")
    analyzer.dataset_summary()
    analyzer.missing_values()
    analyzer.export_report("reports/employee_analyzer_report.csv")

    print("\n-- Analyzing Student Dataset --")
    analyzer.load_dataset("datasets/students_day9.csv")
    analyzer.dataset_summary()
    analyzer.missing_values()
    analyzer.export_report("reports/student_analyzer_report.csv")


if __name__ == "__main__":
    main()