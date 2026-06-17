"""
csv_to_json.py
--------------
Reads a CSV file and converts it to a JSON file.
Includes logging, type hints, and full exception handling.

Usage:
    python csv_to_json.py <input_csv> <output_json>

Example:
    python csv_to_json.py sample_data/sample.csv sample_data/output.json
"""

import sys
import json
import logging
import pandas as pd

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def csv_to_dict(filepath: str) -> list[dict]:
    """
    Read a CSV file and return its contents as a list of row dictionaries.

    Args:
        filepath: Path to the input CSV file.

    Returns:
        A list of dicts where each dict represents one row.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If the CSV file is empty or unparseable.
    """
    logger.info(f"Reading CSV: {filepath}")
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("CSV file is empty.")
        # Replace NaN with None so JSON serialization produces null, not NaN.
        # We use object dtype conversion because pandas NaN is a float and
        # json.dumps does not support NaN natively.
        records: list[dict] = (
            df.astype(object).where(pd.notnull(df), other=None).to_dict(orient="records")
        )
        logger.info(f"Parsed {len(records)} rows from CSV.")
        return records
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file contains no data.")
    except pd.errors.ParserError as e:
        raise ValueError(f"CSV parsing error: {e}")


def save_json(data: list[dict], output_path: str) -> None:
    """
    Serialize data to a JSON file with pretty formatting.

    Args:
        data: List of row dictionaries to serialize.
        output_path: Destination path for the JSON output file.

    Raises:
        OSError: If the file cannot be written.
    """
    logger.info(f"Writing JSON to: {output_path}")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"JSON saved successfully: {output_path}")
    except OSError as e:
        logger.error(f"Failed to write file: {e}")
        raise


def main() -> None:
    """Entry point: read CSV and write converted JSON output."""
    if len(sys.argv) != 3:
        print("Usage: python csv_to_json.py <input_csv> <output_json>")
        sys.exit(1)

    input_csv: str = sys.argv[1]
    output_json: str = sys.argv[2]

    try:
        records = csv_to_dict(input_csv)
        save_json(records, output_json)
        print(f"\nDone. {len(records)} rows written to '{output_json}'.\n")
    except (FileNotFoundError, ValueError, OSError) as e:
        logger.error(f"Conversion failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()