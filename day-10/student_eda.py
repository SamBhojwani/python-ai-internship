"""
student_eda.py
--------------
Exploratory Data Analysis on student performance dataset.
Exports summary report to CSV.

Usage:
    python student_eda.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/students_day9.csv"
REPORT_FILE = "reports/student_summary.csv"


def load_data(filepath: str) -> pd.DataFrame:
    """Load student dataset and calculate average marks."""
    df = pd.read_csv(filepath)
    df["average"] = df[["math", "science", "english", "history"]].mean(axis=1).round(2)
    print(f"Loaded {len(df)} student records.")
    return df


def analyze(df: pd.DataFrame) -> None:
    """Perform EDA and display student performance insights."""

    subjects = ["math", "science", "english", "history"]
    top = df.loc[df["average"].idxmax()]
    lowest = df.loc[df["average"].idxmin()]
    above_80 = df[df["average"] >= 80]
    below_40 = df[df["average"] < 40]

    print("\n" + "=" * 55)
    print("        STUDENT PERFORMANCE REPORT")
    print("=" * 55)

    print(f"\nTotal Students   : {len(df)}")
    print(f"Class Average    : {df['average'].mean():.2f}%")
    print(f"Top Performer    : {top['name']} - {top['average']}%")
    print(f"Lowest Performer : {lowest['name']} - {lowest['average']}%")

    # Subject-wise averages
    print("\nSubject-wise Average:")
    for subject in subjects:
        print(f"  {subject.capitalize():<12} {df[subject].mean():.2f}%")

    # Subject-wise highest scorer
    print("\nSubject-wise Top Scorer:")
    for subject in subjects:
        top_student = df.loc[df[subject].idxmax()]
        print(f"  {subject.capitalize():<12} {top_student['name']} - {top_student[subject]}")

    # Above 80%
    print(f"\nStudents Above 80% ({len(above_80)}):")
    for _, row in above_80.sort_values("average", ascending=False).iterrows():
        print(f"  {row['name']:<20} {row['average']}%")

    # Below 40%
    print(f"\nFailing Students - Below 40% ({len(below_40)}):")
    if below_40.empty:
        print("  None")
    else:
        for _, row in below_40.iterrows():
            print(f"  {row['name']:<20} {row['average']}%")

    print("=" * 55)


def export_report(df: pd.DataFrame, output_path: str) -> None:
    """Export student summary to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    subjects = ["math", "science", "english", "history", "average"]
    summary = df[["name"] + subjects].sort_values("average", ascending=False)
    summary.to_csv(output_path, index=False)
    print(f"\nReport exported to {output_path}")


def main() -> None:
    df = load_data(INPUT_FILE)
    analyze(df)
    export_report(df, REPORT_FILE)


if __name__ == "__main__":
    main()