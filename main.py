


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