# RAG Assistant Evaluation Report

## Overview
This report documents the testing and evaluation performed while enhancing the RAG Assistant with conversation memory, prompt optimization, and multi-document retrieval.

## Questions Asked

1. What is FastAPI used for? (conversation memory test, turn 1)
2. Does it work well with the database tool we discussed earlier? (conversation memory test, turn 2, session context dependent)
3. Explain FastAPI. (prompt optimization test, in-context question)
4. What is the capital of France? (prompt optimization test, out-of-context question)
5. What tools are commonly used in a Python backend project? (multi-document retrieval test, run at top 1, top 3 and top 5)

## Retrieved Documents

Question 1 and 2 (session test1): fastapi.txt, sqlalchemy.txt, pandas.txt, git.txt, docker.txt depending on turn
Question 3: fastapi.txt, sqlalchemy.txt, python.txt
Question 4: no directly relevant documents retrieved, since the question falls outside the indexed topics
Question 5, Top 1: python.txt
Question 5, Top 3: python.txt, sqlalchemy.txt, fastapi.txt
Question 5, Top 5: python.txt, sqlalchemy.txt, fastapi.txt, pandas.txt, numpy.txt

## AI Responses

Question 2 correctly linked FastAPI to SQLAlchemy using prior conversation context, confirming that persistent session memory works across turns.

Question 3 was answered accurately by both the original and optimized prompts, with the optimized version producing a more concise response.

Question 4 was correctly declined by both prompts. The optimized prompt gave a clean, consistent refusal message, while the original prompt gave a longer, less predictable explanation of its own limitations.

Question 5 showed a clear progression: Top 1 failed to answer, Top 3 gave an accurate and focused answer, and Top 5 gave a broader but slightly less precise answer.

## Observations

Relevance: Retrieved documents were consistently relevant to the questions asked, confirming the embedding and retrieval pipeline from Days 24 and 25 works correctly.
Accuracy: The optimized prompt was more accurate in its refusal behavior on out-of-context questions. Multi-document retrieval accuracy peaked at top 3 for the tested question.
Completeness: Top 5 retrieval provided the most complete document coverage but at a slight cost to answer precision.
Clarity: The optimized prompt produced clearer, more consistent responses overall, particularly for out-of-context questions where a predictable refusal format is more useful than a free-form explanation.

## Improvements Made

Replaced in-memory session storage with persistent JSON files in conversations/, so chat history survives server restarts.
Replaced the original prompt template with an optimized version that includes explicit refusal instructions for out-of-context questions, producing shorter and more predictable responses.
Confirmed top 3 retrieval as the best default balance of accuracy and focus for this document set, based on direct comparison against top 1 and top 5.