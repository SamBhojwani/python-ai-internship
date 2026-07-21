import os
from app.services.embedding_service import generate_embedding
from app.services.vector_service import query_collection, get_all_documents
from app.services.llm_service import generate_answer
from app.models import Conversation
from sqlalchemy.orm import Session
import time
from app.models import Feedback
from sqlalchemy import func

PROMPT_TEMPLATE = """You are an enterprise knowledge assistant.
Answer ONLY using the information in the context below.
If the answer is not present in the context, respond exactly with: "I couldn't find this information in the provided documents."
Keep your answer concise and factual.

Context:
{retrieved_documents}

Question:
{user_question}
"""


def ask_assistant(question: str, top_n: int = 3, category: str = None, db: Session = None, user_id: int = None):
    start_time = time.time()

    query_embedding = generate_embedding(question)
    results = query_collection(query_embedding, n_results=top_n, category=category)

    retrieved = []
    for i in range(len(results["ids"][0])):
        doc_id = results["ids"][0][i]
        document_text = results["documents"][0][i]
        distance = results["distances"][0][i]
        metadata = results["metadatas"][0][i]
        similarity_score = round(1 - distance, 4)
        retrieved.append({
            "document": metadata.get("filename", doc_id),
            "category": metadata.get("category", "unknown"),
            "text": document_text,
            "score": similarity_score
        })

    context_text = "\n\n".join([r["text"] for r in retrieved])
    final_prompt = PROMPT_TEMPLATE.format(retrieved_documents=context_text, user_question=question)
    answer = generate_answer(final_prompt)

    sources = [{"document": r["document"], "score": r["score"]} for r in retrieved]
    response_time_ms = round((time.time() - start_time) * 1000)

    if db is not None and user_id is not None:
        doc_category = retrieved[0]["category"] if retrieved else category
        conversation = Conversation(
            user_id=user_id,
            question=question,
            answer=answer,
            category=doc_category,
            response_time_ms=response_time_ms
        )
        db.add(conversation)
        db.commit()

    return {"answer": answer, "sources": sources}


def search_documents(query: str, top_n: int = 5, category: str = None):
    query_embedding = generate_embedding(query)
    results = query_collection(query_embedding, n_results=top_n, category=category)

    output = []
    for i in range(len(results["ids"][0])):
        doc_id = results["ids"][0][i]
        distance = results["distances"][0][i]
        metadata = results["metadatas"][0][i]
        similarity_score = round(1 - distance, 4)
        output.append({
            "document": metadata.get("filename", doc_id),
            "category": metadata.get("category", "unknown"),
            "score": similarity_score
        })

    return output


def list_categories():
    all_docs = get_all_documents()
    categories = set()
    for metadata in all_docs["metadatas"]:
        if metadata and "category" in metadata:
            categories.add(metadata["category"])
    return sorted(categories)


def list_documents():
    all_docs = get_all_documents()
    documents = []
    for doc_id, metadata in zip(all_docs["ids"], all_docs["metadatas"]):
        documents.append({
            "id": doc_id,
            "filename": metadata.get("filename", ""),
            "category": metadata.get("category", "unknown")
        })
    return documents


def get_user_history(db: Session, user_id: int):
    return db.query(Conversation).filter(Conversation.user_id == user_id).order_by(Conversation.timestamp.desc()).all()


def submit_feedback(db: Session, user_id: int, question_id: int, rating: int, comment: str = None):
    conversation = db.query(Conversation).filter(
        Conversation.id == question_id, Conversation.user_id == user_id
    ).first()

    if conversation is None:
        raise ValueError(f"No conversation found with id {question_id} for this user")

    feedback = Feedback(
        question_id=question_id,
        user_id=user_id,
        rating=rating,
        comment=comment
    )
    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    return feedback.id


def get_analytics(db: Session):
    total_requests = db.query(Conversation).count()

    avg_response_time = db.query(func.avg(Conversation.response_time_ms)).scalar()
    avg_response_time = round(avg_response_time, 2) if avg_response_time else 0.0

    top_category_row = (
        db.query(Conversation.category, func.count(Conversation.category).label("count"))
        .filter(Conversation.category.isnot(None))
        .group_by(Conversation.category)
        .order_by(func.count(Conversation.category).desc())
        .first()
    )
    top_category = top_category_row[0] if top_category_row else None

    avg_rating = db.query(func.avg(Feedback.rating)).scalar()
    avg_rating = round(avg_rating, 2) if avg_rating else None

    return {
        "total_requests": total_requests,
        "average_response_time_ms": avg_response_time,
        "top_category": top_category,
        "average_rating": avg_rating
    }