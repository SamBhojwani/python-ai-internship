"""
test_fixed_code.py
------------------
Tests to verify all bug fixes in fixed_code.py.

Run:
    python -m unittest tests/test_fixed_code.py
"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from fixed_code import (
    calculate_discount,
    get_top_earners,
    count_words_per_line,
    is_palindrome,
    calculate_compound_interest,
    find_common_elements,
)


class TestFixedCode(unittest.TestCase):

    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(1000, 20), 800.0)

    def test_calculate_discount_zero(self):
        self.assertEqual(calculate_discount(1000, 0), 1000.0)

    def test_get_top_earners(self):
        employees = [
            {"name": "Aman", "salary": 90000},
            {"name": "Bhumi", "salary": 75000},
            {"name": "Chaitanya", "salary": 95000},
            {"name": "Dhruv", "salary": 60000},
        ]
        top2 = get_top_earners(employees, 2)
        self.assertEqual(top2[0]["name"], "Chaitanya")
        self.assertEqual(top2[1]["name"], "Aman")

    def test_count_words_per_line(self):
        text = "hello world\nthis is a test\npython"
        self.assertEqual(count_words_per_line(text), [2, 4, 1])

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("Madam"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_calculate_compound_interest(self):
        result = calculate_compound_interest(1000, 0.1, 2)
        self.assertAlmostEqual(result, 1210.0, places=2)

    def test_find_common_elements(self):
        self.assertEqual(find_common_elements([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_find_common_elements_duplicates(self):
        self.assertEqual(find_common_elements([1, 1, 2], [1, 2, 2]), [1, 2])

    def test_find_common_elements_none(self):
        self.assertEqual(find_common_elements([1, 2], [3, 4]), [])


if __name__ == "__main__":
    unittest.main()