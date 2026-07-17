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


## Day 09 - Pandas & Data Analysis

**employee_analysis.py** - Analyzes employee dataset - total, average/highest/lowest salary, department breakdown and top 5 earners. Exports summary to CSV.
```bash
python day-09/employee_analysis.py
```

**student_analysis.py** - Analyzes student performance - highest/lowest scorer, students above 80% and failing students.
```bash
python day-09/student_analysis.py
```

**dataset_cleaner.py** - Cleans a messy dataset - fills missing values with column averages, removes duplicates and saves cleaned CSV.
```bash
python day-09/dataset_cleaner.py
```

**dataset_analyzer.py** - Reusable DatasetAnalyzer class that works with any CSV - summary, missing values and report export.
```bash
python day-09/dataset_analyzer.py
```


## Day 10 - Exploratory Data Analysis (EDA)

**employee_eda.py** - EDA on employee dataset - department breakdown, salary distribution and top 10 earners. Exports to CSV.
```bash
python day-10/employee_eda.py
```

**student_eda.py** - EDA on student dataset - subject-wise averages, top/lowest performer, above 80% and failing students. Exports to CSV.
```bash
python day-10/student_eda.py
```

**sales_eda.py** - EDA on sales dataset - monthly revenue with bar chart, top products and category breakdown. Exports to CSV.
```bash
python day-10/sales_eda.py
```

**eda_report_generator.py** - Reusable EDAReportGenerator class with dataset info, descriptive statistics, group analysis and report export. Works with any CSV.
```bash
python day-10/eda_report_generator.py
```


## Day 11 - Data Cleaning & Feature Engineering

**employee_cleaner.py** - Cleans employee dataset - removes duplicates, fills missing values, standardizes department names and creates annual salary column.
```bash
python3 day-11/employee_cleaner.py
```

**student_cleaner.py** - Prepares student dataset - handles missing marks, calculates total marks, percentage and assigns grades (A/B/C/D/F).
```bash
python3 day-11/student_cleaner.py
```

**sales_cleaner.py** - Engineers features in sales dataset - creates profit, profit percentage, quarter and financial year columns.
```bash
python3 day-11/sales_cleaner.py
```

**data_cleaner.py** - Reusable DataCleaner class with remove duplicates, handle missing values, normalize columns, feature engineering and export methods. Works with any CSV.
```bash
python3 day-11/data_cleaner.py
```


## Day 12 - Introduction to Machine Learning

**salary_prediction.py** - Predicts employee annual salary using Linear Regression with age and department as features.
```bash
python3 day-12/salary_prediction.py
```

**student_prediction.py** - Predicts student percentage using subject marks as features. Achieves R2 of 1.0 since percentage is derived from marks.
```bash
python3 day-12/student_prediction.py
```

**ml_pipeline.py** - Reusable ML pipeline script that handles load, preprocess, split, train and evaluate for any dataset.
```bash
python3 day-12/ml_pipeline.py
```

**ml_pipeline_class.py** - OOP-based MLPipeline class with load, preprocess, split, train, predict and save model methods.
```bash
python3 day-12/ml_pipeline_class.py
```


## Day 13 - Model Evaluation & Performance Comparison

**model_comparison.py** - Compares Linear Regression, Decision Tree and Random Forest on employee salary dataset. Exports predictions to CSV.
```bash
python3 day-13/model_comparison.py
```

**model_improvement.py** - Experiments with split ratios, hyperparameter tuning, cross validation and feature scaling to improve model performance.
```bash
python3 day-13/model_improvement.py
```

**evaluation_report.md** - Full model evaluation report documenting dataset, features, algorithms, metrics, best model and suggestions.


## Day 14 - Week 2 Mini Project: Employee Salary Prediction System

A complete end-to-end ML application consolidating all Week 2 concepts.

### Structure
day-14-mini-project/
├── dataset/raw/ and cleaned/
├── models/
├── reports/predictions/
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── prediction.py
│   └── main.py
└── model_evaluation_report.md

