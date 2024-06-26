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


images = [Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED, Image.ANGRY, Image.ASLEEP, Image.SURPRISED, Image.SILLY, Image.FABULOUS, Image.MEH]


def get_rand_images(num):
    # num must be less than len(images)
    new_images = []
    while len(new_images) < num:
        image = random.choice(images)
        if image not in new_images:
            new_images.append(image)
    return new_images


def send_image():
    for img in get_rand_images(5):  # Send 5 images
        radio.send(extract_image_string(img))
        sleep(500)  # Delay between each image


def receive_image():
    # Receive a message from the radio
    incoming = radio.receive()
    if incoming:
        try:
            display.show(Image(incoming))
        except:
            display.show(incoming, delay=100)


while True:
    if button_a.is_pressed():
        send_image()
    # Receive the image
    receive_image()
