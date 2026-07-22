import ollama

MODEL_NAME = "llama3.2"
REQUEST_TIMEOUT = 30


def generate_answer(prompt: str) -> str:
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
        raise RuntimeError(f"Model error: {e}")
    except TimeoutError:
        raise RuntimeError("Request to the model timed out.")
    except ConnectionError:
        raise RuntimeError("Could not connect to Ollama. Please check that Ollama is running.")
    except Exception as e:
        raise RuntimeError(f"Unexpected error while generating response: {e}")