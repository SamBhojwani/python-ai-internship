# API Test Report

## Summary

APIs Tested: 18
Passed: 18
Failed: 0

## Authentication

POST /auth/register with valid data -> 200, returns access_token. Passed.
POST /auth/register with duplicate username -> 400, rejected as expected. Passed.
POST /auth/login with correct credentials -> 200, returns access_token. Passed.
POST /auth/login with wrong password -> 401, rejected as expected. Passed.

## Assistant Endpoints

POST /assistant/ask without auth token -> 401, correctly blocked. Passed.
POST /assistant/ask with auth and a valid question -> 200, returns answer and sources with document names and similarity scores. Passed.
POST /assistant/ask with an empty question -> 422, rejected by Pydantic validation before reaching the AI service. Passed.
POST /assistant/search with auth -> 200, returns ranked semantic search results. Passed.
GET /assistant/categories -> 200, returns all 5 knowledge base categories. Passed.
GET /assistant/documents -> 200, returns all 20 indexed documents. Passed.
GET /assistant/history with auth -> 200, returns the authenticated user's past conversations ordered by most recent. Passed.
POST /assistant/feedback with a valid question_id -> 200, feedback stored successfully. Passed.
POST /assistant/feedback with an invalid question_id -> 404, correctly rejected since no matching conversation exists for that user. Passed.
GET /assistant/analytics -> 200, returns total requests, average response time, top category and average rating. Passed.

## Document Management

POST /documents/upload with auth -> 200, document saved to disk and indexed into the vector database. Passed.
POST /documents/upload with an invalid category -> 400, rejected with a clear error message listing valid categories. Passed.
DELETE /documents/{id} with auth on a real id -> 200, document removed from both disk and vector database. Passed.
DELETE /documents/{id} without auth -> 401, correctly blocked after the Day 29 refactor added authentication to this endpoint. Passed.

## Observations

Authentication is consistently enforced across all endpoints that were intended to be protected, including after fixing the DELETE /documents/{id} inconsistency found during refactoring.

Input validation via Pydantic correctly rejects empty or malformed requests with 422 before they reach business logic, avoiding wasted embedding or LLM calls.

Error responses are consistent in structure across the application, using FastAPI's standard detail field for all 400, 401, 404 and 422 responses.

No failures were found during this testing pass. The application is considered stable for the current feature set.