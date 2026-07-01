"""
student_prediction.py
---------------------
Predicts student final percentage using Linear Regression.
Features: math, science, english, history
Target: percentage

Usage:
    python3 student_prediction.py
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

INPUT_FILE = "datasets/student_cleaned.csv"

FEATURES = ["math", "science", "english", "history"]
TARGET = "percentage"


def load_data(filepath: str) -> pd.DataFrame:
    """Load cleaned student dataset."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records.")
    return df


def preprocess(df: pd.DataFrame) -> tuple:
    """
    Prepare features and target for model training.
    Features: math, science, english, history
    Target: percentage
    """
    X = df[FEATURES]
    y = df[TARGET]
    return X, y


def train_and_evaluate(X: pd.DataFrame, y: pd.Series) -> None:
    """Train Linear Regression model and evaluate performance."""

    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"\nTraining samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    # train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # predict
    predictions = model.predict(X_test)

    # evaluate
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    print("\n" + "=" * 55)
    print("     STUDENT PERFORMANCE PREDICTION RESULTS")
    print("=" * 55)

    print(f"\nFeature Coefficients:")
    for feature, coef in zip(FEATURES, model.coef_):
        print(f"  {feature:<12} {coef:.4f}")
    print(f"Intercept : {model.intercept_:.4f}")

    print(f"\nModel Performance:")
    print(f"  MAE  : {mae:.2f}%")
    print(f"  RMSE : {rmse:.2f}%")
    print(f"  R2   : {r2:.4f}")

    print(f"\nActual vs Predicted:")
    print(f"{'Student':<20} {'Actual':>10} {'Predicted':>10} {'Difference':>12}")
    print("-" * 55)

    # get student names for test set
    test_indices = y_test.index
    names = pd.read_csv(INPUT_FILE).loc[test_indices, "name"].values

    for name, actual, predicted in zip(names, y_test, predictions):
        diff = actual - predicted
        print(f"{name:<20} {actual:>9.2f}% {predicted:>9.2f}% {diff:>+11.2f}%")

    print("=" * 55)


def main() -> None:
    df = load_data(INPUT_FILE)
    print("\nDataset Preview:")
    print(df[["name"] + FEATURES + [TARGET, "grade"]].head().to_string(index=False))

    X, y = preprocess(df)
    train_and_evaluate(X, y)


if __name__ == "__main__":
    main()