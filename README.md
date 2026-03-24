# 🧠 Tokenizer Comparison Tool

This project explores how different Large Language Model (LLM) tokenizers work by comparing their tokenization strategies across multiple models.

---

## 🚀 Features

- Compare multiple tokenizers:
  - BERT (WordPiece)
  - GPT-2 (BPE)
  - Flan-T5
  - Starcoder
  - Phi-3
- Interactive CLI-based tool
- Token visualization with colored output
- Vocabulary size comparison

---

## 🏗️ Project Structure
Tokenizer/
├── src/
│ ├── main.py
│ ├── tokenizer_cli.py
│ ├── tokenizer_core.py
│ ├── visualization.py
│ └── helper.py
├── requirements.txt
├── README.md
├── .gitignore


---

## ▶️ How to Run

```bash
python -m src.main

🧪 Example Usage
Select a model (e.g., GPT-2)
Enter input text
View:
Tokens
Token IDs
Vocabulary size
Colored token visualization


🧠 Learning Outcomes
Understand how LLMs process text
Compare WordPiece vs BPE tokenization
Analyze tokenizer behavior on real-world text
