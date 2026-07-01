"""
ml_pipeline_class.py
--------------------
OOP-based ML Pipeline class for training and saving models.

Usage:
    python3 ml_pipeline_class.py
"""

import os
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder


class MLPipeline:
    def __init__(self, name: str = "MLPipeline"):
        self.name = name
        self.df: pd.DataFrame = None
        self.X: pd.DataFrame = None
        self.y: pd.Series = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model: LinearRegression = None
        self.feature_cols: list[str] = []
        self.target_col: str = None

    def load_dataset(self, filepath: str) -> None:
        """
        Load a CSV dataset.

        Args:
            filepath: Path to the CSV file.

        Raises:
            FileNotFoundError: If file does not exist.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        self.df = pd.read_csv(filepath)
        print(f"[{self.name}] Loaded {len(self.df)} records with {len(self.df.columns)} columns.")

    def preprocess(self, feature_cols: list[str], target_col: str) -> None:
        """
        Select features and target, encode string columns.

        Args:
            feature_cols: List of feature column names.
            target_col: Target column name.
        """
        if self.df is None:
            raise RuntimeError("No dataset loaded. Call load_dataset() first.")

        self.feature_cols = feature_cols
        self.target_col = target_col
        df = self.df.copy()

        for col in feature_cols:
            if pd.api.types.is_string_dtype(df[col]):
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                print(f"[{self.name}] Encoded column: '{col}'")

        self.X = df[feature_cols]
        self.y = df[target_col]
        print(f"[{self.name}] Features: {feature_cols} | Target: {target_col}")

    def split_data(self, test_size: float = 0.2) -> None:
        """
        Split data into training and testing sets.

        Args:
            test_size: Proportion for testing.
        """
        if self.X is None or self.y is None:
            raise RuntimeError("Data not preprocessed. Call preprocess() first.")

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=42
        )
        print(f"[{self.name}] Train: {len(self.X_train)} | Test: {len(self.X_test)}")

    def train_model(self) -> None:
        """Train a Linear Regression model."""
        if self.X_train is None:
            raise RuntimeError("Data not split. Call split_data() first.")

        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        print(f"[{self.name}] Model trained successfully.")

    def predict(self) -> None:
        """Make predictions and display evaluation results."""
        if self.model is None:
            raise RuntimeError("Model not trained. Call train_model() first.")

        predictions = self.model.predict(self.X_test)

        mae = mean_absolute_error(self.y_test, predictions)
        rmse = np.sqrt(mean_squared_error(self.y_test, predictions))
        r2 = r2_score(self.y_test, predictions)

        print("\n" + "=" * 50)
        print(f"     [{self.name}] RESULTS")
        print("=" * 50)
        print(f"  MAE  : {mae:.2f}")
        print(f"  RMSE : {rmse:.2f}")
        print(f"  R2   : {r2:.4f}")

        print(f"\nActual vs Predicted:")
        print(f"{'Actual':>15} {'Predicted':>15} {'Difference':>15}")
        print("-" * 48)
        for actual, predicted in zip(self.y_test, predictions):
            diff = actual - predicted
            print(f"{actual:>15.2f} {predicted:>15.2f} {diff:>+15.2f}")
        print("=" * 50)

    def save_model(self, output_path: str) -> None:
        """
        Save the trained model to a file using pickle.

        Args:
            output_path: Path to save the model file.
        """
        if self.model is None:
            raise RuntimeError("No model to save. Call train_model() first.")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as f:
            pickle.dump(self.model, f)
        print(f"[{self.name}] Model saved to {output_path}")

    def run(
        self,
        filepath: str,
        feature_cols: list[str],
        target_col: str,
        model_path: str,
        test_size: float = 0.2,
    ) -> None:
        """Run the full pipeline in one call."""
        self.load_dataset(filepath)
        self.preprocess(feature_cols, target_col)
        self.split_data(test_size)
        self.train_model()
        self.predict()
        self.save_model(model_path)


def main() -> None:
    # pipeline 1 - salary prediction
    pipeline1 = MLPipeline(name="SalaryPredictor")
    pipeline1.run(
        filepath="datasets/employee_cleaned.csv",
        feature_cols=["age", "department"],
        target_col="annual_salary",
        model_path="models/salary_model.pkl",
    )

    # pipeline 2 - student percentage prediction
    pipeline2 = MLPipeline(name="StudentPredictor")
    pipeline2.run(
        filepath="datasets/student_cleaned.csv",
        feature_cols=["math", "science", "english", "history"],
        target_col="percentage",
        model_path="models/student_model.pkl",
    )


if __name__ == "__main__":
    main()