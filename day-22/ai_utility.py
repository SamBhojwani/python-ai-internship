import os
import ollama

MODEL_NAME = "llama3.2"
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")

MODES = {
    "1": ("Summarize Text", "summarization.txt"),
    "2": ("Generate Email", "email_generation.txt"),
    "3": ("Explain Code", "code_review.txt"),
    "4": ("Improve Grammar", "grammar_correction.txt"),
    "5": ("Translate Text", "translation.txt")
}


def load_prompt_template(filename):
    filepath = os.path.join(PROMPTS_DIR, filename)
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


def get_ai_response(prompt):
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error: Could not get a response from the AI. Details: {e}"


def show_menu():
    print("\nAI Utility - Choose a mode:")
    for key, (label, _) in MODES.items():
        print(f"{key}. {label}")
    print("6. Exit")


def main():
    print("AI-Powered CLI Utility")
    print("-" * 40)

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "6":
            print("Goodbye.")
            break

        if choice not in MODES:
            print("Invalid choice. Please select a number between 1 and 6.")
            continue

        label, filename = MODES[choice]
        template = load_prompt_template(filename)

        if template is None:
            print(f"Error: Prompt template {filename} not found.")
            continue

        user_input = input(f"\nEnter text for '{label}': ").strip()

        if not user_input:
            print("Please enter some text.")
            continue

        final_prompt = template.replace("{input_text}", user_input)

        print("\nThinking...")
        ai_response = get_ai_response(final_prompt)
        print(f"\nResult:\n{ai_response}")


if __name__ == "__main__":
    main()