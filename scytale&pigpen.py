import math
from typing import Callable












def scytale_encrypt(plain_text: str, key: int) -> str:
    """Enkripton duke rregulluar tekstin në një matricë me 'key' rreshta."""
    text = clean_input(plain_text)
    if not text: return ""
    
    num_cols = math.ceil(len(text) / key)
    text = text.ljust(key * num_cols, "X")
    
    cipher_text = [""] * num_cols
    for i, char in enumerate(text):
        cipher_text[i % num_cols] += char
    return "".join(cipher_text)

def scytale_decrypt(cipher_text: str, key: int) -> str:
    """Dekripton duke përdorur inversin e kolonave."""
    text = clean_input(cipher_text)
    if not text: return ""
    
    num_cols = math.ceil(len(text) / key)
    decoded = [""] * key
    for i, char in enumerate(text):
        decoded[i % key] += char
    return "".join(decoded).rstrip("X")

PIGPEN_DICT = {
    'A': '_|',  'B': '|_|', 'C': '|_',
    'D': '[|',  'E': '[-]', 'F': '|]',
    'G': 'T|',  'H': '|-|', 'I': '|T',
    'J': '._|', 'K': '.|_|', 'L': '._',
    'M': '.[|', 'N': '.[-]', 'O': '.|]',
    'P': '.T|', 'Q': '.|-|', 'R': '.|T',
    'S': 'V',   'T': '<',   'U': '>',   'V_': '^', 
    'W': '.V',  'X': '.<',  'Y': '.>',  'Z': '.^',
    '0': '||',  '1': '||.', '2': '||..', '3': '||...', 
    '4': '==',  '5': '==.', '6': '==..', '7': '==...',
    '8': '##',  '9': '##.'
}
PIGPEN_INV = {v: k for k, v in PIGPEN_DICT.items()}

def pigpen_encrypt(plain_text: str) -> str:
    text = plain_text.upper()
    result = []
    for char in text:
        if char == " ":
            result.append(" ")
        else:
            result.append(PIGPEN_DICT.get(char, char))
    return "/".join(result)

def pigpen_decrypt(cipher_text: str) -> str:
    parts = cipher_text.split("/")
    result = []
    for part in parts:
        part = part.strip()
        if part == "" or part == " ":
            result.append(" ")
        else:
            result.append(PIGPEN_INV.get(part, "?"))
    return "".join(result)

def main():
    print("="*50)
    print("SISTEMI KRIPTOGRAFIK: SCYTALE & PIGPEN")
    print("="*50)
    print("1. Scytale (Transpozicion)")
    print("2. Pigpen (Zëvendësim)")
    print("3. Dil")

    choice = get_menu_choice("Zgjedhja juaj: ", {"1", "2", "3"})

    if choice == "1":
        text = get_non_empty_input("\nShkruaj tekstin: ")
        max_k = max(1, len(clean_input(text)))
        key = get_integer_key(f"Jepni çelësin (1 - {max_k}): ", 1, max_k)
        
        enc = scytale_encrypt(text, key)
        dec = scytale_decrypt(enc, key)
        print(f"\n[REZULTATI SCYTALE]")
        print(f"Teksti i Enkriptuar: {enc}")
        print(f"Teksti i Dekriptuar: {dec}")

    elif choice == "2":
        text = get_validated_input("\nShkruaj tekstin): ", validate_pigpen_text)
        enc = pigpen_encrypt(text)
        dec = pigpen_decrypt(enc)
        print(f"\n[REZULTATI PIGPEN]")
        print(f"Simbolet: {enc}")
        print(f"Dekriptimi: {dec}")

    print("\nFaleminderit që përdorët programin!")

if __name__ == "__main__":
    main()
