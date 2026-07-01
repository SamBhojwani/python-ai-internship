"""
ml_pipeline.py
--------------
A reusable ML pipeline script that performs the full
machine learning workflow for any dataset.

Usage:
    python3 ml_pipeline.py
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder


def load_dataset(filepath: str) -> pd.DataFrame:
    """Load a CSV dataset."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records with {len(df.columns)} columns.")
    return df


def preprocess(df: pd.DataFrame, feature_cols: list[str], target_col: str) -> tuple:
    """
    Prepare features and target.
    Automatically encodes string columns using LabelEncoder.

    Args:
        df: Input DataFrame.
        feature_cols: List of feature column names.
        target_col: Target column name.

    Returns:
        Tuple of (X, y)
    """
    df = df.copy()

    for col in feature_cols:
        if df[col].dtype == "object" or pd.api.types.is_string_dtype(df[col]):
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            print(f"Encoded column: '{col}'")

    X = df[feature_cols]
    y = df[target_col]

    return X, y


def split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2) -> tuple:
    """
    Split data into training and testing sets.

    Args:
        X: Features DataFrame.
        y: Target Series.
        test_size: Proportion of data for testing.

    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """
    Train a Linear Regression model.

    Args:
        X_train: Training features.
        y_train: Training target.

    Returns:
        Trained LinearRegression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Model trained successfully.")
    return model


def evaluate(model: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series) -> None:
    """
    Evaluate model performance and display results.

    Args:
        model: Trained model.
        X_test: Test features.
        y_test: Actual target values.
    """
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("\n" + "=" * 50)
    print("          MODEL EVALUATION RESULTS")
    print("=" * 50)
    print(f"  MAE  : {mae:.2f}")
    print(f"  RMSE : {rmse:.2f}")
    print(f"  R2   : {r2:.4f}")

    print(f"\nActual vs Predicted:")
    print(f"{'Actual':>15} {'Predicted':>15} {'Difference':>15}")
    print("-" * 48)
    for actual, predicted in zip(y_test, predictions):
        diff = actual - predicted
        print(f"{actual:>15.2f} {predicted:>15.2f} {diff:>+15.2f}")
    print("=" * 50)


def run_pipeline(
    filepath: str,
    feature_cols: list[str],
    target_col: str,
    test_size: float = 0.2,
) -> None:
    """
    Run the full ML pipeline.

    Args:
        filepath: Path to the CSV dataset.
        feature_cols: List of feature column names.
        target_col: Target column name.
        test_size: Proportion for test split.
    """
    print("\n" + "=" * 50)
    print(f"  PIPELINE: {filepath}")
    print("=" * 50)

    df = load_dataset(filepath)
    X, y = preprocess(df, feature_cols, target_col)
    X_train, X_test, y_train, y_test = split_data(X, y, test_size)
    model = train_model(X_train, y_train)
    evaluate(model, X_test, y_test)


def main() -> None:
    # pipeline 1 - salary prediction
    run_pipeline(
        filepath="datasets/employee_cleaned.csv",
        feature_cols=["age", "department"],
        target_col="annual_salary",
    )

    # pipeline 2 - student percentage prediction
    run_pipeline(
        filepath="datasets/student_cleaned.csv",
        feature_cols=["math", "science", "english", "history"],
        target_col="percentage",
    )


if __name__ == "__main__":
    main()