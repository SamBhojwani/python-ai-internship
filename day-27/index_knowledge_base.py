import os
from app.services.embedding_service import generate_embedding
from app.services.vector_service import add_document, count_documents

KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "knowledge")


def index_knowledge_base():
    total_indexed = 0

    categories = sorted(os.listdir(KNOWLEDGE_DIR))

    for category in categories:
        category_path = os.path.join(KNOWLEDGE_DIR, category)
        if not os.path.isdir(category_path):
            continue

        filenames = sorted(f for f in os.listdir(category_path) if f.endswith(".txt"))

        for filename in filenames:
            filepath = os.path.join(category_path, filename)
            with open(filepath, "r") as f:
                content = f.read()

            embedding = generate_embedding(content)
            doc_id = f"{category}_{filename}"

            add_document(
                doc_id=doc_id,
                text=content,
                embedding=embedding,
                metadata={"filename": filename, "category": category}
            )
            total_indexed += 1
            print(f"Indexed: {category}/{filename}")

    print("\nIndexing complete.")
    print(f"Total documents indexed: {total_indexed}")
    print(f"Total documents in vector database: {count_documents()}")


if __name__ == "__main__":
    index_knowledge_base()