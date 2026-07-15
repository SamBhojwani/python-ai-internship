import ollama

MODEL_NAME = "llama3.2"


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