import ollama

MODEL_NAME = "llama3.2"


def get_ai_response(user_input):
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error: Could not get a response from the AI. Details: {e}"


def main():
    print("AI Text Assistant")
    print("Type 'exit' or 'quit' to stop.")
    print("-" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye.")
            break

        if not user_input:
            print("Please enter some text.")
            continue

        print("\nThinking...")
        ai_response = get_ai_response(user_input)
        print(f"\nAI: {ai_response}")


if __name__ == "__main__":
    main()