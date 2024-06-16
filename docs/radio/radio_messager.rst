====================================================
Radio messager
====================================================

String message
-------------------------

| Set up the group with a value 0-255 by changing the group value from 8 in: ``radio.config(group=8)``.
| Turn on the radio using: ``radio.on()``


.. code-block:: python
    
    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    # Initialize the alphabet
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    # Display the current letter
    display.show(ALPHABET[index])
    # Initialize the text string
    text = ""

    while True:
        # Check the tilt of the micro:bit
        if accelerometer.get_x() < -300:
            # If the micro:bit is tilted to the left, move to the previous letter
            index = (index - 1) % len(ALPHABET)
            # Short delay to allow the display to update
            sleep(300)
        elif accelerometer.get_x() > 300:
            # If the micro:bit is tilted to the right, move to the next letter
            index = (index + 1) % len(ALPHABET)
            # Short delay to allow the display to update
            sleep(300)
        # Display the current letter
        display.show(ALPHABET[index])

        # Check if the A button was pressed
        if button_a.was_pressed():
            # Add the current letter to the text string
            text += ALPHABET[index]
        # Check if button B was pressed
        elif button_b.was_pressed():
            # Send the text string via the radio
            radio.send(text)
            # scroll text sent
            display.scroll(text, delay=80)
            # Clear the text string
            text = ""

        # receive
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)

