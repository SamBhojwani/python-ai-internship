# Personal Finance Tracker

A CLI-based Personal Finance Tracker built with Python. This is the Week 1 Mini Project for the Muthu Soft Labs Applied AI & Python Engineering Internship.

---

## Project Overview

The Personal Finance Tracker helps users manage their daily expenses and generate financial summaries. All data is persisted locally using JSON, and all operations are logged to a file.

---

## Features

- Add expenses with title, category, amount and date
- View all expenses sorted by date
- Delete expenses by ID
- Search expenses by title or category
- Generate financial reports — total, highest, lowest and category-wise summary
- JSON persistence — data survives between sessions
- File logging — all operations logged to `logs/app.log`
- Full exception handling — invalid inputs never crash the app
- 18 unit tests covering all core functionality

---

## Project Structure
day-07/

├── models/

│   └── expense.py          ← Expense model class

├── services/

│   └── expense_service.py  ← Business logic

├── tests/

│   └── test_expense.py     ← Unit tests

├── data/

│   └── expenses.json       ← Persisted expense data

├── logs/

│   └── app.log             ← Application logs

├── main.py                 ← CLI interface

├── requirements.txt        ← Dependencies

└── README.md

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/SamBhojwani/python-ai-internship.git
cd python-ai-internship

# 2. Activate virtual environment
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
cd day-07
python main.py
```

### Sample Session
Welcome to Personal Finance Tracker
--- Menu ---

Add Expense
View Expenses
Delete Expense
Search Expenses
Generate Report
Exit


### Running Tests

```bash
python -m unittest tests/test_expense.py
```

---

## Sample Data Format

```json
[
    {
        "expense_id": "E001",
        "title": "Lunch",
        "category": "Food",
        "amount": 150.0,
        "date": "2026-06-24"
    }
]
```

---

## Future Improvements

- Add budget limits per category with alerts
- Export reports as CSV or PDF
- Add monthly and weekly filtering
- Build a web interface using FastAPI
- Add multi-user support with authentication