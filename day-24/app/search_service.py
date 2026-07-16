from app.embedding import generate_embedding
from app.vector_store import query_collection


def perform_search(query: str, n_results: int = 1):
    query_embedding = generate_embedding(query)
    results = query_collection(query_embedding, n_results=n_results)

    output = []
    for i in range(len(results["ids"][0])):
        doc_id = results["ids"][0][i]
        distance = results["distances"][0][i]
        similarity_score = round(1 - distance, 4)
        output.append({"document": doc_id, "score": similarity_score})

    return output