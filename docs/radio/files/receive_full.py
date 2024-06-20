from microbit import *
import radio

radio.on()
radio.config(group=8, length=251)


while True:
    # send
    if button_a.was_pressed():
        radio.send('hello')
    # receive
    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details
        display.scroll(msg)
        display.scroll(rssi)
        display.scroll(timestamp)
