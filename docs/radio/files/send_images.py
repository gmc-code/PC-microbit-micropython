from microbit import *
import radio

# Turn on the radio
radio.on()

def send_images(img_list):
    for img in img_list:
        # Convert the image to a string
        img_str = str(img)
        # Send the string over the radio
        radio.send(img_str)
        # Wait for a bit to avoid sending images too quickly
        sleep(100)

def receive_images():
    received_images = []
    while True:
        # Receive a message from the radio
        message = radio.receive()
        if message:
            # If a message was received, convert it back into an image
            img = Image(message)
            # Add the image to the list of received images
            received_images.append(img)
            # Display the image
            display.show(img)
        else:
            # If no message was received, break the loop
            break
    return received_images

# Test the functions with a list of images
test_images = [Image.HEART, Image.HAPPY, Image.SAD]
send_images(test_images)

# On the receiving microbit
received_images = receive_images()
