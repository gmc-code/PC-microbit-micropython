from microbit import *
import radio


# Set radio group
radio.config(group=8)
# Set transmit power
radio.config(power=3)
radio.on()

while True:
    # Send the number 3
    radio.send("3")
    # Show the heart icon
    display.show(Image.HEART)
    # Pause for a moment
    sleep(1000)
    # Show the small heart icon
    display.show(Image.HEART_SMALL)
    # Pause for a moment
    sleep(1000)
