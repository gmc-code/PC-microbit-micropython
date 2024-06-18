from microbit import *
import radio

# Turn on the radio
radio.on()

# Function to extract numbers from the image string
def extract_image_string(image):
    # Convert the image to a string
    image_string = str(image)
    # Replace the colon and newline characters with an empty string
    numbers = image_string.replace("'", '').replace('\n', '').replace(' ', '').replace('(', '').replace(')', '').replace('Image', '')
    return numbers


def send_image(img):
    # Convert the image to a string
    img_str = extract_image_string(img)
    # Send the string over the radio
    radio.send(img_str)

def receive_image():
    # Receive a message from the radio
    message = radio.receive()
    if message:
        # If a message was received, convert it back into an image
        # img = Image(message)
        # Display the image
        display.scroll(message)

while True:
    # send
    if button_a.was_pressed():
        # Test the functions with an image
        test_img = Image.HEART
        send_image(test_img)
    # On the receiving microbit
    receive_image()
    sleep(300)
