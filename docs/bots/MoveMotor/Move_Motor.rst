====================================================
Mu editor
====================================================

Mu editor is the simplest choice of windows apps to use when programming the microbit with micropython.

It can be downlaoded from: https://codewith.mu/en/download

Useful keyboard shortcuts are at: https://codewith.mu/en/tutorials/1.1/shortcuts

----
"""
    Repeatedly display random colours on the 4 LEDs connected to pin8.
"""

from microbit import *
import neopixel
import random


# Setup the Neopixel strip on pin8 with a length of 4 pixels
NUM_PIXELS = 4
LED_PIN = pin8
np = neopixel.NeoPixel(LED_PIN, NUM_PIXELS)

def front_lights():
    # LED 0 and 1; red, green and blue value between 0 and 255
    np[0] = (0, 255, 0)
    np[1] = (0, 255, 0)
    # Display the current pixel data on the Neopixel strip
    np.show()

def rear_lights():
    # LED 2 and 3; red, green and blue value between 0 and 255
    np[2] = (255, 0, 0)
    np[3] = (255, 0, 0)
    # Display the current pixel data on the Neopixel strip
    np.show()

def same_random_pixels():
    # Iterate over each LED in the strip
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    for pixel_id in range(NUM_PIXELS):
        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)
    # Display the current pixel data on the Neopixel strip
    np.show()


front_lights()
rear_lights()

while True:
    sleep(400)
    same_random_pixels()