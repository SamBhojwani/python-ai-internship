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
            name="documents",
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


def retrieve_documents(query_embedding: list, top_n: int = 3):
    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_n
    )

    output = []
    for i in range(len(results["ids"][0])):
        doc_id = results["ids"][0][i]
        document_text = results["documents"][0][i]
        distance = results["distances"][0][i]
        similarity_score = round(1 - distance, 4)
        output.append({
            "document": doc_id,
            "text": document_text,
            "score": similarity_score
        })

    return output