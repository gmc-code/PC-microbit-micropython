from microbit import *
import radio


# Set radio group
radio.config(group=8)
radio.on()

while True:
    incoming_message = radio.receive()
    if incoming_message:
        display.scroll(incoming_message)
        sleep(200)
