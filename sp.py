import math

# --- FUNKSIONET NDIHMËSE ---
def normalize_text(text: str) -> str:
    """Heq hapesirat per te siguruar qe algoritmi te punoje paster."""
    return text.upper().replace(" ", "")
