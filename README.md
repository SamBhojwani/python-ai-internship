# Python AI Internship – Muthu Soft Labs

**Intern:** Samarth Bhojwani  
**Mentor:** Harish Kumar S  
**Duration:** 30 Days (Remote)

---

## Day 01 – Environment Setup & Python Basics

### Scripts

**csv_analyzer.py** – Reads a CSV file and displays row count, column count, column names, and missing values.
```bash
python day-01/csv_analyzer.py day-01/sample_data/sample.csv
```

**json_formatter.py** – Reads a JSON file and pretty-prints it with error handling.
```bash
python day-01/json_formatter.py day-01/sample_data/sample.json
```

**csv_to_json.py** – Converts a CSV file to a JSON file.
```bash
python day-01/csv_to_json.py day-01/sample_data/sample.csv day-01/sample_data/output.json
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Day 02 – Python Data Structures & Utility Development

### Scripts

**student_manager.py** – Menu-driven student record manager with add, update, delete, search and display operations.
```bash
python day-02/student_manager.py
```

**utils.py** – Reusable utility module with string, number and list helper functions.

**test_utils.py** – Tests for all functions in utils.py.
```bash
python day-02/test_utils.py
```

**employee_analysis.py** – Processes employee records using list comprehensions, lambda functions and built-in functions.
```bash
python day-02/employee_analysis.py
```

**contact_manager.py** – CLI-based contact manager with add, search, update, delete and display operations.
```bash
python day-02/contact_manager.py
```

## Day 03 – Modules, Exception Handling & File Processing

### Scripts

**expense_tracker.py** – CLI expense tracker that persists data using a JSON file.
```bash
python day-03/expense_tracker.py
```

**file_analyzer.py** – Reads a text file and displays line, word and character counts.
```bash
python day-03/file_analyzer.py day-03/data/sample.txt
```

**csv_report_generator.py** – Reads employee CSV data and exports a salary summary as JSON.
```bash
python day-03/csv_report_generator.py day-03/data/employees.csv day-03/data/report.json
```

## Day 04 – Data Processing, Logging & Configuration Management

### Scripts

**employee_processor.py** – Reads employee CSV data, calculates salary statistics, groups by department and generates a JSON report. Logs to both terminal and app.log. Configuration driven via config.json.
```bash
python day-04/employee_processor.py
```

**log_analyzer.py** – Reads a log file and counts INFO, WARNING and ERROR entries.
```bash
python day-04/log_analyzer.py day-04/app.log
```


## Day 05 – Object-Oriented Programming & System Design Basics

### Structure
day-05/

├── models/

│   └── employee.py        ← Employee class

├── services/

│   └── employee_service.py ← Business logic

├── data/

│   └── employees.json     ← Persisted data

└── main.py                ← CLI interface

### Features
- Add, view, update, delete and list employees
- Department statistics (total, average salary, highest paid)
- Search by ID, name and department
- Email format validation
- JSON persistence — data survives between runs

### Usage
```bash
python day-05/main.py
```

## Day 06 – Unit Testing, Debugging & Code Quality

### Structure
day-06/

├── models/

│   └── employee.py        ← refactored model

├── services/

│   └── employee_service.py ← refactored service

├── tests/

│   ├── test_employee.py   ← unit tests for employee system

│   └── test_fixed_code.py ← tests verifying bug fixes

├── buggy_code.py          ← intentional bugs for debugging practice

├── fixed_code.py          ← fixed version with documented fixes

├── main.py                ← refactored CLI with file logging

└── app.log                ← generated log file

### Running Tests
```bash
python -m unittest tests/test_employee.py
python -m unittest tests/test_fixed_code.py
```

### Bugs Fixed in buggy_code.py
- `calculate_discount` — discount percent not divided by 100
- `get_top_earners` — sorted ascending instead of descending
- `calculate_compound_interest` — used `^` (XOR) instead of `**` (power)
- `find_common_elements` — mutating list while iterating caused incorrect results

### Refactoring Changes from Day 05
- Moved `json` and `os` imports to top of `employee_service.py`
- Removed duplicate logging setup in `main.py`
- Added `__repr__` method to `Employee` class


## Day 07 – Week 1 Mini Project: Personal Finance Tracker

A complete CLI-based Personal Finance Tracker consolidating all Week 1 concepts.

### Features
- Add, view, delete and search expenses
- Financial reports — total, highest, lowest, category-wise summary
- JSON persistence
- File logging to `logs/app.log`
- 18 unit tests

### Usage
```bash
cd day-07
python main.py
```

### Run Tests
```bash
cd day-07
python -m unittest tests/test_expense.py
```


## Day 08 – NumPy & Numerical Computing

**student_marks.py** – Analyzes student marks — highest, lowest, average, median and students above average.
```bash
python day-08/student_marks.py
```

**matrix_calculator.py** – Performs matrix addition, subtraction, multiplication and transpose.
```bash
python day-08/matrix_calculator.py
```

**sales_analysis.py** – Analyzes 12 months of sales data with a bar chart visualization.
```bash
python day-08/sales_analysis.py
```

**salary_analysis.py** – Generates random salary data for 100 employees and calculates stats including top 10 salaries.
```bash
python day-08/salary_analysis.py
```