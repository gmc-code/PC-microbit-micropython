from microbit import *
import radio
import random

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()

# Define image_strings for Rock, Paper and Scissors
rock = '00000:09990:99999:09990:00000:'
paper = '99999:90009:90009:90009:99999:'
scissors = '99009:99090:00900:99090:99009:'

# Put the image_strings in a list
image_strings = [rock, paper, scissors]


def get_rps_image():
    image_string = random.choice(image_strings)
    return image_string


def send_image():
    image_string = get_rps_image()
    radio.send(image_string)


def receive_image():
    # Receive a message from the radio
    incoming = radio.receive()
    if incoming:
        try:
            display.show(Image(incoming))
        except:
            display.show(incoming, delay=100)


while True:
    if button_a.was_pressed():
        for _ in range(3):
            send_image()
            sleep(200)
        # sleep(500)
    # Receive the image
    receive_image()

w