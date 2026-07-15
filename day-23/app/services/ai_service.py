import os
import ollama

MODEL_NAME = "llama3.2"
PROMPTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "prompts")
REQUEST_TIMEOUT = 30


def generate_text(prompt: str) -> str:
    try:
        client = ollama.Client(timeout=REQUEST_TIMEOUT)
        response = client.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
    except ollama.ResponseError as e:
        if "not found" in str(e).lower():
            raise RuntimeError(f"Model '{MODEL_NAME}' is not available. Please run: ollama pull {MODEL_NAME}")
        raise RuntimeError(f"Model error: {e}")
    except TimeoutError:
        raise RuntimeError("Request to the model timed out. The model may be overloaded or unresponsive.")
    except ConnectionError:
        raise RuntimeError("Could not connect to Ollama. Please check that Ollama is running.")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while generating response: {e}")


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