"""
model_improvement.py
--------------------
Experiments with different train-test splits, feature selection
and hyperparameters to improve model performance.

Usage:
    python3 model_improvement.py
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

INPUT_FILE = "datasets/employee_cleaned.csv"


def load_and_preprocess(filepath: str) -> pd.DataFrame:
    """Load and preprocess employee dataset."""
    df = pd.read_csv(filepath)
    le = LabelEncoder()
    df["department_encoded"] = le.fit_transform(df["department"])
    return df


def evaluate(name: str, y_test, predictions) -> dict:
    """Return evaluation metrics for a model."""
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    return {"model": name, "mae": round(mae, 2), "rmse": round(rmse, 2), "r2": round(r2, 4)}


def split_ratio_comparison(df: pd.DataFrame) -> None:
    """Compare different train-test split ratios."""
    print("\n" + "=" * 60)
    print("  EXPERIMENT 1 - Different Train-Test Split Ratios")
    print("=" * 60)

    X = df[["age", "department_encoded"]]
    y = df["annual_salary"]

    splits = [0.1, 0.2, 0.3]
    print(f"\n{'Split':>8} {'Train':>8} {'Test':>8} {'MAE':>12} {'R2':>8}")
    print("-" * 50)

    for split in splits:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=split, random_state=42
        )
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        result = evaluate(f"RF split={split}", y_test, predictions)
        print(f"{split:>8} {len(X_train):>8} {len(X_test):>8} {result['mae']:>12,.2f} {result['r2']:>8.4f}")


def hyperparameter_tuning(df: pd.DataFrame) -> None:
    """Tune Random Forest hyperparameters."""
    print("\n" + "=" * 60)
    print("  EXPERIMENT 2 - Random Forest Hyperparameter Tuning")
    print("=" * 60)

    X = df[["age", "department_encoded"]]
    y = df["annual_salary"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    configs = [
        {"n_estimators": 10, "max_depth": None},
        {"n_estimators": 50, "max_depth": 3},
        {"n_estimators": 100, "max_depth": 3},
        {"n_estimators": 200, "max_depth": 5},
    ]

    print(f"\n{'Estimators':>12} {'Max Depth':>12} {'MAE':>12} {'R2':>8}")
    print("-" * 50)

    for config in configs:
        model = RandomForestRegressor(random_state=42, **config)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        result = evaluate("RF", y_test, predictions)
        depth = str(config["max_depth"]) if config["max_depth"] else "None"
        print(f"{config['n_estimators']:>12} {depth:>12} {result['mae']:>12,.2f} {result['r2']:>8.4f}")


def cross_validation(df: pd.DataFrame) -> None:
    """Compare models using 5-fold cross validation."""
    print("\n" + "=" * 60)
    print("  EXPERIMENT 3 - Cross Validation (3-Fold)")
    print("=" * 60)

    X = df[["age", "department_encoded"]]
    y = df["annual_salary"]

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    }

    print(f"\n{'Model':<25} {'CV R2 Mean':>12} {'CV R2 Std':>12}")
    print("-" * 52)

    for name, model in models.items():
        scores = cross_val_score(model, X, y, cv=3, scoring="r2")
        print(f"{name:<25} {scores.mean():>12.4f} {scores.std():>12.4f}")


def feature_scaling(df: pd.DataFrame) -> None:
    """Compare Linear Regression with and without feature scaling."""
    print("\n" + "=" * 60)
    print("  EXPERIMENT 4 - Feature Scaling for Linear Regression")
    print("=" * 60)

    X = df[["age", "department_encoded"]]
    y = df["annual_salary"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # without scaling
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    result_before = evaluate("Linear - No Scaling", y_test, predictions)

    # with scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model_scaled = LinearRegression()
    model_scaled.fit(X_train_scaled, y_train)
    predictions_scaled = model_scaled.predict(X_test_scaled)
    result_after = evaluate("Linear - With Scaling", y_test, predictions_scaled)

    print(f"\n{'Model':<25} {'MAE':>12} {'R2':>8}")
    print("-" * 48)
    print(f"{result_before['model']:<25} {result_before['mae']:>12,.2f} {result_before['r2']:>8.4f}")
    print(f"{result_after['model']:<25} {result_after['mae']:>12,.2f} {result_after['r2']:>8.4f}")


def main() -> None:
    print("Loading dataset...")
    df = load_and_preprocess(INPUT_FILE)

    split_ratio_comparison(df)
    hyperparameter_tuning(df)
    cross_validation(df)
    feature_scaling(df)

    print("\n" + "=" * 60)
    print("Key Finding: All experiments confirm that 15 records")
    print("is too small for reliable ML. Cross-validation with")
    print("3 folds gives more stable estimates than a single split.")
    print("=" * 60)


if __name__ == "__main__":
    main()