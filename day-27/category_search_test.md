# Category-Based Search Test

## Test Question
What tools should I use for my project?

## Without Category Filter
This question could plausibly retrieve documents from multiple categories, including technical/ and manuals/ (e.g. coding_standards.txt), since both discuss tools and practices.

## With category=technical Filter
Request: POST /assistant/ask?category=technical

Retrieved sources were correctly limited to the technical category only:
fastapi_guide.txt (score: 0.2637)
database_documentation.txt (score: 0.2286)
git_guide.txt (score: 0.2264)

No documents from manuals, hr, policies or faq were included, confirming the category filter is correctly applied at the vector database query level using ChromaDB's where clause on the category metadata field.

## Conclusion
Category-based search works as expected, restricting retrieval to a single knowledge category when specified, useful for narrowing an enterprise assistant's scope when the user already knows which domain their question falls under.