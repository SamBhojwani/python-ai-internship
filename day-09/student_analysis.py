"""
student_analysis.py
-------------------
Analyzes student performance dataset using Pandas.

Usage:
    python student_analysis.py
"""

import pandas as pd

INPUT_FILE = "datasets/students_day9.csv"


def load_data(filepath: str) -> pd.DataFrame:
    """Load student dataset and calculate average marks."""
    df = pd.read_csv(filepath)
    df["average"] = df[["math", "science", "english", "history"]].mean(axis=1).round(2)
    print(f"Loaded {len(df)} student records.")
    return df


def analyze(df: pd.DataFrame) -> None:
    """Generate and display student performance report."""

    highest = df.loc[df["average"].idxmax()]
    lowest = df.loc[df["average"].idxmin()]
    above_80 = df[df["average"] >= 80]
    failing = df[df["average"] < 40]

    print("\n" + "=" * 55)
    print("        STUDENT PERFORMANCE ANALYSIS REPORT")
    print("=" * 55)

    print(f"\nTotal Students   : {len(df)}")
    print(f"Class Average    : {df['average'].mean():.2f}%")
    print(f"Highest Scorer   : {highest['name']} - {highest['average']}%")
    print(f"Lowest Scorer    : {lowest['name']} - {lowest['average']}%")

    print(f"\nStudents Scoring Above 80% ({len(above_80)}):")
    for _, row in above_80.iterrows():
        print(f"  {row['name']:<20} {row['average']}%")

    print(f"\nFailing Students - Below 40% ({len(failing)}):")
    if failing.empty:
        print("  None")
    else:
        for _, row in failing.iterrows():
            print(f"  {row['name']:<20} {row['average']}%")

    print("\nFull Results (sorted by average):")
    print("-" * 55)
    sorted_df = df[["name", "math", "science", "english", "history", "average"]].sort_values(
        by="average", ascending=False
    )
    print(sorted_df.to_string(index=False))
    print("=" * 55)


def main() -> None:
    df = load_data(INPUT_FILE)
    analyze(df)


if __name__ == "__main__":
    main()