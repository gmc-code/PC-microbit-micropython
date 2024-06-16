from microbit import *
import radio

# Turn on the radio
radio.on()

def send_image(img):
    # Convert the image to a string
    img_str = str(img)
    # Send the string over the radio
    radio.send(img_str)

def receive_image():
    # Receive a message from the radio
    message = radio.receive()
    if message:
        # If a message was received, convert it back into an image
        img = Image(message)
        # Display the image
        display.show(img)

# Test the functions with an image
test_img = Image.HEART
send_image(test_img)

# On the receiving Micro:bit
receive_image()
