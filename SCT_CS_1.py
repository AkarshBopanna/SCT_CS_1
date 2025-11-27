
def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    # Reverse shift for decryption
    if mode == "decrypt":
        shift = -shift

    for char in text:
        # For uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # For lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        # For numbers, punctuation, spaces
        else:
            result += char

    return result


# Main program
if __name__ == "__main__":
    print("=== Caesar Cipher Program ===")
    message = input("Enter a message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_cipher(message, shift, "encrypt")
    decrypted = caesar_cipher(encrypted, shift, "decrypt")

    print("\nEncrypted message:", encrypted)
    print("Decrypted message:", decrypted)