### Features
- Complete ML pipeline from raw data to predictions
- Three models compared - Linear Regression, Decision Tree, Random Forest
- Interactive salary prediction interface
- Logging to app.log
- Model saved with pickle for reuse

### Usage
```bash
cd day-14-mini-project/src
python3 main.py
```


## Day 15 - FastAPI REST API Development

**Employee API** - A REST API for employee management with full CRUD operations, Pydantic schema validation, health check endpoint, and department filter. Auto-generated Swagger UI at /docs.




## Day 16 - Request Validation & CRUD API Enhancement

**Employee API v2** - Enhanced API with Pydantic field validation (email format, salary > 0), centralized exception handling, standardized success/error responses, services layer separating business logic from routes, and search/filter endpoints.



## Day 17 - Database Integration with SQLAlchemy

**database.py** - Configures SQLAlchemy engine, session factory and base model. Provides get_db dependency for injecting database sessions into routes.

**models.py** - Defines the Employee table using SQLAlchemy ORM with columns for employee_id, name, department, salary and email.

**schemas.py** - Pydantic schemas for request validation and response serialization with from_attributes enabled for ORM compatibility.

**crud.py** - All database operations - create, read, update, delete, department filter and pagination using SQLAlchemy session queries.

**routes.py** - API endpoint definitions wired to crud functions with database session injected via Depends(get_db).

**main.py** - App setup with Base.metadata.create_all to auto-create the employees table on startup.



## Day 18 - Authentication & API Security with JWT

**security.py** - Password hashing with bcrypt and JWT token creation and validation using python-jose. Tokens expire after 30 minutes and are signed with a secret key.

**auth.py** - Business logic for user registration and login. Checks for duplicate username and email on registration, verifies password against bcrypt hash on login.

**dependencies.py** - Reusable FastAPI dependency that extracts the JWT token from the Authorization header, validates it, and returns the current logged in user.

**models.py** - SQLAlchemy models for both Employee and User tables. User table stores hashed passwords and roles.

**schemas.py** - Pydantic schemas for user registration, login and response, plus all employee schemas from Day 17.

**routes.py** - Auth endpoints (register, login, me) and employee endpoints with POST, PUT and DELETE protected behind JWT authentication.

**main.py** - App setup with table auto-creation on startup.


## Day 19 - Docker & Application Containerization

**Dockerfile** - Builds the Employee API image using python:3.12-slim as the base image, installs dependencies and starts the server with uvicorn.

**docker-compose.yml** - Defines the employee-api service with port mapping, environment variable injection from .env, and volume mapping for live reload.

**.dockerignore** - Excludes unnecessary files from the Docker build context including pycache, .env, .venv and database files.

**.env.example** - Template showing required environment variables without exposing real secrets. The actual .env file is excluded from version control via .gitignore.

**app/config.py** - Loads environment variables from .env using python-dotenv and provides them to the rest of the application. Replaces all hardcoded values in database.py, security.py and main.py.


## Day 20 - API Testing, Logging & Documentation

**logger.py** - Centralized logging configuration that writes to both console and logs/application.log with timestamps and log levels.

**routes.py** - Enhanced Swagger documentation with descriptions, response models and status codes on every endpoint.

**main.py** - Added request logging middleware that logs method, endpoint, response status and execution time for every request.

**crud.py** - Added log statements for employee create, update and delete operations and error logs for not found cases.

**auth.py** - Added log statements for successful registration, successful login and failed login attempts.

**postman/Employee-Management-API.postman_collection.json** - Complete Postman collection with Auth, Employees and Health folders covering all endpoints.

**day-20/README.md** - Standalone README with project overview, tech stack, folder structure, installation guide, Docker instructions, endpoint table, authentication flow and sample curl requests.


## Day 21 - Week 3 Capstone: Employee Management REST API

**app/services/auth_service.py** - Business logic for user registration and authentication with bcrypt password hashing and login validation.

**app/services/employee_service.py** - Business logic for all employee CRUD operations, search, department filter and pagination.

**app/utils/id_generator.py** - Utility function for generating sequential employee IDs (E001, E002 etc).

**app/routes/auth_routes.py** - Auth endpoints - register, login and get current user - with full Swagger documentation.

