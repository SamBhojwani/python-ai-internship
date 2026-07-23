# Enterprise AI Knowledge Assistant
## Final Project Report

Intern: Samarth Bhojwani
Mentor: Harish Kumar S, Team Lead
Internship: 30-Day Applied AI and Python Engineering, Muthu Soft Labs
Repository: https://github.com/SamBhojwani/python-ai-internship

---

## 1. Project Overview

The Enterprise AI Knowledge Assistant is a backend application that answers employee questions using an organization's own internal documentation rather than an AI model's general training knowledge. It uses Retrieval-Augmented Generation, where a user question is converted into a vector, matched against an indexed document collection, and the most relevant documents are supplied to a language model as context before it produces an answer.

The practical problem it addresses is that internal knowledge in most organizations is scattered across HR policies, technical guides, SOPs and FAQs. Employees either search manually or ask a colleague. A general purpose AI assistant cannot help, because it has never seen those documents and will invent plausible answers instead. This project makes internal documents the only source the assistant is allowed to draw from, and returns the source documents alongside every answer so the user can verify it.

Target users are employees asking day to day questions such as leave entitlement, expense claim procedure or internal technical standards, and administrators who maintain the knowledge base by uploading and removing documents.

## 2. Objectives

Build a working RAG pipeline from document indexing through to answer generation.
Ground every response in retrieved organizational documents and prevent the model from answering from outside that context.
Return source attribution with similarity scores so answers are traceable rather than opaque.
Secure the AI endpoints so only authenticated users can query the knowledge base.
Persist conversation history per user and collect feedback on response quality.
Expose usage analytics for basic observability of how the assistant is being used.
Package the application so another developer can run it from the repository without prior context.

## 3. Architecture

The request flow is as follows.

A client sends an authenticated question to the FastAPI layer. The JWT dependency validates the bearer token and resolves the user. The question is passed to the assistant service, which converts it to an embedding using a local sentence-transformers model. That embedding is used to query ChromaDB, which returns the top three most similar documents by cosine similarity, optionally filtered to a single category. The retrieved document text is injected into a prompt template alongside the user question, and that prompt is sent to a locally running Ollama model. The generated answer is returned to the client together with the source document names and their similarity scores. In parallel, the conversation is written to SQLite and the request is written to the application log with user, response time and status.

The codebase is separated into three layers. Routes handle HTTP concerns only, including request parsing, status codes and authentication dependencies. Services hold the business logic, split by responsibility across embedding generation, vector storage and retrieval, LLM communication, RAG orchestration and document management. Models and schemas define the database tables and the request and response contracts respectively. No AI logic sits inside a route function.

Two storage systems run side by side and serve different purposes. ChromaDB stores document embeddings and answers similarity queries. SQLite stores users, conversations and feedback, which are relational records rather than semantic ones.

## 4. Technology Stack

FastAPI was chosen for the API layer because it generates interactive Swagger documentation automatically, validates requests through Pydantic without manual checks, and supports dependency injection, which made JWT authentication reusable across routes with a single dependency.

Ollama running llama3.2 was chosen as the language model provider because it runs entirely on the local machine with no API key and no per-request cost. This decision is discussed further under Challenges.

sentence-transformers with the all-MiniLM-L6-v2 model was chosen for embeddings because it runs locally, is small enough to load quickly, and is well suited to short passage similarity, which is what document retrieval requires.

ChromaDB was chosen as the vector database because it runs embedded with no separate server process, persists to a local directory, and supports metadata filtering, which is what makes category-scoped search possible.

SQLAlchemy with SQLite was chosen for relational storage because users, conversations and feedback have clear relationships and benefit from aggregate queries, which is how the analytics endpoint computes averages and groupings.

python-jose and bcrypt handle JWT signing and password hashing. Docker and Docker Compose package the application for consistent execution. Git and GitHub track the project across all thirty days with one commit per assignment.

## 5. Features

Retrieval-Augmented question answering over a 20 document knowledge base spanning HR, technical, policies, manuals and FAQ categories.

Source attribution returning document names, similarity scores and the number of documents retrieved for every answer.

Category-scoped retrieval, allowing a question to be restricted to a single knowledge domain through a query parameter.

