# python caesar shift


def caesar_shift(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
ciphertext = caesar_shift(plaintext.lower(), 3).upper()
print(f"plaintext: {plaintext}")
print(f"ciphertext: {ciphertext}")

# ciphertext: WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
