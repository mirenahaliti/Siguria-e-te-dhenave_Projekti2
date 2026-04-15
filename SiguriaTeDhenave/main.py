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

def get_integer_key(prompt: str, min_value: int = 1, max_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Gabim: çelësi nuk mund të jetë bosh.")
            continue
        if not raw.lstrip("-").isdigit():
            print("Gabim: çelësi duhet të jetë numër i plotë.")
            continue

        key = int(raw)
        if key < min_value:
            print(f"Gabim: çelësi duhet të jetë >= {min_value}.")
            continue
        if max_value is not None and key > max_value:
            print(f"Gabim: çelësi duhet të jetë <= {max_value}.")
            continue
        return key
