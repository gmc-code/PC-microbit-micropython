from microbit import *
import radio
import random  # Import the random module

# Turn on the radio
radio.on()
# Choose own group in pairs 0-255
radio.config(group=8)

# Define the string
s = "ABCDEFG"
# Initialize the index
inc = 1
# Initialize the time to display a letter
showtime = 400

while True:
    # send
    if button_a.was_pressed():
        start_letter = random.choice(s)  # Choose a random letter from s
        radio.send(start_letter)  # Send the random letter
    # receive
    incoming_message = radio.receive()
    if incoming_message is not None:
        if button_b.was_pressed():
            # Clear the radio queue by calling radio.receive()
            while radio.receive() is not None:
                sleep(100)
        else:
            display.show(incoming_message)
            sleep(showtime)
            index_next = (s.index(incoming_message) + inc) % len(s)
            radio.send(s[index_next])
