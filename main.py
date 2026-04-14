import math
from typing import Callable

# ==========================================================
# MENAXHIMI I INPUTEVE DHE VALIDIMI
# ==========================================================

ALLOWED_PIGPEN_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")


def clean_input(text: str, remove_spaces: bool = True) -> str:
    """Pastron tekstin nga hapësirat dhe e kthen në shkronja të mëdha."""
    text = text.upper().strip()
    return text.replace(" ", "") if remove_spaces else text


def get_non_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Gabim: Input-i nuk mund të jetë bosh.")


def get_integer_key(prompt: str, min_value: int = 1, max_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        if not raw or not raw.lstrip("-").isdigit():
            print("Gabim: Çelësi duhet të jetë një numër i plotë.")
            continue
        key = int(raw)
        if key < min_value or (max_value and key > max_value):
            print(f"Gabim: Çelësi duhet të jetë midis {min_value} dhe {max_value}.")
            continue
        return key


def get_menu_choice(prompt: str, valid_choices: set[str]) -> str:
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Gabim: Zgjidhni një nga opsionet: {', '.join(sorted(valid_choices))}")


def validate_pigpen_text(text: str) -> tuple[bool, list[str]]:
    invalid = sorted({ch for ch in text.upper() if ch not in ALLOWED_PIGPEN_CHARS})
    return (len(invalid) == 0, invalid)


def get_validated_input(prompt: str, validator: Callable[[str], tuple[bool, list[str]]]) -> str:
    while True:
        value = get_non_empty_input(prompt)
        ok, issues = validator(value)
        if ok:
            return value
        print(f"Gabim: Karaktere të pambështetura -> {', '.join(issues)}")


# ==========================================================
# SCYTALE CIPHER (Transposition)
# ==========================================================

def scytale_encrypt(plain_text: str, key: int) -> str:
    """Enkripton duke rregulluar tekstin në një matricë me 'key' rreshta."""
    text = clean_input(plain_text)
    if not text: return ""

    num_cols = math.ceil(len(text) / key)
    # Mbushim tekstin me 'X' që të plotësohet matrica
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
    # Dekriptimi i Scytale është enkriptim me numrin e kolonave si çelës
    decoded = [""] * key
    for i, char in enumerate(text):
        decoded[i % key] += char
    return "".join(decoded).rstrip("X")


# ==========================================================
# PIGPEN CIPHER (Substitution)
# ==========================================================

PIGPEN_DICT = {
    'A': '_|', 'B': '|_|', 'C': '|_',
    'D': '[|', 'E': '[-]', 'F': '|]',
    'G': 'T|', 'H': '|-|', 'I': '|T',
    'J': '._|', 'K': '.|_|', 'L': '._',
    'M': '.[|', 'N': '.[-]', 'O': '.|]',
    'P': '.T|', 'Q': '.|-|', 'R': '.|T',
    'S': 'V', 'T': '<', 'U': '>', 'V_': '^',
    'W': '.V', 'X': '.<', 'Y': '.>', 'Z': '.^',
    '0': '||', '1': '||.', '2': '||..', '3': '||...',
    '4': '==', '5': '==.', '6': '==..', '7': '==...',
    '8': '##', '9': '##.'
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


# ==========================================================
# NDËRFAQJA KRYESORE (Main)
# ==========================================================

def main():
    print("=" * 50)
    print("SISTEMI KRIPTOGRAFIK: SCYTALE & PIGPEN")
    print("=" * 50)
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
        text = get_validated_input("\nShkruaj tekstin (A-Z, 0-9): ", validate_pigpen_text)
        enc = pigpen_encrypt(text)
        dec = pigpen_decrypt(enc)
        print(f"\n[REZULTATI PIGPEN]")
        print(f"Simbolet: {enc}")
        print(f"Dekriptimi: {dec}")

    print("\nFaleminderit që përdorët programin!")


if __name__ == "__main__":
    main()