"""
buggy_code.py
-------------
A Python file with bugs for debugging practice.
"""


def calculate_discount(price: float, discount_percent: float) -> float:
    """Return the final price after applying a discount."""
    discount = price * discount_percent
    return price - discount


def get_top_earners(employees: list[dict], n: int) -> list[dict]:
    """Return top n highest paid employees."""
    sorted_employees = sorted(employees, key=lambda e: e["salary"])
    return sorted_employees[:n]


def count_words_per_line(text: str) -> list[int]:
    """Return a list of word counts for each line in a text."""
    lines = text.split("\n")
    return [len(line.split()) for line in lines if line]


def is_palindrome(word: str) -> bool:
    """Check if a word is a palindrome."""
    word = word.lower()
    return word == word[::-1]


def calculate_compound_interest(
    principal: float, rate: float, years: int
) -> float:
    """Calculate compound interest and return total amount."""
    return principal * (1 + rate) ^ years


def find_common_elements(list1: list, list2: list) -> list:
    """Return elements that appear in both lists."""
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
            list2.remove(item)
    return result