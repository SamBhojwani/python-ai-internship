"""
test_utils.py
-------------
Tests for all functions in utils.py.

Usage:
    python test_utils.py
"""

from utils import (
    capitalize_words,
    reverse_text,
    word_count,
    is_prime,
    factorial,
    average,
    remove_duplicates,
    find_max,
    find_min,
)


def test_string_utilities() -> None:
    """Test all string utility functions."""
    print("── String Utilities ──")

    # capitalize_words
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is great") == "Python Is Great"
    print("capitalize_words: PASSED")

    # reverse_text
    assert reverse_text("hello") == "olleh"
    assert reverse_text("python") == "nohtyp"
    print("reverse_text    : PASSED")

    # word_count
    assert word_count("hello world") == 2
    assert word_count("one two three four") == 4
    assert word_count("") == 0
    assert word_count("   ") == 0
    print("word_count      : PASSED")


def test_number_utilities() -> None:
    """Test all number utility functions."""
    print("\n── Number Utilities ──")

    # is_prime
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(9) == False
    print("is_prime  : PASSED")

    # factorial
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720
    print("factorial : PASSED")

    # average
    assert average([1, 2, 3, 4, 5]) == 3.0
    assert average([10, 20]) == 15.0
    print("average   : PASSED")


def test_list_utilities() -> None:
    """Test all list utility functions."""
    print("\n── List Utilities ──")

    # remove_duplicates
    assert remove_duplicates([1, 2, 2, 3, 3]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
    print("remove_duplicates : PASSED")

    # find_max
    assert find_max([3, 1, 4, 1, 5, 9]) == 9
    assert find_max([100, 200, 50]) == 200
    print("find_max          : PASSED")

    # find_min
    assert find_min([3, 1, 4, 1, 5, 9]) == 1
    assert find_min([100, 200, 50]) == 50
    print("find_min          : PASSED")


def test_edge_cases() -> None:
    """Test edge cases and error handling."""
    print("\n── Edge Cases ──")

    # word_count with empty string
    assert word_count("") == 0
    print("word_count empty string : PASSED")

    # factorial of 0
    assert factorial(0) == 1
    print("factorial(0)            : PASSED")

    # is_prime with 0 and 1
    assert is_prime(0) == False
    assert is_prime(1) == False
    print("is_prime(0) and (1)     : PASSED")

    # ValueError for empty list
    try:
        find_max([])
        print("find_max empty list     : FAILED")
    except ValueError:
        print("find_max empty list     : PASSED")

    try:
        average([])
        print("average empty list      : FAILED")
    except ValueError:
        print("average empty list      : PASSED")


def main() -> None:
    print("=" * 40)
    print("     UTILS MODULE TEST RESULTS")
    print("=" * 40)
    test_string_utilities()
    test_number_utilities()
    test_list_utilities()
    test_edge_cases()
    print("\n" + "=" * 40)
    print("All tests passed!")
    print("=" * 40)


if __name__ == "__main__":
    main()