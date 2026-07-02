"""
model_comparison.py
-------------------
Compares Linear Regression, Decision Tree and Random Forest
on the employee salary dataset.

Usage:
    python3 model_comparison.py
"""

import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

INPUT_FILE = "datasets/employee_cleaned.csv"
PREDICTIONS_DIR = "predictions"


def load_and_preprocess(filepath: str) -> tuple:
    """Load and preprocess employee dataset."""
    df = pd.read_csv(filepath)

    le = LabelEncoder()
    df["department_encoded"] = le.fit_transform(df["department"])

    X = df[["age", "department_encoded"]]
    y = df["annual_salary"]

    print(f"Loaded {len(df)} records.")
    print(f"Features: age, department | Target: annual_salary")
    return X, y, df


def evaluate_model(name: str, model, X_test, y_test) -> dict:
    """Evaluate a trained model and return metrics."""
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    return {
        "model": name,
        "mae": round(mae, 2),
        "mse": round(mse, 2),
        "rmse": round(rmse, 2),
        "r2": round(r2, 4),
        "predictions": predictions,
    }


def save_predictions(
    name: str,
    y_test: pd.Series,
    predictions: np.ndarray,
    df: pd.DataFrame,
    output_dir: str,
) -> None:
    """Save actual vs predicted values to CSV."""
    os.makedirs(output_dir, exist_ok=True)

    results = pd.DataFrame({
        "name": df.loc[y_test.index, "name"].values,
        "department": df.loc[y_test.index, "department"].values,
        "actual_salary": y_test.values,
        "predicted_salary": predictions.round(0),
        "difference": (y_test.values - predictions).round(0),
    })

    filename = f"{output_dir}/{name.lower().replace(' ', '_')}.csv"
    results.to_csv(filename, index=False)
    print(f"Saved predictions to {filename}")


def display_comparison(results: list[dict]) -> None:
    """Display model comparison table."""
    print("\n" + "=" * 70)
    print("              MODEL COMPARISON TABLE")
    print("=" * 70)
    print(f"{'Model':<25} {'MAE':>12} {'MSE':>15} {'RMSE':>12} {'R2':>8}")
    print("-" * 70)
    for r in results:
        print(f"{r['model']:<25} {r['mae']:>12,.2f} {r['mse']:>15,.2f} {r['rmse']:>12,.2f} {r['r2']:>8.4f}")
    print("=" * 70)

    # find best model by R2
    best = max(results, key=lambda x: x["r2"])
    print(f"\nBest Model: {best['model']} (R2 = {best['r2']})")


def main() -> None:
    X, y, df = load_and_preprocess(INPUT_FILE)

    # train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Train: {len(X_train)} | Test: {len(X_test)}\n")

    # define models
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    }

    results = []

    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        result = evaluate_model(name, model, X_test, y_test)
        results.append(result)
        save_predictions(name, y_test, result["predictions"], df, PREDICTIONS_DIR)

    display_comparison(results)

    # detailed actual vs predicted for each model
    print("\n-- Actual vs Predicted --")
    for r in results:
        print(f"\n{r['model']}:")
        print(f"  {'Actual':>12} {'Predicted':>12} {'Difference':>12}")
        print("  " + "-" * 40)
        for actual, predicted in zip(y_test, r["predictions"]):
            diff = actual - predicted
            print(f"  Rs.{actual:>9,.0f} Rs.{predicted:>9,.0f} Rs.{diff:>+9,.0f}")


if __name__ == "__main__":
    main()