# Self Reflection

## Most valuable skill learned

Building a retrieval pipeline end to end, and understanding that retrieval quality sets the ceiling on answer quality. Before this internship I thought of RAG as a prompting technique. It is mostly an engineering problem: how documents are chunked and indexed, which distance metric the vector store uses, and how many documents get retrieved all matter more than the wording of the prompt.

## Biggest technical challenge

Losing access to commercial LLM APIs partway through the GenAI week. Both the OpenAI and Anthropic accounts required paid credits, and the assignments assumed one would be available. Rewriting the generation layer to run llama3.2 locally through Ollama was the fix, and it worked because model communication had been isolated in a single service function rather than spread across route handlers. That was the moment the value of separating layers stopped being theoretical.

## Where I improved the most

Debugging problems where nothing crashes. The similarity scores being wrong is the clearest example: the API returned correct rankings and a valid response every time, so nothing looked broken. Finding that ChromaDB defaults to squared L2 distance while my conversion assumed cosine required reasoning about what the numbers should look like rather than reading an error message. I also got better at reviewing my own work deliberately, which is how the unprotected delete endpoint was found.

## Technologies I want to explore further

Evaluation for RAG systems, since I measured retrieval depth by reading outputs and judging them myself rather than against a labelled set. Chunking strategies, since every document here was indexed whole and real documents are longer than that. PostgreSQL with pgvector, to understand where an embedded store stops being sufficient. And containerised deployment properly, since Ollama running on the host is a compromise rather than a design.

## Overall internship experience

The structure worked. Building daily and committing per assignment meant that by Week 4 the FastAPI, database and authentication work from Weeks 1 to 3 was already in hand, so the GenAI material could be about GenAI rather than fighting the backend. The parts I learned most from were the ones where something did not work as expected and I had to reason about why. Having a real constraint to design around, rather than a clean path through the assignments, made the final project more genuinely mine.