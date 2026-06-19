"""
file_analyzer.py
----------------
Reads a text file and displays a summary:
  - Number of lines
  - Number of words
  - Number of characters

Usage:
    python file_analyzer.py <path_to_file>
"""

import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def read_file(filepath: str) -> str:
    """Read and return the contents of a text file."""
    logger.info(f"Reading file: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    logger.info("File read successfully.")
    return content


def analyze(content: str) -> dict:
    """Analyze text content and return line, word, and character counts."""
    return {
        "lines": len(content.splitlines()),
        "words": len(content.split()),
        "characters": len(content),
    }


def display_report(filepath: str, stats: dict) -> None:
    """Display the file analysis report."""
    print("\n" + "=" * 35)
    print("     FILE ANALYSIS REPORT")
    print("=" * 35)
    print(f"File       : {filepath}")
    print("-" * 35)
    print(f"Lines      : {stats['lines']}")
    print(f"Words      : {stats['words']}")
    print(f"Characters : {stats['characters']}")
    print("=" * 35 + "\n")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py <path_to_file>")
        sys.exit(1)

    filepath: str = sys.argv[1]
    content = read_file(filepath)
    stats = analyze(content)
    display_report(filepath, stats)


if __name__ == "__main__":
    main()