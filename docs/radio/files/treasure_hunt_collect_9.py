from microbit import *
import radio


# Set radio group
radio.config(group=8)
# Set the received message handler
radio.on()


def sort_string_numbers(lst):
    # Convert the strings to integers and sort the list
    sorted_list = sorted(lst, key=int)
    return sorted_list


# Create a set to store unique messages
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
        for treasure_id in sort_string_numbers(unique_ids):
            display.scroll(treasure_id)
        display.scroll("-")
    elif button_b.was_pressed():
        treasure_count = len(unique_ids)
        display.scroll("*")
        display.scroll(treasure_count)
        display.scroll("*")
