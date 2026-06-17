"""
json_formatter.py
-----------------
Reads a JSON file and pretty-prints its contents.
Handles invalid JSON and missing files gracefully.

Usage:
    python json_formatter.py <path_to_json>

Example:
    python json_formatter.py sample_data/sample.json
"""

import sys
import json
import logging

# --- Logging Setup ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def load_json(filepath: str) -> dict | list:
    """
    Load and parse a JSON file.

    Args:
        filepath: Path to the JSON file.

    Returns:
        Parsed JSON content as a Python dict or list.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    logger.info(f"Reading JSON file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info("JSON loaded and parsed successfully.")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON at line {e.lineno}, column {e.colno}: {e.msg}")
        raise


def pretty_print(data: dict | list) -> None:
    """
    Pretty-print JSON data to stdout with 4-space indentation.

    Args:
        data: Parsed JSON data (dict or list).
    """
    print("\n" + "=" * 40)
    print("       FORMATTED JSON OUTPUT")
    print("=" * 40 + "\n")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    print("\n" + "=" * 40 + "\n")


def main() -> None:
    """Entry point: parse CLI argument, load JSON, and format output."""
    if len(sys.argv) != 2:
        print("Usage: python json_formatter.py <path_to_json>")
        sys.exit(1)

    filepath: str = sys.argv[1]

    try:
        data = load_json(filepath)
        pretty_print(data)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON — {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()