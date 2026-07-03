"""
feature_engineering.py
----------------------
Creates new features from existing data and encodes
categorical variables for the Employee Salary Prediction System.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import logging

logger = logging.getLogger(__name__)


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Engineer new features from existing columns.
    - Annual Salary
    - Experience Group (based on age)
    - Age Category

    Args:
        df: Cleaned DataFrame.

    Returns:
        DataFrame with new features.
    """
    df = df.copy()

    # annual salary
    df["annual_salary"] = df["salary"] * 12
    logger.info("Created feature: annual_salary")

    # experience group based on age
    df["experience_group"] = pd.cut(
        df["age"],
        bins=[0, 27, 31, 100],
        labels=["Junior", "Mid", "Senior"]
    )
    logger.info("Created feature: experience_group")

    # age category
    df["age_category"] = pd.cut(
        df["age"],
        bins=[0, 26, 30, 34, 100],
        labels=["Early Career", "Mid Career", "Experienced", "Veteran"]
    )
    logger.info("Created feature: age_category")

    return df


def encode_features(df: pd.DataFrame) -> tuple:
    """
    Encode categorical features for ML model training.
    Returns encoded DataFrame and label encoders.

    Args:
        df: DataFrame with engineered features.

    Returns:
        Tuple of (encoded DataFrame, dict of LabelEncoders)
    """
    df = df.copy()
    encoders = {}

    categorical_cols = ["department", "experience_group", "age_category"]

    for col in categorical_cols:
        le = LabelEncoder()
        df[f"{col}_encoded"] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
        logger.info(f"Encoded column: '{col}'")

    return df, encoders


def get_feature_matrix(df: pd.DataFrame) -> tuple:
    """
    Return feature matrix X and target vector y.

    Args:
        df: Encoded DataFrame.

    Returns:
        Tuple of (X, y)
    """
    feature_cols = ["age", "department_encoded", "experience_group_encoded"]
    target_col = "annual_salary"

    X = df[feature_cols]
    y = df[target_col]

    logger.info(f"Feature matrix shape: {X.shape}")
    return X, y, feature_cols