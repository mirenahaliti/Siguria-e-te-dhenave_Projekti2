import math
from utils import clean_input
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