**app/routes/employee_routes.py** - Employee endpoints - CRUD, search, department filter and pagination - with public and protected routes.

**app/main.py** - FastAPI app setup with request logging middleware, route registration and table auto-creation on startup.


# Day 22 - Introduction to LLMs & Prompt Engineering

## Files

**prompt_comparison.md** - Report comparing 10 different prompting techniques (simple, detailed, role-based, bullet format, structured output, tone-specific, audience-specific, one-shot, chain-of-thought, few-shot) applied to the same employee performance review summarization task, with outputs and observations documented.

**ai_assistant.py** - CLI application that accepts user input, sends it to a locally running Ollama model (llama3.2), and displays the generated response. Handles connection and generation errors gracefully.

**ai_utility.py** - Extended CLI utility offering 5 modes: Summarize Text, Generate Email, Explain Code, Improve Grammar, and Translate Text. Loads the matching prompt template from the prompts folder, fills in the user's input, and sends it to Ollama.

**prompts/summarization.txt** - Reusable prompt template for summarizing any given text.

**prompts/email_generation.txt** - Reusable prompt template for generating professional emails from context.

**prompts/code_review.txt** - Reusable prompt template for reviewing and explaining code, used by the Explain Code mode.

**prompts/translation.txt** - Reusable prompt template for translating text.

**prompts/grammar_correction.txt** - Reusable prompt template for correcting grammar, spelling, and punctuation while preserving tone.

**requirements.txt** - Python dependencies for this day, currently just the ollama library.

## Usage

```bash
python3 ai_assistant.py
python3 ai_utility.py
```


# Day 23 - AI-Powered APIs with FastAPI

**app/main.py** - FastAPI entry point, registers AI router and global exception handler.

**app/schemas.py** - Request and response models with empty input validation.

**app/routes/ai.py** - Endpoints for generate, summarize, translate, email, explain-code and chat.

**app/services/ai_service.py** - Connects to local Ollama model, loads prompts dynamically, maintains chat history.

**prompts/** - Reusable prompt templates for summarize, translate, email and explain-code.

**requirements.txt** - Python dependencies for this day.

Uses a local Ollama model instead of a paid API provider due to no available credits on OpenAI or Anthropic.


# Day 24 - Embeddings & Vector Databases

**app/embedding.py** - Generates text embeddings locally using sentence-transformers (all-MiniLM-L6-v2).

**app/vector_store.py** - ChromaDB persistent client and collection functions for adding and querying vectors using cosine similarity.

**app/search_service.py** - Performs semantic search with top N and minimum score filtering, and logs every search to logs/search.log.

**app/routes.py** - POST /search endpoint returning ranked documents with similarity scores and metadata.

**index_documents.py** - Reads all documents, generates embeddings and stores them in the vector database.

**search.py** - Standalone CLI search utility for testing semantic search outside the API.

**documents/** - 10 sample text documents covering Python, FastAPI, Docker, SQLAlchemy, Machine Learning, REST APIs, JWT, Git, NumPy and Pandas.

Uses sentence-transformers and ChromaDB running fully locally, no external API required.


# Day 25 - Building a RAG Assistant

**app/services/embedding_service.py** - Generates text embeddings locally using sentence-transformers.

**app/services/retrieval_service.py** - ChromaDB persistent client for storing and retrieving document embeddings using cosine similarity.

**app/services/llm_service.py** - Sends prompts to a local Ollama model and returns generated answers.

**app/services/rag_service.py** - Combines retrieval and generation, builds context-grounded prompts, logs every request, and maintains conversation history for chat.

**app/routes/rag.py** - POST /ai/ask for single-turn RAG question answering and POST /ai/chat for session-based conversational RAG.

**index_documents.py** - Indexes documents into the vector database.

**test_retrieval.py** - Standalone CLI to test document retrieval outside the API.

**documents/** - Same 10 technical documents used on Day 24, re-indexed for this day's vector database.

Combines FastAPI, ChromaDB and a local Ollama model into a full retrieval-augmented generation pipeline, answering questions grounded in the indexed documents with source attribution and logging.