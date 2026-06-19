"""
file_analyzer.py
----------------
Reads a text file and displays a summary:
  - Number of lines
  - Number of words
  - Number of characters

Includes input validation and enhanced exception handling.

Usage:
    python file_analyzer.py <path_to_file>

Example:
    python file_analyzer.py data/sample.txt
"""

import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def validate_filepath(filepath: str) -> None:
    """
    Validate that the filepath points to a .txt file.

    Args:
        filepath: Path to validate.

    Raises:
        ValueError: If the file is not a .txt file.
    """
    if not filepath.endswith(".txt"):
        raise ValueError(f"Expected a .txt file, got: {filepath}")


def read_file(filepath: str) -> str:
    """
    Read and return the contents of a text file.

    Args:
        filepath: Path to the text file.

    Returns:
        File contents as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If the file encoding is not supported.
        ValueError: If the file is empty.
        OSError: If the file cannot be read.
    """
    logger.info(f"Reading file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if not content.strip():
            raise ValueError("The file is empty.")
        logger.info("File read successfully.")
        return content
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except UnicodeDecodeError:
        logger.error("File encoding not supported. Please use a UTF-8 encoded file.")
        raise
    except OSError as e:
        logger.error(f"Could not read file: {e}")
        raise


def analyze(content: str) -> dict:
    """
    Analyze text content and return line, word, and character counts.

    Args:
        content: Text content to analyze.

    Returns:
        Dict with keys: lines, words, characters.
    """
    return {
        "lines": len(content.splitlines()),
        "words": len(content.split()),
        "characters": len(content),
    }


def display_report(filepath: str, stats: dict) -> None:
    """
    Display the file analysis report.

    Args:
        filepath: Path to the analyzed file.
        stats: Dict containing lines, words, characters counts.
    """
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
    """Entry point: read file path from CLI and run analysis."""
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py <path_to_file>")
        sys.exit(1)

    filepath: str = sys.argv[1]

    try:
        validate_filepath(filepath)
        content = read_file(filepath)
        stats = analyze(content)
        display_report(filepath, stats)
    except ValueError as e:
        print(f"Validation error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)
    except UnicodeDecodeError:
        print("Error: File encoding not supported. Please use a UTF-8 encoded file.")
        sys.exit(1)
    except OSError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()