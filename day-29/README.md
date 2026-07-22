# Enterprise AI Knowledge Assistant

## Project Overview

An enterprise-ready AI assistant that answers questions using an organization's own documents through Retrieval-Augmented Generation (RAG). Built across multiple stages of a 30-day internship, it combines semantic search, a locally running LLM, JWT authentication, conversation history, feedback collection and usage analytics into a single FastAPI application.

## Features

Question answering grounded in a 20 document knowledge base spanning HR, technical, policy, manual and FAQ categories
Category-scoped semantic search and question answering
JWT authenticated user registration and login
Persistent conversation history per user
Response feedback collection with 1 to 5 star ratings
Usage analytics including total requests, average response time, top category and average rating
Dynamic document upload and deletion with automatic re-indexing
Request logging with user, question, response time and status

## Technology Stack

FastAPI for the REST API layer
Ollama running llama3.2 locally for answer generation, no external API key required
sentence-transformers (all-MiniLM-L6-v2) for local text embeddings
ChromaDB as the persistent vector database
SQLAlchemy with SQLite for users, conversations and feedback
python-jose and bcrypt for JWT authentication and password hashing
Pydantic for request and response validation

## Installation

Clone the repository and navigate to this folder.

Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies.

```bash
python3 -m pip install -r requirements.txt
```

Install and start Ollama, then pull the model used for generation.

```bash
brew install ollama
ollama serve
ollama pull llama3.2
```

In a separate terminal, index the knowledge base.

```bash
export HF_HUB_OFFLINE=1
python3 index_knowledge_base.py
```

Start the API server.

```bash
python3 -m uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000/docs for interactive API documentation.

## Docker Setup

Build and run using Docker Compose.

```bash
docker compose up --build
```

This starts the API container. Ollama must be running on the host machine and accessible to the container, since the model runs outside the container for performance reasons.

## Environment Variables

See .env.example for required variables. Currently the application does not require external API keys since it uses a local Ollama model, but the .env.example file documents configuration such as the JWT secret key for production deployments.

## API Endpoints

### Authentication
POST /auth/register - create a new user account and receive an access token
POST /auth/login - authenticate and receive an access token

### Assistant
POST /assistant/ask - ask a question, answered using retrieved context (authenticated)
POST /assistant/search - semantic search without AI generation (authenticated)
GET /assistant/categories - list knowledge base categories
GET /assistant/documents - list all indexed documents
GET /assistant/history - view your past conversations (authenticated)
POST /assistant/feedback - rate a previous AI response (authenticated)
GET /assistant/analytics - view aggregate usage analytics

### Document Management
POST /documents/upload - upload and index a new document (authenticated)
GET /documents - list all indexed documents
DELETE /documents/{id} - remove a document (authenticated)

## Folder Structure

day-29/
├── app/
│ ├── routes/
│ │ ├── assistant.py
│ │ ├── documents.py
│ │ └── auth_routes.py
│ ├── services/
│ │ ├── embedding_service.py
│ │ ├── vector_service.py
│ │ ├── llm_service.py
│ │ ├── assistant_service.py
│ │ └── document_service.py
│ ├── models.py
│ ├── schemas.py
│ ├── security.py
│ ├── database.py
│ ├── dependencies.py
│ └── main.py
├── knowledge/
│ ├── hr/
│ ├── technical/
│ ├── policies/
│ ├── manuals/
│ └── faq/
├── vector_db/
├── logs/
├── reports/
├── index_knowledge_base.py
├── requirements.txt
└── README.md


## Example Requests

Register a user:

```bash
curl -X POST http://127.0.0.1:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "sam", "email": "sam@test.com", "password": "test1234"}'
```

Ask a question (replace TOKEN with the access_token from register or login):

```bash
curl -X POST http://127.0.0.1:8000/assistant/ask \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"question": "How many days of annual leave do I get?"}'
```

## Future Improvements

Move the JWT secret key and other configuration into environment variables loaded via python-dotenv rather than a hardcoded value, for safer production deployment.

Replace polling-based ChromaDB persistence with a hosted vector database for multi-instance deployments.

Add pagination to GET /assistant/history and GET /assistant/documents for larger datasets.

Add rate limiting to protect against API abuse, currently only discussed conceptually.

Support additional file formats for document upload beyond plain text, such as PDF and DOCX.