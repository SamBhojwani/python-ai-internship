"""
prediction.py
-------------
Loads the saved model and provides salary prediction
based on user input for the Employee Salary Prediction System.
"""

import pickle
import numpy as np
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_model(model_path: str, encoders_path: str) -> tuple:
    """
    Load saved model and encoders from disk.

    Args:
        model_path: Path to the saved model pickle file.
        encoders_path: Path to the saved encoders pickle file.

    Returns:
        Tuple of (model, encoders)

    Raises:
        FileNotFoundError: If model or encoders file not found.
    """
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        with open(encoders_path, "rb") as f:
            encoders = pickle.load(f)
        logger.info("Model and encoders loaded successfully.")
        return model, encoders
    except FileNotFoundError as e:
        logger.error(f"Model file not found: {e}")
        raise


def get_experience_group(age: int) -> str:
    """Map age to experience group."""
    if age <= 27:
        return "Junior"
    elif age <= 31:
        return "Mid"
    else:
        return "Senior"


def predict_salary(
    model,
    encoders: dict,
    age: int,
    department: str,
) -> float:
    """
    Predict annual salary for a given employee profile.

    Args:
        model: Trained ML model.
        encoders: Dict of LabelEncoders.
        age: Employee age.
        department: Employee department.

    Returns:
        Predicted annual salary.
    """
    experience_group = get_experience_group(age)

    # encode categorical features
    dept_encoded = encoders["department"].transform([department])[0]
    exp_encoded = encoders["experience_group"].transform([experience_group])[0]

    # build feature array
    features = pd.DataFrame({
        "age": [age],
        "department_encoded": [dept_encoded],
        "experience_group_encoded": [exp_encoded],
    })

    prediction = model.predict(features)[0]
    return round(prediction, 2)


def run_prediction_interface(model, encoders: dict) -> None:
    """
    Interactive CLI interface for salary prediction.

    Args:
        model: Trained ML model.
        encoders: Dict of LabelEncoders.
    """
    print("\n" + "=" * 50)
    print("       SALARY PREDICTION INTERFACE")
    print("=" * 50)

    valid_departments = list(encoders["department"].classes_)
    print(f"Available Departments: {', '.join(valid_departments)}")

    while True:
        print("\nEnter employee details (or 'quit' to exit):")

        try:
            age_input = input("Age: ").strip()
            if age_input.lower() == "quit":
                break

            age = int(age_input)
            if age < 18 or age > 65:
                print("Age must be between 18 and 65.")
                continue

            department = input("Department: ").strip().title()
            department = department.replace("Hr", "HR")

            if department not in valid_departments:
                print(f"Invalid department. Choose from: {', '.join(valid_departments)}")
                continue

            experience_group = get_experience_group(age)
            predicted = predict_salary(model, encoders, age, department)

            print("\n" + "-" * 40)
            print(f"Age              : {age}")
            print(f"Department       : {department}")
            print(f"Experience Group : {experience_group}")
            print(f"Predicted Salary : Rs.{predicted:,.2f} per year")
            print(f"Monthly Salary   : Rs.{predicted/12:,.2f} per month")
            print("-" * 40)

        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
        except Exception as e:
            print(f"Error: {e}")