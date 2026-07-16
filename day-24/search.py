from app.embedding import generate_embedding
from app.vector_store import query_collection


def semantic_search(query: str, n_results: int = 1):
    query_embedding = generate_embedding(query)
    results = query_collection(query_embedding, n_results=n_results)

    output = []
    for i in range(len(results["ids"][0])):
        doc_id = results["ids"][0][i]
        document = results["documents"][0][i]
        distance = results["distances"][0][i]
        similarity_score = 1 - distance

        output.append({
            "document": doc_id,
            "score": round(similarity_score, 4),
            "preview": document[:150].strip() + "..."
        })

    return output


def main():
    print("Semantic Search")
    print("-" * 40)

    while True:
        query = input("\nEnter search query (or 'exit' to quit): ").strip()

        if query.lower() == "exit":
            print("Goodbye.")
            break

        if not query:
            print("Please enter a query.")
            continue

        results = semantic_search(query, n_results=1)

        for r in results:
            print(f"\nMost relevant document: {r['document']}")
            print(f"Similarity score: {r['score']}")
            print(f"Preview: {r['preview']}")


if __name__ == "__main__":
    main()