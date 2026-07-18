# Prompt Optimization Comparison

## Original Prompt
You are an AI Assistant.
Use ONLY the following context to answer the question.
Context:
{retrieved_documents}
Question:
{user_question}

## Optimized Prompt
You are a precise technical assistant that answers questions strictly using the provided context.
Instructions:
Answer ONLY using the information in the context below.
If the answer is not present in the context, respond exactly with: "I couldn't find this information in the provided documents."
Keep your answer concise and factual. Do not add information that is not supported by the context.
Context:
{retrieved_documents}
Question:
{user_question}

## Test 1: In-Context Question

**Question:** Explain FastAPI.

Both prompts produced accurate, relevant answers grounded in the fastapi.txt document. The original prompt response was longer, using a numbered feature list and closing summary sentence. The optimized prompt response was more concise, using a shorter bullet list and no closing summary. Both were accurate, but the optimized version was noticeably more compact without losing key information.

## Test 2: Out-of-Context Question

**Question:** What is the capital of France?

This question has no relevant content in the indexed documents, so it tests hallucination handling.

The original prompt did not hallucinate, but it explained its own limitation in a roundabout way, describing what topics it does cover instead of clearly refusing. The optimized prompt gave the exact refusal specified in the instructions: "I couldn't find this information in the provided documents." This is more predictable and easier to handle programmatically, since the client can check for that specific string.

## Observations

Response Quality: Optimized prompt produced more consistent, predictable behavior, especially for out-of-context questions.
Response Length: Optimized prompt responses were shorter and more direct across both tests.
Accuracy: Both prompts were accurate on in-context questions. Neither hallucinated on the out-of-context question, but the optimized prompt's refusal was cleaner and more consistent with the instructed format.

## Conclusion

The optimized prompt is preferred for production use. Explicit refusal instructions produce a consistent, predictable output for out-of-context questions, which is easier to detect and handle in application code than a free-form explanation.