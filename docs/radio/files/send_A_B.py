from microbit import *
import radio

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()

while True:
    # send
    if button_a.was_pressed():
        radio.send("A")
    elif button_b.was_pressed():
        radio.send("B")
    # receive
    incoming_message = radio.receive()
    if incoming_message is not None:
        display.scroll(incoming_message)
