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