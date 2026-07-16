import os
from app.embedding import generate_embedding
from app.vector_store import add_document, count_documents

DOCUMENTS_DIR = os.path.join(os.path.dirname(__file__), "documents")


def index_documents():
    filenames = sorted(os.listdir(DOCUMENTS_DIR))
    text_files = [f for f in filenames if f.endswith(".txt")]

    total_indexed = 0

    for filename in text_files:
        filepath = os.path.join(DOCUMENTS_DIR, filename)
        with open(filepath, "r") as f:
            content = f.read()

        embedding = generate_embedding(content)
        add_document(doc_id=filename, text=content, embedding=embedding, metadata={"filename": filename})
        total_indexed += 1
        print(f"Indexed: {filename}")

    print("\nIndexing complete.")
    print(f"Total documents indexed: {total_indexed}")
    print(f"Total embeddings created: {total_indexed}")
    print(f"Total documents in vector database: {count_documents()}")


if __name__ == "__main__":
    index_documents()