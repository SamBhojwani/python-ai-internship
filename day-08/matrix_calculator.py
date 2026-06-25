"""
matrix_calculator.py
--------------------
Performs matrix operations using NumPy.

Usage:
    python matrix_calculator.py
"""

import numpy as np

# Define two matrices
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])


def display_matrix(label: str, matrix: np.ndarray) -> None:
    """Display a matrix with a label."""
    print(f"\n{label}:")
    print(matrix)


def main() -> None:
    print("\n" + "=" * 40)
    print("        MATRIX CALCULATOR")
    print("=" * 40)

    display_matrix("Matrix A", A)
    display_matrix("Matrix B", B)

    display_matrix("Addition (A + B)", A + B)
    display_matrix("Subtraction (A - B)", A - B)
    display_matrix("Multiplication (A × B)", np.dot(A, B))
    display_matrix("Transpose of A", A.T)
    display_matrix("Transpose of B", B.T)

    print("\n" + "=" * 40 + "\n")


if __name__ == "__main__":
    main()