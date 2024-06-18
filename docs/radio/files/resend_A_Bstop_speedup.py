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
# set the delay after showing a letter
showtime = 550

while True:
    # send
    if button_a.was_pressed():
        if showtime == 100:
            # reset delay after showing a letter
            showtime = 500
        else:
            # speed up letter display
            showtime = max(100, showtime - 50)
        # Send the showtime to all microbits
        radio.send('showtime:' + str(showtime))
        start_letter = random.choice(s)  # Choose a random letter from s
        radio.send(start_letter)  # Send the random letter
    # receive
    incoming_message = radio.receive()
    if incoming_message is not None:
        if incoming_message.startswith('showtime:'):
            # Update the showtime from the received message
            showtime = int(incoming_message.split(':')[1])
        elif button_b.was_pressed():
            # Clear the radio queue by calling radio.receive()
            while radio.receive() is not None:
                sleep(100)
        else:
            display.show(incoming_message)
            sleep(showtime)
            index_next = (s.index(incoming_message) + inc) % len(s)
            radio.send(s[index_next])
