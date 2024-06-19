from microbit import *
import radio
import random

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()


# Function to extract numbers from the image string
def extract_image_string(image):
    # Convert the image to a string
    full_image_string = str(image)
    # Replace the colon and newline characters with an empty string
    image_string = full_image_string.replace("'", "").replace("\n", "").replace(" ", "").replace("(", "").replace(")", "").replace("Image", "")
    return image_string


# Define images for Rock, Paper and Scissors
rock = Image('00000:09990:99999:09990:00000:')
paper = Image('99999:90009:90009:90009:99999:')
scissors = Image('99009:99090:00900:99090:99009:')

# Put the images in a list
images = [rock, paper, scissors]


def get_rps_image():
    image = random.choice(images)
    return image


def send_image():
    img = get_rps_image()
    radio.send(extract_image_string(img))


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
        send_image()
    # Receive the image
    receive_image()
