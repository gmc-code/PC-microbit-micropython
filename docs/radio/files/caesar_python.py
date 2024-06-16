def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

ciphertext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
plaintext = caesar_shift(ciphertext.lower(), 3).upper()
print(f"Plaintext: {plaintext}")
