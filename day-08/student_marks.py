"""
student_marks.py
----------------
Analyzes student marks using NumPy.

Usage:
    python student_marks.py
"""

import numpy as np

# Student data
students = [
    "Aman", "Bhumi", "Chaitanya", "Dhruv", "Ekta",
    "Farhan", "Geeta", "Harish", "Isha", "Jay"
]

marks = np.array([81, 56, 84, 42, 96, 73, 68, 91, 75, 62])

# Calculations
highest = marks.max()
lowest = marks.min()
average = marks.mean()
median = np.median(marks)
above_average = marks[marks > average]
above_average_students = [students[i] for i in range(len(marks)) if marks[i] > average]

# Display
print("\n" + "=" * 40)
print("     STUDENT MARKS ANALYSIS REPORT")
print("=" * 40)
print(f"Highest Marks : {highest}")
print(f"Lowest Marks  : {lowest}")
print(f"Average Marks : {average:.1f}")
print(f"Median Marks  : {median:.1f}")
print("\nStudents Above Average:")
for name, mark in zip(above_average_students, above_average):
    print(f"  {name:<15} {mark}")
print("=" * 40 + "\n")