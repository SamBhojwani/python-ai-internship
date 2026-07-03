# Model Evaluation Report
## Employee Salary Prediction System

**Intern:** Samarth Bhojwani
**Date:** 3rd July 2026
**Project:** Week 2 Mini Project - Muthu Soft Labs

---

## Problem Statement

Predict the annual salary of an employee based on their age, department and experience group using machine learning regression models.

---

## Dataset Description

- **File:** employees.csv
- **Records:** 15 employees
- **Original Features:** employee_id, name, department, salary, age, city
- **Target:** annual_salary (salary x 12)

---

## Data Cleaning Steps

- Checked for duplicates - none found
- Checked for missing values - none found
- Standardized department names to title case
- Standardized name and city columns to title case

---

## Feature Engineering

| Feature | Description |
|---|---|
| annual_salary | Monthly salary x 12 |
| experience_group | Junior (<=27), Mid (28-31), Senior (32+) |
| age_category | Early Career, Mid Career, Experienced, Veteran |
| department_encoded | Label encoded department |
| experience_group_encoded | Label encoded experience group |

**Features used for training:** age, department_encoded, experience_group_encoded

---

## Models Trained

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

---

## Evaluation Metrics

| Model | MAE | RMSE | R2 Score |
|---|---|---|---|
| Linear Regression | Rs.124,472 | Rs.165,657 | -70.46 |
| Decision Tree | Rs.36,000 | Rs.36,000 | -2.38 |
| Random Forest | Rs.31,440 | Rs.46,175 | -4.55 |

---

## Best Performing Model

**Decision Tree Regressor** achieved the best R2 score (-2.38) and second lowest MAE (Rs.36,000).

All models produced negative R2 scores because the dataset has only 15 records which is far too small for reliable machine learning. With only 3 test samples, a single poor prediction heavily impacts all metrics.

---

## Key Observations

- Department is the strongest predictor of salary - Engineering pays significantly more than HR
- Age alone is a weak predictor since salary varies more by department than by age
- Decision Tree performed best likely due to memorizing department-salary patterns
- Linear Regression performed worst because the relationship between features and salary is not strongly linear with this data
- All predictions from the interface are reasonable and match actual department averages

---

## Suggestions for Improvement

- Increase dataset to at least 500-1000 records
- Add years of experience as an explicit feature
- Add education level as a feature
- Use cross-validation instead of single train-test split
- Try gradient boosting models like XGBoost
- Add salary bands or ranges instead of exact prediction