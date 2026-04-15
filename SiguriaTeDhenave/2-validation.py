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

def get_menu_choice(prompt: str, valid_choices: set[str]) -> str:
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Gabim: zgjidh vetëm {', '.join(sorted(valid_choices))}.")

def validate_pigpen_text(text: str) -> tuple[bool, list[str]]:
    invalid = sorted({ch for ch in text.upper() if ch not in ALLOWED_PIGPEN_CHARS})
    return (len(invalid) == 0, invalid)

def get_validated_input(prompt: str, validator: Callable[[str], tuple[bool, list[str]]]) -> str:
    while True:
        value = get_non_empty_input(prompt)
        ok, issues = validator(value)
        if ok:
            return value
        print(f"Gabim: karaktere të pambështetura -> {', '.join(issues)}")