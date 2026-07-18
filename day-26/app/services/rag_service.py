import time
import logging
import os
import json
from app.services.embedding_service import generate_embedding
from app.services.retrieval_service import retrieve_documents
from app.services.llm_service import generate_answer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
CONVERSATIONS_DIR = os.path.join(BASE_DIR, "conversations")
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(CONVERSATIONS_DIR, exist_ok=True)

rag_logger = logging.getLogger("rag_logger")
rag_logger.setLevel(logging.INFO)

if not rag_logger.handlers:
    file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "rag.log"))
    formatter = logging.Formatter("%(asctime)s\nQuestion: %(message)s")
    file_handler.setFormatter(formatter)
    rag_logger.addHandler(file_handler)

PROMPT_TEMPLATE = """You are a precise technical assistant that answers questions strictly using the provided context.

Instructions:
Answer ONLY using the information in the context below.
If the answer is not present in the context, respond exactly with: "I couldn't find this information in the provided documents."
Keep your answer concise and factual. Do not add information that is not supported by the context.

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


def get_session_filepath(session_id: str) -> str:
    safe_id = "".join(c for c in session_id if c.isalnum() or c in ("-", "_"))
    return os.path.join(CONVERSATIONS_DIR, f"{safe_id}.json")


def load_session(session_id: str) -> list:
    filepath = get_session_filepath(session_id)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []


def save_session(session_id: str, history: list):
    filepath = get_session_filepath(session_id)
    with open(filepath, "w") as f:
        json.dump(history, f, indent=2)


def chat_with_context(session_id: str, message: str, top_n: int = 3):
    start_time = time.time()

    history = load_session(session_id)

    query_embedding = generate_embedding(message)
    retrieved = retrieve_documents(query_embedding, top_n=top_n)
    context_text = "\n\n".join([r["text"] for r in retrieved])

    history_text = ""
    for turn in history:
        history_text += f"User: {turn['user']}\nAssistant: {turn['assistant']}\n\n"

    final_prompt = f"""You are a precise technical assistant that answers questions strictly using the provided context.
Consider the previous conversation for context if relevant.
If the answer is not present in the context or conversation, respond exactly with: "I couldn't find this information in the provided documents."
Keep your answer concise and factual.

Previous Conversation:
{history_text}

Context:
{context_text}

Question:
{message}
"""

    answer = generate_answer(final_prompt)

    history.append({"user": message, "assistant": answer})
    save_session(session_id, history)

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

def get_history(session_id: str) -> list:
    return load_session(session_id)