import time
import logging
import os
from app.services.embedding_service import generate_embedding
from app.services.retrieval_service import retrieve_documents
from app.services.llm_service import generate_answer

LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

rag_logger = logging.getLogger("rag_logger")
rag_logger.setLevel(logging.INFO)

if not rag_logger.handlers:
    file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "rag.log"))
    formatter = logging.Formatter("%(asctime)s\nQuestion: %(message)s")
    file_handler.setFormatter(formatter)
    rag_logger.addHandler(file_handler)

PROMPT_TEMPLATE = """You are an AI Assistant.
Use ONLY the following context to answer the question.

Context:
{retrieved_documents}

Question:
{user_question}
"""


def answer_question(question: str, top_n: int = 3):
    start_time = time.time()

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

    response_time_ms = round((time.time() - start_time) * 1000, 2)

    rag_logger.info(
        f"{question}\nRetrieved Documents: {documents_used}\nResponse Time: {response_time_ms} ms\n"
    )

    return {
        "answer": answer,
        "documents_used": documents_used,
        "sources": sources,
        "retrieved_count": len(retrieved)
    }

chat_sessions = {}


def chat_with_context(session_id: str, message: str, top_n: int = 3):
    start_time = time.time()

    if session_id not in chat_sessions:
        chat_sessions[session_id] = []

    query_embedding = generate_embedding(message)
    retrieved = retrieve_documents(query_embedding, top_n=top_n)
    context_text = "\n\n".join([r["text"] for r in retrieved])

    history_text = ""
    for turn in chat_sessions[session_id]:
        history_text += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n\n"

    final_prompt = f"""You are an AI Assistant.
Use ONLY the following context to answer the question.
Consider the previous conversation for context if relevant.

Previous Conversation:
{history_text}

Context:
{context_text}

Question:
{message}
"""

    answer = generate_answer(final_prompt)

    chat_sessions[session_id].append({"user": message, "assistant": answer})

    documents_used = [r["document"] for r in retrieved]
    sources = [{"document": r["document"], "score": r["score"]} for r in retrieved]

    response_time_ms = round((time.time() - start_time) * 1000, 2)

    rag_logger.info(
        f"{message}\nRetrieved Documents: {documents_used}\nResponse Time: {response_time_ms} ms\n"
    )

    return {
        "answer": answer,
        "documents_used": documents_used,
        "sources": sources,
        "retrieved_count": len(retrieved)
    }