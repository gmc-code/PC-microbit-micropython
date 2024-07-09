from microbit import *
import radio


# Set radio group
radio.config(group=8)
# Set the received message handler
radio.on()

# Create a list to store unique ids
unique_ids = list()


def sort_integer_strings(lst):
    # Convert the strings to integers and sort the list
    sorted_list = sorted(lst, key=int)
    return sorted_list


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
        for treasure_id in sort_integer_strings(unique_ids):
            display.scroll(treasure_id)
        display.scroll("-")
