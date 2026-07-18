# Multi-Document Retrieval Comparison

## Test Question
What tools are commonly used in a Python backend project?

## Top 1 Retrieval

Documents retrieved: python.txt (score: 0.619)

Answer: The model correctly declined to answer, since python.txt alone does not mention specific backend tools by name. This shows top 1 retrieval can be too narrow for broad questions, missing relevant context that exists in other documents.

## Top 3 Retrieval

Documents retrieved: python.txt, sqlalchemy.txt, fastapi.txt

Answer: The model correctly identified SQLAlchemy and FastAPI as commonly used tools, grounded directly in the retrieved documents. This was the most accurate and focused answer of the three.

## Top 5 Retrieval

Documents retrieved: python.txt, sqlalchemy.txt, fastapi.txt, pandas.txt, numpy.txt

Answer: The model expanded the list to include FastAPI, SQLAlchemy, SQL and Pydantic. While still reasonably accurate, "SQL" was listed as if it were a separate tool rather than the underlying language SQLAlchemy works with, showing a slight drift in precision as more context was added.

## Conclusion

Top 1 retrieval is too narrow for broad questions and can cause the model to unnecessarily decline to answer. Top 5 retrieval adds more coverage but introduces minor precision issues as less directly relevant documents (pandas.txt, numpy.txt) get pulled into the context. Top 3 retrieval performed best for this question, balancing enough context to answer confidently without introducing noise from less relevant documents. Top 3 will remain the default for the /ai/ask and /ai/chat endpoints, while top 5 could be offered as an optional parameter for broader questions.