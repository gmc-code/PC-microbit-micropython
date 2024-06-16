====================================================
Radio manual messages
====================================================

Letter tilting
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
        # Check the tilt of the microbit
        if accelerometer.get_x() < -200:
            # If the microbit is tilted to the left, move to the previous letter
            index = (index - 1) % len(ALPHABET)
            # Short delay to allow the display to update
            sleep(900)
        elif accelerometer.get_x() > 200:
            # If the microbit is tilted to the right, move to the next letter
            index = (index + 1) % len(ALPHABET)
            # Short delay to allow the display to update
            sleep(900)
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

----

.. admonition:: Exercises

    #. Send a single word to your partner.
    #. Send a a 3 to 5 word phrase to your partner.

----

.. admonition:: Tasks

    #. Modify the code to reduce the sleep time as the tilting increases with a minimum of 200 and a maximum of 900 sleep.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to reduce the sleep time as the tilting increases with a minimum of 200 and a maximum of 900 sleep.

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
                        # Check the tilt of the microbit
                        tilt = accelerometer.get_x()
                        if tilt < -200:
                            # If the microbit is tilted to the left, move to the previous letter
                            index = (index - 1) % len(ALPHABET)
                            # The more it's tilted, the faster the letter changes
                            sleep_time = max(200, 900 + int(tilt + 200))
                            # Short delay to allow the display to update
                            sleep(sleep_time)
                        elif tilt > 200:
                            # If the microbit is tilted to the right, move to the next letter
                            index = (index + 1) % len(ALPHABET)
                            # The more it's tilted, the faster the letter changes
                            sleep_time = max(200, 900 - int(tilt - 200))
                            # Short delay to allow the display to update
                            sleep(sleep_time)
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
