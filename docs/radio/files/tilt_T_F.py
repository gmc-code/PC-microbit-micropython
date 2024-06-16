from microbit import *
import radio

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()

while True:
    # send
    x_reading = accelerometer.get_x()
    if x_reading < -200:
        response = "T"
    elif x_reading > 200:
        response = "F"
    else:
        response = "-"
    display.show(response)
    if button_a.was_pressed():
        radio.send(response)
        sleep(100)
    # receive
    incoming_message = radio.receive()
    if incoming_message is not None:
        display.scroll(incoming_message)
        sleep(500)

