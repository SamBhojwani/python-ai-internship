"""
model_training.py
-----------------
Trains and evaluates multiple ML models for the
Employee Salary Prediction System.
"""

import os
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import logging

logger = logging.getLogger(__name__)


def split_data(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2) -> tuple:
    """
    Split data into training and testing sets.

    Args:
        X: Feature matrix.
        y: Target vector.
        test_size: Proportion for testing.

    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    logger.info(f"Train: {len(X_train)} | Test: {len(X_test)}")
    return X_train, X_test, y_train, y_test


def train_models(X_train, y_train) -> dict:
    """
    Train Linear Regression, Decision Tree and Random Forest.

    Args:
        X_train: Training features.
        y_train: Training target.

    Returns:
        Dict of model name to trained model.
    """
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    }

    trained = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained[name] = model
        logger.info(f"Trained: {name}")

    return trained


def evaluate_models(models: dict, X_test, y_test) -> list[dict]:
    """
    Evaluate all trained models and return metrics.

    Args:
        models: Dict of model name to trained model.
        X_test: Test features.
        y_test: Actual target values.

    Returns:
        List of result dicts with metrics and predictions.
    """
    results = []

    for name, model in models.items():
        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, predictions)

        results.append({
            "model": name,
            "mae": round(mae, 2),
            "mse": round(mse, 2),
            "rmse": round(rmse, 2),
            "r2": round(r2, 4),
            "predictions": predictions,
        })

        logger.info(f"{name} - MAE: {mae:.2f} | R2: {r2:.4f}")

    return results


def display_comparison(results: list[dict]) -> str:
    """Display and return model comparison table."""
    print("\n" + "=" * 70)
    print("              MODEL COMPARISON TABLE")
    print("=" * 70)
    print(f"{'Model':<25} {'MAE':>12} {'RMSE':>12} {'R2':>8}")
    print("-" * 70)

    for r in results:
        print(f"{r['model']:<25} {r['mae']:>12,.2f} {r['rmse']:>12,.2f} {r['r2']:>8.4f}")

    print("=" * 70)

    best = max(results, key=lambda x: x["r2"])
    print(f"\nBest Model: {best['model']} (R2 = {best['r2']})")
    return best["model"]


def save_model(model, encoders: dict, output_dir: str) -> None:
    """
    Save the best model and encoders to disk.

    Args:
        model: Trained model to save.
        encoders: Dict of LabelEncoders.
        output_dir: Directory to save files.
    """
    os.makedirs(output_dir, exist_ok=True)

    model_path = os.path.join(output_dir, "best_model.pkl")
    encoders_path = os.path.join(output_dir, "encoders.pkl")

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    with open(encoders_path, "wb") as f:
        pickle.dump(encoders, f)

    logger.info(f"Model saved to {model_path}")
    logger.info(f"Encoders saved to {encoders_path}")


def save_predictions(results: list[dict], y_test, df, output_dir: str) -> None:
    """Save actual vs predicted values for each model to CSV."""
    os.makedirs(output_dir, exist_ok=True)

    for r in results:
        filename = r["model"].lower().replace(" ", "_") + ".csv"
        output_path = os.path.join(output_dir, filename)

        pred_df = pd.DataFrame({
            "actual_salary": y_test.values,
            "predicted_salary": r["predictions"].round(0),
            "difference": (y_test.values - r["predictions"]).round(0),
        })

        pred_df.to_csv(output_path, index=False)
        logger.info(f"Predictions saved to {output_path}")