from microbit import *
import radio

# Turn on the radio
radio.on()
# Choose own group in pairs 0-255
radio.config(group=8)

# Initialize counters for A and B
counter_A = 0
counter_B = 0

while True:
    # send
    if button_a.was_pressed():
        radio.send("A")
        counter_A = 0
    elif button_b.was_pressed():
        radio.send("B")
        counter_B = 0
    # receive
    incoming_message = radio.receive()
    if incoming_message is not None:
        if incoming_message == "A" and counter_A < 5:
            radio.send("A")
            counter_A += 1
            display.show("A" + str(counter_A))
        elif incoming_message == "B" and counter_B < 5:
            radio.send("B")
            counter_B += 1
            display.show("B" + str(counter_B))
        sleep(250)

