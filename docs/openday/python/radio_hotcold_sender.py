from microbit import *
import radio

radio.config(group=7)
radio.config(power=2)
radio.on()

radio_on = False  # Start with radio OFF

while True:

    # A turns radio ON
    if button_a.was_pressed():
        radio_on = True
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)

    # B turns radio OFF
    if button_b.was_pressed():
        radio_on = False
        display.clear()

    # Only send if radio is ON
    if radio_on:
        radio.send("7")
        # Pulse heart to show "ON" status
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)
    else:
        sleep(1000)
