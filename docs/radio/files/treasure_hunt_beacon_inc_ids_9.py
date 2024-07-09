from microbit import *
import power
import radio
import random

# Set radio group and transmit power
radio.config(group=8, power=0)
# Set the received message handler
radio.on()

# start at random id, not always 1.
treasure_id = str(random.randint(1, 9))
display.show(treasure_id)
sleep(2000)
display.clear()


@run_every(s=5)
def send_id():
    radio.send(treasure_id)
    display.scroll(treasure_id)


@run_every(s=12)
def change_id():
    global treasure_id
    if int(treasure_id) == 9:
        treasure_id = str(1)
    else:
        treasure_id = str(int(treasure_id) + 1)
    radio.send(treasure_id)
    display.scroll(treasure_id)


min_ms = 60 * 1000
while True:
    # renew deep sleep every minute
    power.deep_sleep(wake_on=(button_a, button_b), ms=min_ms, run_every=True)
    # display treasure_id
    if button_a.was_pressed():
        display.scroll(treasure_id)
    # change treasure_id
    elif button_b.was_pressed():
        change_id()
