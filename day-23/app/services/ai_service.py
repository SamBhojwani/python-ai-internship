import os
import ollama

MODEL_NAME = "llama3.2"
PROMPTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "prompts")


def generate_text(prompt: str) -> str:
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
    except ollama.ResponseError as e:
        raise RuntimeError(f"Model error: {e}")
    except Exception as e:
        raise RuntimeError(f"Could not connect to Ollama: {e}")


def load_prompt_template(filename: str) -> str:
    filepath = os.path.join(PROMPTS_DIR, filename)
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise RuntimeError(f"Prompt template {filename} not found")


def run_prompt_template(filename: str, input_text: str) -> str:
    template = load_prompt_template(filename)
    final_prompt = template.replace("{input_text}", input_text)
    return generate_text(final_prompt)