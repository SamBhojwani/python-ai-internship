"""
main.py
-------
Entry point for the Employee Salary Prediction System.
Runs the complete ML pipeline and prediction interface.

Usage:
    python3 src/main.py
"""

import os
import logging
import pandas as pd

from preprocessing import load_raw_data, inspect_dataset, clean_data, save_cleaned_data
from feature_engineering import create_features, encode_features, get_feature_matrix
from model_training import (
    split_data,
    train_models,
    evaluate_models,
    display_comparison,
    save_model,
    save_predictions,
)
from prediction import load_model, run_prediction_interface

# ── Logging Setup ─────────────────────────────────────────────
os.makedirs("../logs", exist_ok=True)
os.makedirs("../reports", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("../logs/app.log", mode="a", encoding="utf-8")
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))
logging.getLogger().addHandler(file_handler)

# ── Paths ─────────────────────────────────────────────────────
RAW_DATA = "../dataset/raw/employees.csv"
CLEANED_DATA = "../dataset/cleaned/employees_cleaned.csv"
MODELS_DIR = "../models"
PREDICTIONS_DIR = "../reports/predictions"


def run_pipeline() -> None:
    """Run the complete ML pipeline."""

    logger.info("Application started.")
    print("\n" + "=" * 55)
    print("    EMPLOYEE SALARY PREDICTION SYSTEM")
    print("=" * 55)

    # step 1 - load and inspect
    print("\n[Step 1] Loading and Inspecting Dataset...")
    df_raw = load_raw_data(RAW_DATA)
    inspect_dataset(df_raw)

    # step 2 - clean
    print("\n[Step 2] Cleaning Dataset...")
    df_clean = clean_data(df_raw)
    save_cleaned_data(df_clean, CLEANED_DATA)
    print(f"Cleaned dataset: {df_clean.shape[0]} rows x {df_clean.shape[1]} columns")

    # step 3 - feature engineering
    print("\n[Step 3] Engineering Features...")
    df_features = create_features(df_clean)
    df_encoded, encoders = encode_features(df_features)

    print("\nNew Features Created:")
    print(df_encoded[["name", "department", "age", "experience_group",
                       "age_category", "annual_salary"]].to_string(index=False))

    # step 4 - EDA summary
    print("\n[Step 4] EDA Summary...")
    print("\nEmployees by Department:")
    dept_counts = df_clean.groupby("department")["name"].count()
    for dept, count in dept_counts.items():
        print(f"  {dept:<20} {count} employees")

    print("\nAverage Salary by Department:")
    dept_salary = df_clean.groupby("department")["salary"].mean()
    for dept, avg in dept_salary.items():
        print(f"  {dept:<20} Rs.{avg:,.2f}")

    print("\nTop 5 Highest Paid:")
    top5 = df_clean.nlargest(5, "salary")[["name", "department", "salary"]]
    for _, row in top5.iterrows():
        print(f"  {row['name']:<20} {row['department']:<15} Rs.{row['salary']:,}")

    # step 5 - train and evaluate
    print("\n[Step 5] Training and Evaluating Models...")
    X, y, feature_cols = get_feature_matrix(df_encoded)
    X_train, X_test, y_train, y_test = split_data(X, y)

    print(f"Features used: {feature_cols}")
    models = train_models(X_train, y_train)
    results = evaluate_models(models, X_test, y_test)
    best_model_name = display_comparison(results)

    # step 6 - save predictions and model
    print("\n[Step 6] Saving Predictions and Model...")
    save_predictions(results, y_test, df_encoded, PREDICTIONS_DIR)
    best_model = models[best_model_name]
    save_model(best_model, encoders, MODELS_DIR)
    print(f"Best model saved: {best_model_name}")

    # step 7 - prediction interface
    print("\n[Step 7] Launching Prediction Interface...")
    model, encoders = load_model(
        os.path.join(MODELS_DIR, "best_model.pkl"),
        os.path.join(MODELS_DIR, "encoders.pkl"),
    )
    run_prediction_interface(model, encoders)

    logger.info("Application finished.")


if __name__ == "__main__":
    run_pipeline()