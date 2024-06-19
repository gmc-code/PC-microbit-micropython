from microbit import *
import radio
import random

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()

# Caesar cipher letters
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# secrets to be chosen from
SECRETS = [
    "MEET AT DAWN",
    "THE BIRD HAS FLOWN",
    "TRUST NO ONE",
    "SEEK THE TRUTH",
    "SECURE THE ASSET",
    "AVOID DETECTION",
    "KEEP MOVING",
    "STAY HIDDEN",
    "WATCH YOUR BACK",
    "TIME IS KEY",
]
# Caesar cipher shift to be chosen from
SHIFTS = [-1, 1]


def caesar_cipher(message, shift):
    """
    Apply a Caesar cipher to a message.
    """
    cipher_text = ""
    for char in message:
        if char in ALPHABET:
            # Shift character
            index = (ALPHABET.index(char) + shift) % len(ALPHABET)
            cipher_text += ALPHABET[index]
        else:
            cipher_text += char
    return cipher_text


# Initialize timer
timer = 0

while True:
    # Check button presses to send a secret message
    if button_a.was_pressed():
        # Select a random shift
        shift = random.choice(SHIFTS)
        # Select a random secret message
        secret = random.choice(SECRETS)
        cipher_text = caesar_cipher(secret, shift)
        radio.send(cipher_text)
        # Display the secret message on the sender's microbit
        display.scroll(secret, delay=100)
        # Start the timer
        timer = running_time()
    elif button_b.was_pressed() and timer:
        # time must be not 0; so A button must be pressed first
        # Stop the timer and display the elapsed time in seconds
        elapsed_time = int((running_time() - timer) / 1000)
        display.scroll(str(elapsed_time))
        timer = 0
    # Check for incoming messages
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming, delay=100)
