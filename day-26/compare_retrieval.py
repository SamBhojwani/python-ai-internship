from app.services.embedding_service import generate_embedding
from app.services.retrieval_service import retrieve_documents
from app.services.llm_service import generate_answer

PROMPT_TEMPLATE = """You are a precise technical assistant that answers questions strictly using the provided context.

Instructions:
Answer ONLY using the information in the context below.
If the answer is not present in the context, respond exactly with: "I couldn't find this information in the provided documents."
Keep your answer concise and factual. Do not add information that is not supported by the context.

Context:
{retrieved_documents}

Question:
{user_question}
"""

TEST_QUESTION = "What tools are commonly used in a Python backend project?"
TOP_N_VALUES = [1, 3, 5]


def run_comparison():
    query_embedding = generate_embedding(TEST_QUESTION)

    print(f"Question: {TEST_QUESTION}\n")

    for top_n in TOP_N_VALUES:
        retrieved = retrieve_documents(query_embedding, top_n=top_n)
        context_text = "\n\n".join([r["text"] for r in retrieved])

        prompt = PROMPT_TEMPLATE.format(retrieved_documents=context_text, user_question=TEST_QUESTION)
        answer = generate_answer(prompt)

        print("=" * 60)
        print(f"TOP {top_n} RETRIEVAL")
        print("Documents retrieved:")
        for r in retrieved:
            print(f"  {r['document']} (score: {r['score']})")
        print(f"\nAnswer:\n{answer}\n")


if __name__ == "__main__":
    run_comparison()