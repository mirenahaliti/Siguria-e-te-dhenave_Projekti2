import math

def scytale_encrypt(plain_text: str, key: int) -> str:
    """
    Enkriptimi Scytale funksionon duke e vendosur tekstin ne nje shkop (matrice).
    Key perfaqeson numrin e rreshtave rreth shkopit.
    """
    if key <= 0: return "Celesi duhet te jete > 0"
    
    text = normalize_text(plain_text)
    columns = math.ceil(len(text) / key)
    
    text = text.ljust(key * columns, 'X')
    
    cipher_text = [''] * columns
    for i, char in enumerate(text):
        cipher_text[i % columns] += char
        
    return "".join(cipher_text)

def scytale_decrypt(cipher_text: str, key: int) -> str:
    """Dekriptimi i Scytale duke perdorur te njejtin parim te kolonave."""
    if key <= 0: return ""
    
    columns = math.ceil(len(cipher_text) / key)
    decoded = [''] * key
    for i, char in enumerate(cipher_text):
        decoded[i % key] += char
        
    return "".join(decoded).rstrip('X')