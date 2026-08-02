# Python & AI Engineering Internship — 30 Days

> Thirty consecutive days at **Muthu Soft Labs**, from `csv_analyzer.py` on day one to a
> JWT-secured, Dockerised RAG knowledge assistant on day twenty-nine. **152 commits**, every
> day's work in its own folder.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-vector%20store-FF6B6B?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![commits](https://img.shields.io/badge/commits-152-success?style=flat-square)

**Intern:** Samarth Bhojwani · **Mentor:** Harish Kumar S · **Duration:** 30 days, remote

---

Most internship repos are a single zip of the final deliverable. This one is the whole climb,
committed daily, including the days that were just unit tests and the day spent fixing four
deliberately planted bugs. The interesting part is the arc: each week's project is built on
the previous week's code rather than starting fresh.

## Where it ends up

The final artefact (days 27 to 29) is an **Enterprise AI Knowledge Assistant**:

- **Retrieval-augmented generation** over a 20-document knowledge base spanning five categories,
  embedded with `sentence-transformers` (all-MiniLM-L6-v2) and stored in **ChromaDB** with
  cosine similarity and category-scoped filtering
- **JWT authentication** with bcrypt-hashed passwords, protecting ask, search and upload
- **Persistent conversation memory** per session, plus per-user history, feedback ratings and
  usage analytics in SQLite
- **Prompt hardening** — an optimised template with explicit refusal instructions, benchmarked
  against the baseline for hallucination on out-of-context questions
- **Runs fully locally** — Ollama for generation, sentence-transformers for embeddings, so there
  is no API key and no per-token cost
- **Containerised** with a Dockerfile, compose file and a documented deployment checklist

## The four weeks

| Week | Focus | Ends with |
| :-- | :-- | :-- |
| **1** · Days 1–7 | Python fundamentals, data structures, file and exception handling, OOP, unit testing, debugging | CLI **Personal Finance Tracker** with JSON persistence, logging and 18 unit tests |
| **2** · Days 8–14 | NumPy, Pandas, exploratory data analysis, data cleaning, feature engineering, scikit-learn | **Employee Salary Prediction System** comparing Linear Regression, Decision Tree and Random Forest end to end |
| **3** · Days 15–21 | FastAPI, Pydantic validation, SQLAlchemy ORM, JWT auth, Docker, API testing and documentation | **Employee Management REST API** — layered services, protected routes, Swagger docs, Postman collection |
| **4** · Days 22–29 | LLMs and prompt engineering, embeddings, vector databases, RAG, production hardening | **Enterprise AI Knowledge Assistant** (above) |

Day 30 was the presentation.

## Things worth opening

| | |
| :-- | :-- |
| [`day-26/`](day-26) | Two prompt templates and a written comparison of what changed when the refusal instructions were added, plus a retrieval-depth study showing top-3 beat top-1 and top-5 |
| [`day-13/`](day-13) | Model comparison across three algorithms with split-ratio, hyperparameter and cross-validation experiments, written up in `evaluation_report.md` |
| [`day-06/`](day-06) | Four deliberately planted bugs, each diagnosed and fixed with a test proving it: a discount not divided by 100, a reversed sort, `^` used for exponentiation, and a list mutated while iterating |
| [`day-29/`](day-29) | The consolidated final build with refactoring notes, an 18-endpoint manual test report and a deployment checklist |

## Running any given day

Each day is self-contained. The FastAPI days follow the same shape:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cd day-29
uvicorn app.main:app --reload     # http://127.0.0.1:8000/docs
```

Days 22 onward expect [Ollama](https://ollama.com) running locally with `llama3.2` pulled.
Days 24 onward build a local ChromaDB store on first index.

## Full daily log

Every day's scripts and what each one does: **[docs/daily-log.md](docs/daily-log.md)**.

---

<sub>Internship work by Samarth Bhojwani at Muthu Soft Labs.</sub>
