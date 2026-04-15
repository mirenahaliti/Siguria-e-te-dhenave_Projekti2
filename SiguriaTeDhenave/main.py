import math
from typing import Callable

ALLOWED_PIGPEN_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")

def clean_input(text: str, remove_spaces: bool = True) -> str:
    text = text.upper().strip()
    return text.replace(" ", "") if remove_spaces else text

def get_non_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Gabim: input-i nuk mund të jetë bosh.")
