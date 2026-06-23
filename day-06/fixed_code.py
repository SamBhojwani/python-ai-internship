"""
fixed_code.py
-------------
Fixed version of buggy_code.py with documented bug fixes.
"""


def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Return the final price after applying a discount.

    Fix: discount_percent must be divided by 100 before multiplying.
    e.g. 20% discount = price * 0.20, not price * 20
    """
    discount = price * (discount_percent / 100)
    return price - discount


def get_top_earners(employees: list[dict], n: int) -> list[dict]:
    """
    Return top n highest paid employees.

    Fix: sorted() defaults to ascending order so [:n] was returning
    the lowest earners. Added reverse=True to sort descending.
    """
    sorted_employees = sorted(employees, key=lambda e: e["salary"], reverse=True)
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
    """
    Calculate compound interest and return total amount.

    Fix: ^ is the XOR operator in Python, not exponentiation.
    Changed ^ to ** for correct power calculation.
    """
    return principal * (1 + rate) ** years


def find_common_elements(list1: list, list2: list) -> list:
    """
    Return elements that appear in both lists.

    Fix: removing items from list2 while using it for lookup
    caused incorrect results with duplicates. Using a Counter
    to track occurrences correctly.
    """
    from collections import Counter
    count = Counter(list2)
    result = []
    for item in list1:
        if count.get(item, 0) > 0:
            result.append(item)
            count[item] -= 1
    return result