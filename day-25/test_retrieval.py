from app.services.embedding_service import generate_embedding
from app.services.retrieval_service import retrieve_documents


def main():
    print("Document Retrieval Test")
    print("-" * 40)

    while True:
        question = input("\nEnter your question (or 'exit' to quit): ").strip()

        if question.lower() == "exit":
            print("Goodbye.")
            break

        if not question:
            print("Please enter a question.")
            continue

        query_embedding = generate_embedding(question)
        results = retrieve_documents(query_embedding, top_n=3)

        print(f"\nQuestion: {question}")
        print("Retrieved Documents:")
        for r in results:
            print(f"{r['document']} (score: {r['score']})")


if __name__ == "__main__":
    main()