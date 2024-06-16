from microbit import *
import radio
import random


# Turn on the radio
radio.on()
# Choose own group in pairs 0-255
radio.config(group=8)

# polybius cipher letters
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


# Define the Polybius square
polybius_square = {
    "A": (0, 0),
    "B": (1, 0),
    "C": (2, 0),
    "D": (3, 0),
    "E": (4, 0),
    "F": (0, 1),
    "G": (1, 1),
    "H": (2, 1),
    "I": (3, 1),
    "J": (4, 1),
    "K": (0, 2),
    "L": (1, 2),
    "M": (2, 2),
    "N": (3, 2),
    "O": (4, 2),
    "P": (0, 3),
    "Q": (1, 3),
    "R": (2, 3),
    "S": (3, 3),
    "T": (4, 3),
    "U": (0, 4),
    "V": (1, 4),
    "W": (2, 4),
    "X": (3, 4),
    "Y": (4, 4),
    "Z": (0, 0),  # Z is usually replaced with A in a Polybius square
}


def polybius_cipher(message):
    cipher_img_list = []
    for char in message:
        if char in ALPHABET:
            # Get the coordinates for the letter
            x, y = polybius_square[letter.upper()]
            # Create an empty image
            img = Image("00000:" * 5)
            # Set the pixel at the coordinates to 9
            img.set_pixel(x, y, 9)
            cipher_img_list.append(img)
        else:
            img = Image("00000:" * 5)
            cipher_img_list.append(img)
    return cipher_img_list


# Initialize timer
timer = 0

while True:
    # Check button presses to send a secret message
    if button_a.was_pressed():
        # Select a random shift
        shift = random.choice(SHIFTS)
        # Select a random secret message
        secret = random.choice(SECRETS)
        cipher_text = polybius_cipher(secret, shift)
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
        display.show(incoming, delay=100)
