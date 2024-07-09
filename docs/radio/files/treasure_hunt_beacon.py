from microbit import *
import radio


# Set radio group and transmit power
radio.config(group=8, power=0)
radio.on()

treasure_id = "1"  # change the number string for each treasure beacon
display.scroll(treasure_id)


while True:
    radio.send(treasure_id)
    sleep(200)
