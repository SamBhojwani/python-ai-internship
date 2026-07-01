"""
salary_prediction.py
--------------------
Predicts employee annual salary using Linear Regression.
Features: age, department (encoded)
Target: annual_salary

Usage:
    python3 salary_prediction.py
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

INPUT_FILE = "datasets/employee_cleaned.csv"


def load_data(filepath: str) -> pd.DataFrame:
    """Load cleaned employee dataset."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} records.")
    return df


def preprocess(df: pd.DataFrame) -> tuple:
    """
    Prepare features and target for model training.
    - Encode department as numeric
    - Select features: age, department
    - Target: annual_salary
    """
    df = df.copy()

    # encode department column to numeric
    le = LabelEncoder()
    df["department_encoded"] = le.fit_transform(df["department"])

    print(f"\nDepartment Encoding:")
    for label, encoded in zip(le.classes_, le.transform(le.classes_)):
        print(f"  {label} -> {encoded}")

    # features and target
    X = df[["age", "department_encoded"]]
    y = df["annual_salary"]

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
    print("         SALARY PREDICTION MODEL RESULTS")
    print("=" * 55)
    print(f"\nModel Coefficients : {model.coef_}")
    print(f"Intercept          : {model.intercept_:.2f}")

    print(f"\nModel Performance:")
    print(f"  MAE   : Rs.{mae:,.2f}")
    print(f"  RMSE  : Rs.{rmse:,.2f}")
    print(f"  R2    : {r2:.4f}")

    print(f"\nActual vs Predicted:")
    print(f"{'Actual':>15} {'Predicted':>15} {'Difference':>15}")
    print("-" * 50)
    for actual, predicted in zip(y_test, predictions):
        diff = actual - predicted
        print(f"Rs.{actual:>10,.0f}  Rs.{predicted:>10,.0f}  Rs.{diff:>10,.0f}")

    print("=" * 55)


def main() -> None:
    df = load_data(INPUT_FILE)
    print("\nDataset Preview:")
    print(df[["name", "department", "age", "salary", "annual_salary"]].head().to_string(index=False))

    X, y = preprocess(df)
    train_and_evaluate(X, y)


if __name__ == "__main__":
    main()