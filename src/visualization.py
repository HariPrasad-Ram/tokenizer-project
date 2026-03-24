from transformers import AutoTokenizer

colors = [
    '102;194;165', '252;141;98', '141;160;203',
    '231;138;195', '166;216;84', '255;217;47'
]

def show_tokens(text: str, tokenizer_name: str):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    token_ids = tokenizer(text).input_ids

    print(f"\nVocab Size: {len(tokenizer)}\n")

    for idx, token_id in enumerate(token_ids):
        print(
            f'\x1b[0;30;48;2;{colors[idx % len(colors)]}m'
            + tokenizer.decode(token_id)
            + '\x1b[0m',
            end=' '
        )
    print("\n")