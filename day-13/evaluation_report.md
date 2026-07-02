# Model Evaluation Report

**Intern:** Samarth Bhojwani
**Date:** 29th June 2026
**Internship:** Applied AI & Python Engineering - Muthu Soft Labs

---

## Dataset Used

- **File:** employee_cleaned.csv
- **Source:** Day 11 cleaned employee dataset
- **Records:** 15 employees
- **Features:** age, department (label encoded)
- **Target:** annual_salary

---

## Features Selected

| Feature | Type | Description |
|---|---|---|
| age | Numeric | Employee age in years |
| department | Categorical (encoded) | Engineering=1, Data Science=0, HR=2 |

**Target Variable:** annual_salary (monthly salary x 12)

---

## Algorithms Tested

### 1. Linear Regression
Finds the best fit straight line through data points. Assumes a linear relationship between features and target.

### 2. Decision Tree Regressor
Splits data into branches based on feature conditions. Can capture non-linear relationships.

### 3. Random Forest Regressor
An ensemble of 100 decision trees. Averages predictions across all trees to reduce overfitting.

---

## Evaluation Metrics

| Model | MAE | RMSE | R2 Score |
|---|---|---|---|
| Linear Regression | Rs.115,189 | Rs.158,030 | -64.04 |
| Decision Tree | Rs.36,000 | Rs.36,000 | -2.38 |
| Random Forest | Rs.32,400 | Rs.43,817 | -3.99 |

---

## Best Performing Model

**Decision Tree Regressor** achieved the highest R2 score (-2.38) and lowest MAE (Rs.36,000).

However, all three models produced negative R2 scores, meaning none of them performed better than simply predicting the mean salary for every employee. This is not a failure of the algorithms - it is a data size problem.

---

## Observations

- All R2 scores are negative because the dataset has only 15 records
- With only 3 test samples, a single poor prediction heavily impacts all metrics
- Department alone does not explain salary variation well - employees in the same department have different salaries based on experience, which is not captured in the dataset
- Decision Tree performed best likely because it memorized the training data (overfitting) rather than learning a generalizable pattern
- Linear Regression performed worst because it assumes a linear relationship which does not exist strongly between age/department and salary with this data

---

## Suggestions for Improvement

- Increase dataset size to at least 500-1000 records for meaningful results
- Add more features - years of experience, education level, performance rating
- Use cross-validation instead of a single train-test split to get more reliable metrics
- Try feature scaling (StandardScaler) for Linear Regression
- Tune Decision Tree depth to reduce overfitting
- Increase Random Forest estimators and tune max_depth hyperparameter