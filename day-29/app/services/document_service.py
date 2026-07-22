import os
from app.services.embedding_service import generate_embedding
from app.services.vector_service import add_document, delete_document, get_all_documents

KNOWLEDGE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "knowledge")
VALID_CATEGORIES = {"hr", "technical", "policies", "manuals", "faq"}


def upload_document(filename: str, content: str, category: str):
    """Save a new document to disk under its category and index it into the vector database."""
    category = category.lower().strip()

    if category not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category '{category}'. Must be one of {sorted(VALID_CATEGORIES)}")

    category_dir = os.path.join(KNOWLEDGE_DIR, category)
    os.makedirs(category_dir, exist_ok=True)

    filepath = os.path.join(category_dir, filename)
    with open(filepath, "w") as f:
        f.write(content)

    embedding = generate_embedding(content)
    doc_id = f"{category}_{filename}"

    add_document(
        doc_id=doc_id,
        text=content,
        embedding=embedding,
        metadata={"filename": filename, "category": category}
    )

    return {"id": doc_id, "filename": filename, "category": category}


def remove_document(doc_id: str):
    """Remove a document from the vector database and delete its file from disk."""
    all_docs = get_all_documents()

    if doc_id not in all_docs["ids"]:
        raise ValueError(f"Document with id '{doc_id}' not found")

    index = all_docs["ids"].index(doc_id)
    metadata = all_docs["metadatas"][index]
    filename = metadata.get("filename")
    category = metadata.get("category")

    delete_document(doc_id)

    if filename and category:
        filepath = os.path.join(KNOWLEDGE_DIR, category, filename)
        if os.path.exists(filepath):
            os.remove(filepath)

    return {"id": doc_id, "deleted": True}