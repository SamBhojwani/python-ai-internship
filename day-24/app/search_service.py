import time
import logging
import os
from app.embedding import generate_embedding
from app.vector_store import query_collection

LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

search_logger = logging.getLogger("search_logger")
search_logger.setLevel(logging.INFO)

if not search_logger.handlers:
    file_handler = logging.FileHandler(os.path.join(LOGS_DIR, "search.log"))
    formatter = logging.Formatter("%(asctime)s\nQuery: %(message)s")
    file_handler.setFormatter(formatter)
    search_logger.addHandler(file_handler)


def perform_search(query: str, n_results: int = 1):
    start_time = time.time()

    query_embedding = generate_embedding(query)
    results = query_collection(query_embedding, n_results=n_results)

    output = []
    for i in range(len(results["ids"][0])):
        doc_id = results["ids"][0][i]
        distance = results["distances"][0][i]
        similarity_score = round(1 - distance, 4)
        output.append({"document": doc_id, "score": similarity_score})

    response_time_ms = round((time.time() - start_time) * 1000, 2)

    search_logger.info(f"{query}\nResults Returned: {len(output)}\nResponse Time: {response_time_ms} ms\n")

    return output