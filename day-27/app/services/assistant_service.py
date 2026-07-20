import os
from app.services.embedding_service import generate_embedding
from app.services.vector_service import query_collection, get_all_documents
from app.services.llm_service import generate_answer

PROMPT_TEMPLATE = """You are an enterprise knowledge assistant.
Answer ONLY using the information in the context below.
If the answer is not present in the context, respond exactly with: "I couldn't find this information in the provided documents."
Keep your answer concise and factual.

Context:
{retrieved_documents}

Question:
{user_question}
"""


def ask_assistant(question: str, top_n: int = 3, category: str = None):
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