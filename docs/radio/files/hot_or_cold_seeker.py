
from microbit import *
import radio


# Set radio group
radio.config(group=8)
radio.on()

# Function to handle received messages
def on_received_message():
    incoming_full_details = radio.receive_full()
    if incoming_full_details:
        msg, rssi, timestamp = incoming_full_details
        # Show the signal strength
        display.scroll(rssi, delay=60)

while True:
    # received
    on_received_message()
    sleep(200)
