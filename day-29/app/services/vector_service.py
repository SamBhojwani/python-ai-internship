import chromadb
import os

VECTOR_DB_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "vector_db")

_client = None
_collection = None


def get_collection():
    global _client, _collection
    if _client is None:
        _client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
    if _collection is None:
        _collection = _client.get_or_create_collection(
            name="knowledge_base",
            metadata={"hnsw:space": "cosine"}
        )
    return _collection


def add_document(doc_id: str, text: str, embedding: list, metadata: dict = None):
    collection = get_collection()
    collection.add(
        ids=[doc_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata or {}]
    )


def delete_document(doc_id: str):
    collection = get_collection()
    collection.delete(ids=[doc_id])


def query_collection(query_embedding: list, n_results: int = 3, category: str = None):
    collection = get_collection()
    where_filter = {"category": category} if category else None
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        where=where_filter
    )
    return results


def get_all_documents():
    collection = get_collection()
    return collection.get()


def count_documents():
    collection = get_collection()
    return collection.count()