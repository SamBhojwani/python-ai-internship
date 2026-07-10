# Employee Management API

A production-ready REST API built with FastAPI, SQLAlchemy, and JWT authentication. Supports full employee CRUD operations, user authentication, structured logging, and Docker deployment.

## Technology Stack

- **FastAPI** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Database
- **JWT** - Authentication via python-jose
- **bcrypt** - Password hashing
- **Docker** - Containerization
- **uvicorn** - ASGI server

## Project Structure
day-20/
├── app/
│   ├── auth.py          - User registration and login logic
│   ├── config.py        - Environment variable configuration
│   ├── crud.py          - Database operations for employees
│   ├── database.py      - SQLAlchemy engine and session setup
│   ├── dependencies.py  - JWT authentication dependency
│   ├── logger.py        - Centralized logging configuration
│   ├── main.py          - FastAPI app setup
│   ├── models.py        - SQLAlchemy database models
│   ├── routes.py        - API endpoint definitions
│   ├── schemas.py       - Pydantic request and response schemas
│   └── security.py      - Password hashing and JWT functions
├── logs/
│   └── application.log  - Application log file
├── postman/
│   └── Employee-Management-API.postman_collection.json
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── requirements.txt

## Installation

### Run Locally

```bash
git clone https://github.com/SamBhojwani/python-ai-internship
cd python-ai-internship/day-20
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Run with Docker

```bash
cp .env.example .env
docker compose up
```

## Environment Variables

Copy `.env.example` to `.env` and fill in the values:
DATABASE_URL=sqlite:///./employees.db
SECRET_KEY=your-secret-key-here
TOKEN_EXPIRE_MINUTES=30
APP_NAME=Employee API

## API Endpoints

### Auth
| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | /register | No | Register a new user |
| POST | /login | No | Login and get JWT token |
| GET | /me | Yes | Get current user info |

### Employees
| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | /employees | No | Get all employees (paginated) |
| GET | /employees/{id} | No | Get employee by ID |
| GET | /employees/search?name= | No | Search by name |
| GET | /employees/filter?department= | No | Filter by department |
| POST | /employees | Yes | Create employee |
| PUT | /employees/{id} | Yes | Update employee |
| DELETE | /employees/{id} | Yes | Delete employee |

## Authentication Flow

POST /register with username, email, password, role
POST /login with username and password
Copy the access_token from the response
Add header to protected requests: Authorization: Bearer <token>


## Sample Requests

Register:
```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "samarth", "email": "samarth@example.com", "password": "secret123", "role": "Admin"}'
```

Login:
```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "samarth", "password": "secret123"}'
```

Create Employee:
```bash
curl -X POST http://localhost:8000/employees \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Aman Sharma", "email": "aman@example.com", "department": "Engineering", "salary": 90000}'
```

## Swagger UI
http://localhost:8000/docs