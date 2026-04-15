import math

def scytale_encrypt(plain_text: str, key: int) -> str:
    text = clean_input(plain_text)
    if not text: return ""
    
    num_cols = math.ceil(len(text) / key)

    text = text.ljust(key * num_cols, "X")
    
    cipher_text = [""] * num_cols
    for i, char in enumerate(text):
        cipher_text[i % num_cols] += char
    return "".join(cipher_text)


def scytale_decrypt(cipher_text: str, key: int) -> str:
    text = clean_input(cipher_text)
    if not text: return ""
    
    num_cols = math.ceil(len(text) / key)
   
    decoded = [""] * key
    for i, char in enumerate(text):
        decoded[i % key] += char
    return "".join(decoded).rstrip("X")