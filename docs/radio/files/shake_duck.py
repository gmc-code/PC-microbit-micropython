from microbit import *
import radio

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()

while True:
    # sender
    if accelerometer.was_gesture('shake'):
        display.clear()
        radio.send("duck")
    # receiver
    incoming_message = radio.receive()
    if incoming_message:
        display.show(Image.DUCK)
