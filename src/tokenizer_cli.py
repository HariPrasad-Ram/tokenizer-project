from src.tokenizer_core import load_tokenizer, tokenize_text
from src.visualization import show_tokens

# ✅ Model list (this is your selection menu)
MODELS = [
    "bert-base-cased",
    "gpt2",
    "google/flan-t5-small",
    "bigcode/starcoder2-15b",
    "microsoft/Phi-3-mini-4k-instruct",
    "Qwen/Qwen2-VL-7B-Instruct",
    "Xenova/gpt-4"
]

def run_cli():
    print("=== TOKENIZER CLI TOOL ===\n")

    while True:
        # ✅ SHOW MODELS EVERY TIME
        print("\nAvailable Models:\n")
        for i, model in enumerate(MODELS):
            print(f"{i+1}. {model}")

        choice = input("\nSelect model number (or type 'exit'): ").strip()

        # ✅ EXIT OPTION
        if choice.lower() == "exit":
            print("Exiting... 👋")
            break

        # ✅ HANDLE NUMBER INPUT
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(MODELS):
                model = MODELS[index]
            else:
                print("Invalid number. Try again.")
                continue
        else:
            print("Please enter a valid number from the list.")
            continue

        # ✅ TAKE TEXT INPUT
        text = input("\nEnter text: ")

        # ✅ LOAD TOKENIZER
        try:
            tokenizer = load_tokenizer(model)
        except Exception as e:
            print("Error loading model:", e)
            continue

        # ✅ PROCESS TEXT
        tokens, ids, vocab_size = tokenize_text(tokenizer, text)

        print("\nSelected Model:", model)
        print("\nTokens:", tokens)
        print("\nToken IDs:", ids)
        print("\nVocabulary Size:", vocab_size)

        print("\n--- Visualization ---")
        show_tokens(text, model)