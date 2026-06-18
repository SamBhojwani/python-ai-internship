"""
utils.py
--------
A reusable utility module with string, number, and list helper functions.

Import example:
    from utils import word_count, is_prime, find_max
"""


# ── String Utilities ──────────────────────────────────────────


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    Args:
        text: Input string.

    Returns:
        String with each word capitalized.

    Raises:
        ValueError: If text is empty or whitespace only.
    """
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")
    return text.title()


def reverse_text(text: str) -> str:
    """
    Reverse the characters in a string.

    Args:
        text: Input string.

    Returns:
        Reversed string.

    Raises:
        ValueError: If text is empty or whitespace only.
    """
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")
    return text[::-1]


def word_count(text: str) -> int:
    """
    Count the number of words in a string.

    Args:
        text: Input string.

    Returns:
        Number of words. Returns 0 for empty input.
    """
    if not text or not text.strip():
        return 0
    return len(text.split())


# ── Number Utilities ──────────────────────────────────────────


def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    Args:
        number: Integer to check.

    Returns:
        True if prime, False otherwise.

    Raises:
        ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Prime check not defined for negative numbers.")
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def factorial(number: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Args:
        number: Non-negative integer.

    Returns:
        Factorial of the number.

    Raises:
        ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: List of numeric values.

    Returns:
        Average as a float.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum(numbers) / len(numbers)


# ── List Utilities ────────────────────────────────────────────


def remove_duplicates(items: list) -> list:
    """
    Remove duplicate values from a list while preserving order.

    Args:
        items: Input list.

    Returns:
        New list with duplicates removed.

    Raises:
        ValueError: If the list is empty.
    """
    if not items:
        raise ValueError("Input list cannot be empty.")
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def find_max(items: list) -> float:
    """
    Find the maximum value in a list.

    Args:
        items: Input list of numbers.

    Returns:
        Maximum value.

    Raises:
        ValueError: If the list is empty.
    """
    if not items:
        raise ValueError("Cannot find max of an empty list.")
    return max(items)


def find_min(items: list) -> float:
    """
    Find the minimum value in a list.

    Args:
        items: Input list of numbers.

    Returns:
        Minimum value.

    Raises:
        ValueError: If the list is empty.
    """
    if not items:
        raise ValueError("Cannot find min of an empty list.")
    return min(items)