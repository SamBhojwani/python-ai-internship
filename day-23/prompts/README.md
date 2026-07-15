# Prompt Management

All prompts used by the AI service are stored as separate .txt files in this folder rather than hardcoded inside route or service functions.

summarize.txt is used by POST /ai/summarize
translate.txt is used by POST /ai/translate
email.txt is used by POST /ai/email
explain_code.txt is used by POST /ai/explain-code

Each template contains a {input_text} placeholder. The run_prompt_template function in app/services/ai_service.py loads the matching file at request time, replaces the placeholder with the user's input, and sends the final prompt to the model. This means prompts can be edited or extended without changing any code.