Semantic search returning ranked documents without generating an answer, for cases where the user wants to locate a document rather than ask a question.

JWT authentication with user registration and login, protecting question answering, search, document upload and document deletion.

Persistent per-user conversation history, queryable through a dedicated endpoint.

Feedback collection allowing users to rate any previous response from one to five with an optional comment, linked to the original conversation record.

Usage analytics reporting total requests, average response time, most queried category and average feedback rating.

Document management supporting upload with automatic indexing and deletion with removal from both disk and the vector database.

Request logging capturing user, question, response time and status for every request.

## 6. Screenshots

Screenshots are located in the screenshots folder of this directory.

01 to 02 show the Swagger API surface and user registration.
03 to 05 show the registration and login responses returning JWT access tokens.
06 to 07 show an authenticated question returning an answer grounded in leave_policy.txt, with three source documents and their similarity scores.
08 to 09 show document upload with automatic indexing into the vector database.
10 shows the analytics endpoint reporting total requests, average response time, top category and average feedback rating.

## 7. Challenges

The most significant challenge was provider availability. The assignments assumed access to a commercial LLM API, and both the OpenAI and Anthropic accounts required paid credits before any request would succeed, returning quota errors on the first call. Rather than stall the project, the LLM layer was rewritten to use Ollama running llama3.2 locally. Because the code already isolated model communication inside a dedicated service function, the change touched one file rather than the whole application. The tradeoff is slower generation and a smaller model than a commercial API would provide, in exchange for zero cost and no external dependency.

Similarity scores were initially far lower than expected, around 0.25 for a document that was clearly the correct match. The cause was that ChromaDB defaults to squared L2 distance, and the conversion being applied assumed cosine distance. Rankings were correct but the scores were misleading. Recreating the collection with cosine similarity explicitly configured brought scores into the expected range.

The embedding model repeatedly stalled on startup with HTTP 504 errors while contacting the Hugging Face Hub, despite the model already being cached locally. The library was checking for metadata updates on every load. Setting HF_HUB_OFFLINE forced local-only loading and eliminated the delay.

Choosing retrieval depth required testing rather than assumption. A comparison across top one, top three and top five retrieval on the same broad question showed that top one caused the model to decline to answer because a single document lacked the needed detail, while top five introduced less relevant documents and reduced answer precision. Top three was selected as the default based on that comparison rather than an arbitrary choice.

During the final refactoring pass, a security inconsistency surfaced that had gone unnoticed while features were being added incrementally. The document upload endpoint required authentication but the document delete endpoint did not, meaning any unauthenticated caller could remove documents from the knowledge base. This was corrected and is documented in the refactoring notes.

## 8. Learnings

Retrieval quality determines answer quality. A well written prompt cannot compensate for retrieving the wrong documents, and most of the practical work in a RAG system is in the retrieval layer rather than the generation layer.

Explicit refusal instructions in a prompt materially change model behaviour. Comparing an original prompt against an optimized one showed that instructing the model to return a specific phrase when the answer is absent produced a consistent, machine-checkable response, whereas the original prompt produced a different free-form explanation each time.

Isolating external dependencies behind a service function pays off under pressure. Because LLM communication lived in one function, switching providers mid-project was a contained change rather than a rewrite.

Separating routes from services keeps a project navigable as it grows. By the final week the application had eleven endpoints, and locating logic remained straightforward because routes contained no business logic.

Incremental feature development introduces inconsistencies that only a deliberate review pass will surface. The unprotected delete endpoint was not caught by any single day's testing because each day only tested that day's additions.

## 9. Future Scope

Move the JWT secret key and other configuration out of source code into environment variables loaded at runtime, which is required before any production deployment.

Replace SQLite with PostgreSQL to support concurrent writes and multiple application instances.

Add role-based access control so administrators can manage documents while standard users can only query them, rather than the current model where any authenticated user can upload and delete.

Support additional document formats beyond plain text, including PDF and DOCX, with OCR for scanned documents.

Add pagination to conversation history and document listing endpoints, which currently return complete result sets.

Implement API rate limiting, which was covered conceptually during the internship but not built.

Deploy to a cloud environment with a CI/CD pipeline running the test suite on every commit, and add monitoring and alerting on response time and error rate.