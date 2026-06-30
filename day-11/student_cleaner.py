"""
student_cleaner.py
------------------
Cleans and prepares the student dataset for Machine Learning.
- Removes duplicates
- Handles missing marks
- Calculates total marks and percentage
- Assigns grades

Usage:
    python3 student_cleaner.py
"""

import pandas as pd
import os

INPUT_FILE = "datasets/raw/students_day9.csv"
OUTPUT_FILE = "datasets/cleaned/student_cleaned.csv"

SUBJECTS = ["math", "science", "english", "history"]
MAX_MARKS_PER_SUBJECT = 100
TOTAL_MAX_MARKS = MAX_MARKS_PER_SUBJECT * len(SUBJECTS)


def load_data(filepath: str) -> pd.DataFrame:
    """Load raw student dataset."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records.")
    return df


def inspect(df: pd.DataFrame) -> None:
    """Display dataset info before cleaning."""
    print("\n-- Before Cleaning --")
    print(f"Shape      : {df.shape}")
    print(f"Duplicates : {df.duplicated().sum()}")
    print("Missing Values:")
    print(df.isnull().sum().to_string())


def assign_grade(percentage: float) -> str:
    """
    Assign grade based on percentage.

    A: 90+
    B: 80-89
    C: 70-79
    D: 60-69
    F: Below 60
    """
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare the student dataset.
    - Remove duplicates
    - Fill missing marks with subject mean
    - Calculate total marks
    - Calculate percentage
    - Assign grade
    """
    df = df.copy()

    # remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"\nRemoved {before - len(df)} duplicate(s).")

    # fill missing marks with subject mean
    for subject in SUBJECTS:
        if df[subject].isnull().sum() > 0:
            mean_val = df[subject].mean()
            df[subject] = df[subject].fillna(round(mean_val, 2))
            print(f"Filled missing {subject} marks with mean: {mean_val:.2f}")

    # standardize name to title case
    df["name"] = df["name"].str.strip().str.title()

    # calculate total marks and percentage
    df["total_marks"] = df[SUBJECTS].sum(axis=1)
    df["percentage"] = ((df["total_marks"] / TOTAL_MAX_MARKS) * 100).round(2)

    # assign grade
    df["grade"] = df["percentage"].apply(assign_grade)

    return df


def inspect_after(df: pd.DataFrame) -> None:
    """Display dataset info after cleaning."""
    print("\n-- After Cleaning --")
    print(f"Shape      : {df.shape}")
    print(f"Duplicates : {df.duplicated().sum()}")
    print(f"Missing    : {df.isnull().sum().sum()}")

    print("\nGrade Distribution:")
    grade_counts = df["grade"].value_counts().sort_index()
    for grade, count in grade_counts.items():
        print(f"  Grade {grade}: {count} student(s)")

    print("\nSample Records:")
    print(df[["name", "total_marks", "percentage", "grade"]].head().to_string(index=False))


def export(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned dataset to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved to {output_path}")


def main() -> None:
    df = load_data(INPUT_FILE)
    inspect(df)
    cleaned_df = clean(df)
    inspect_after(cleaned_df)
    export(cleaned_df, OUTPUT_FILE)


if __name__ == "__main__":
    main()