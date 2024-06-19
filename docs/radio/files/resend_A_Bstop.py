from microbit import *
import radio

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()

# Define the string
s = "ABCDEFG"
# set the index steps
inc = 1
# set the delay after showing a letter
showtime = 400

while True:
    # send
    if button_a.was_pressed():
        radio.send(s[0])   # start at start       
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
