"""
log_analyzer.py
---------------
Reads a log file and counts INFO, WARNING, and ERROR entries.
Generates a summary report.

Usage:
    python log_analyzer.py <path_to_log>

Example:
    python log_analyzer.py app.log
"""

import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def read_log(filepath: str) -> list[str]:
    """
    Read a log file and return its lines.

    Args:
        filepath: Path to the log file.

    Returns:
        List of log lines.

    Raises:
        FileNotFoundError: If the log file does not exist.
        ValueError: If the log file is empty.
    """
    logger.info(f"Reading log file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            raise ValueError("Log file is empty.")
        logger.info(f"Read {len(lines)} log entries.")
        return lines
    except FileNotFoundError:
        logger.error(f"Log file not found: {filepath}")
        raise


def analyze_log(lines: list[str]) -> dict:
    """
    Count INFO, WARNING and ERROR entries in log lines.

    Args:
        lines: List of log lines.

    Returns:
        Dict with counts for each log level.
    """
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "OTHER": 0}

    for line in lines:
        if "[INFO]" in line:
            counts["INFO"] += 1
        elif "[WARNING]" in line:
            counts["WARNING"] += 1
        elif "[ERROR]" in line:
            counts["ERROR"] += 1
        else:
            counts["OTHER"] += 1

    return counts


def display_report(filepath: str, counts: dict) -> None:
    """Print the log analysis report."""
    total = sum(counts.values())

    print("\n" + "=" * 35)
    print("      LOG ANALYSIS REPORT")
    print("=" * 35)
    print(f"File    : {filepath}")
    print(f"Total   : {total} entries")
    print("-" * 35)
    print(f"INFO    : {counts['INFO']}")
    print(f"WARNING : {counts['WARNING']}")
    print(f"ERROR   : {counts['ERROR']}")
    if counts["OTHER"] > 0:
        print(f"OTHER   : {counts['OTHER']}")
    print("=" * 35 + "\n")


def main() -> None:
    """Entry point: read log file path from CLI and run analysis."""
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <path_to_log>")
        sys.exit(1)

    filepath: str = sys.argv[1]

    try:
        lines = read_log(filepath)
        counts = analyze_log(lines)
        display_report(filepath, counts)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()