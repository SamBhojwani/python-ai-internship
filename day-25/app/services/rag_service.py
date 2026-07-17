from app.services.embedding_service import generate_embedding
from app.services.retrieval_service import retrieve_documents
from app.services.llm_service import generate_answer

PROMPT_TEMPLATE = """You are an AI Assistant.
Use ONLY the following context to answer the question.

Context:
{retrieved_documents}

Question:
{user_question}
"""


def answer_question(question: str, top_n: int = 3):
    query_embedding = generate_embedding(question)
    retrieved = retrieve_documents(query_embedding, top_n=top_n)

    context_text = "\n\n".join([r["text"] for r in retrieved])

    final_prompt = PROMPT_TEMPLATE.format(
        retrieved_documents=context_text,
        user_question=question
    )

    answer = generate_answer(final_prompt)

    documents_used = [r["document"] for r in retrieved]
    sources = [{"document": r["document"], "score": r["score"]} for r in retrieved]

    return {
        "answer": answer,
        "documents_used": documents_used,
        "sources": sources,
        "retrieved_count": len(retrieved)
    }