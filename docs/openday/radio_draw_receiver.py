from microbit import *
import radio


# Choose own group in pairs 0-255
radio.config(group=6)
# Turn on the radio
radio.on()

while True:
    incoming_message = radio.receive()
    if incoming_message:
        # print(incoming_message)
        i = Image(incoming_message)
        display.show(i)


