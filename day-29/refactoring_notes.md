# Refactoring Notes

## Changes Made

Added docstrings to every route function across assistant.py and documents.py explaining what each endpoint does and whether authentication is required.

Fixed an inconsistency where DELETE /documents/{doc_id} was not protected by authentication while POST /documents/upload was. Added the same JWT dependency to delete for consistency.

Extracted the hardcoded valid_categories set in document_service.py into a module level VALID_CATEGORIES constant, making it reusable and easier to update in one place.

Improved spacing and readability across route files, which had become dense after multiple days of incremental edits without formatting passes.

## Known Intentional Duplication

GET /documents and GET /assistant/documents return the same data. This is intentional rather than a bug, the assignment structure explicitly calls for both an assistant router and a separate document management router. Documented here so it is not mistaken for oversight.

## Not Changed

Core RAG logic in assistant_service.py (retrieval, prompt construction, generation) was left as is, since it already had a single responsibility per function and no duplicated logic.