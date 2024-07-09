from microbit import *
import radio


# Set radio group
radio.config(group=8)
# Set the received message handler
radio.on()

# Create a list to store unique ids
unique_ids = list()

while True:
    incoming_message = radio.receive()
    if incoming_message:
        # If the message is not already in the list, append it
        if incoming_message not in unique_ids:
            unique_ids.append(incoming_message)
        display.scroll(incoming_message)
        sleep(200)
    if button_a.was_pressed():
        display.scroll("-")
        display.show(unique_ids, delay=300)
        display.scroll("-")

