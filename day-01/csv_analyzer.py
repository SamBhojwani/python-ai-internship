"""
csv_analyzer.py
---------------
Reads a CSV file and displays a summary:
  - Row and column count
  - Column names
  - Missing values per column

Usage:
    python csv_analyzer.py <path_to_csv>

Example:
    python csv_analyzer.py sample_data/sample.csv
"""

import sys
import logging
import pandas as pd

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the CSV data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty or cannot be parsed as CSV.
    """
    logger.info(f"Loading CSV file: {filepath}")
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("The CSV file is empty.")
        logger.info("CSV loaded successfully.")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except pd.errors.EmptyDataError:
        logger.error("The file has no data.")
        raise ValueError("CSV file contains no data.")
    except pd.errors.ParserError as e:
        logger.error(f"Failed to parse CSV: {e}")
        raise ValueError(f"CSV parsing error: {e}")


def analyze(df: pd.DataFrame) -> None:
    """
    Print a structured summary of the DataFrame.

    Args:
        df: The loaded pandas DataFrame.
    """
    print("\n" + "=" * 40)
    print("        CSV ANALYSIS REPORT")
    print("=" * 40)

    # Basic dimensions
    print(f"\nRows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    # Column names
    print("\nColumn Names:")
    for col in df.columns:
        print(f"  - {col}")

    # Missing values (only show columns that actually have missing values)
    missing = df.isnull().sum()
    missing_cols = missing[missing > 0]

    print("\nMissing Values:")
    if missing_cols.empty:
        print("  None — all columns are complete.")
    else:
        for col, count in missing_cols.items():
            pct = (count / len(df)) * 100
            print(f"  {col}: {count} missing ({pct:.1f}%)")

    print("\n" + "=" * 40 + "\n")


def main() -> None:
    """Entry point: parse CLI argument, load CSV, and run analysis."""
    if len(sys.argv) != 2:
        print("Usage: python csv_analyzer.py <path_to_csv>")
        sys.exit(1)

    filepath: str = sys.argv[1]

    try:
        df = load_csv(filepath)
        analyze(df)
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Analysis failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()