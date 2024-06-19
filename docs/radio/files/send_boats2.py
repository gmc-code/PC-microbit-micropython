from microbit import *
import radio

# Choose own group in pairs 0-255
radio.config(group=8)
# Turn on the radio
radio.on()

# Define the boat images as strings
boat1 = '05050:05050:05050:99999:09990'
boat2 = '00000:05050:05050:05050:99999'
boat3 = '00000:00000:05050:05050:05050'
boat4 = '00000:00000:00000:05050:05050'
boat5 = '00000:00000:00000:00000:05050'
boat6 = '00000:00000:00000:00000:00000'

sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
rising_boats = sinking_boats[::-1]

while True:
    if button_a.is_pressed():
        # Send each boat image over radio
        for boat in sinking_boats:
            radio.send(boat)
            sleep(500)  # Delay between each image
    elif button_b.is_pressed():
        # Send each boat image over radio
        for boat in rising_boats:
            radio.send(boat)
            sleep(500)  # Delay between each image
    else:
        # Receive the boat image
        received = radio.receive()
        if received in sinking_boats:
            # Convert the received string back to an image and display it
            display.show(Image(received))
