from transformers import AutoTokenizer

def load_tokenizer(model_name: str):
    return AutoTokenizer.from_pretrained(model_name)

def tokenize_text(tokenizer, text: str):
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer(text).input_ids
    vocab_size = len(tokenizer)

    return tokens, token_ids, vocab_size