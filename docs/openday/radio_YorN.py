' mind reader


from microbit import *
import radio

# Turn on the radio
radio.on()
# Choose own group in pairs 0-255
radio.config(group=8)

while True:
    if button_a.was_pressed():
        radio.send("Y")
        display.show(Image.YES)
    elif button_b.was_pressed():
        radio.send("N")
        display.show(Image.NO)
    incoming_message = radio.receive()
    if incoming_message:
        if incoming_message == "Y":
            display.show(Image.YES)
        elif incoming_message == "N":
            display.show(Image.NO)