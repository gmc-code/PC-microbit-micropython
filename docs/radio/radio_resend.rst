====================================================
Radio resend
====================================================

Back and forth messaging
---------------------------

| The code below creates a continuous conversation between 2 microbits that might seem like an infinite loop as the messages might be sent back and forth indefinitely.
| If two microbits are running this code and one sends a message "A", the other will receive it, display it, and then send a message "B". 
| Then the first microbit will receive "B", display it, and send "A" again. 
| This could go on indefinitely, but it's controlled by the sleep(250) command which introduces a delay of 250 milliseconds between each loop iteration, preventing the system from being overwhelmed.
| To stop this, introduce a condition to break the loop or turn off the microbits.

.. code-block:: python

    from microbit import *
    import radio

    # Turn on the radio
    radio.on()
    # Choose own group in pairs 0-255
    radio.config(group=8)

    while True:
        # send
        if button_a.was_pressed():
            radio.send("A")
        elif button_b.was_pressed():
            radio.send("B")
        # receive
        incoming_message = radio.receive()
        if incoming_message:
            display.show(incoming_message)
            sleep(250)
            if incoming_message == "A":
                radio.send("B")
            elif incoming_message == "B":
                radio.send("A")


.. admonition:: Tasks

    #. Add counter variables to the code to limit the number of receiver based sends to 5 for each letter.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Add counter variables to the code to limit the number of receiver based sends to 5 for each letter.

                .. code-block:: python

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
                        if incoming_message:
                            if incoming_message == "A" and counter_A < 5:
                                radio.send("A")
                                counter_A += 1
                                display.show("A" + str(counter_A))
                            elif incoming_message == "B" and counter_B < 5:
                                radio.send("B")
                                counter_B += 1
                                display.show("B" + str(counter_B))
                            sleep(250)


Back and forth messaging
---------------------------

| In summary, the code below allows two microbits to send and receive characters from the string "ABCDEFG" to each other. 
| When one microbit sends a character, the other microbit displays it and then sends the next character in the sequence. 
| If button B is pressed, it stops displaying messages and clears the radio queue.

| ``index_next = (s.index(incoming_message) + inc) % len(s)``: calculates the index of the next character to be sent.
| ``s.index(incoming_message)``: finds the index of the received message in the string `s`. For example, if `s` is "ABCDEFG" and the incoming message is "C", this would return 2 (since indexing starts from 0).
| ``+ inc``: adds the increment (`inc`) to the index. In this code, `inc` is set to 1, so this effectively gets the index of the next character in the string.
| ``% len(s)``: is the modulus operation, which finds the remainder of the division of the number by `len(s)`. This is used to ensure that the index doesn't go out of bounds. If the index reaches the end of the string, it wraps around to the start.
| ``radio.send(s[index_next])``: This line sends the character at the calculated index in the string `s` via radio. For example, if `s` is "ABCDEFG" and `index_next` is 3, this would send "D".


.. code-block:: python

    from microbit import *
    import radio

    # Turn on the radio
    radio.on()
    # Choose own group in pairs 0-255
    radio.config(group=8)

    # Define the string
    s = "ABCDEFG"
    # set the index steps
    inc = 1
    # set the delay after showing a letter
    showtime = 400

    while True:
        # send
        if button_a.was_pressed():
            radio.send(s[0])   # start at start       
        # receive
        incoming_message = radio.receive()
        if incoming_message is not None:
            if button_b.was_pressed():
                # Clear the radio queue by calling radio.receive()
                while radio.receive() is not None:
                    sleep(100)
            else:
                display.show(incoming_message)
                sleep(showtime)
                index_next = (s.index(incoming_message) + inc) % len(s)
                radio.send(s[index_next])

.. admonition:: Exercises

    #. Challenge your partner to stop the display on their microbit at a certain letter by pressing B.

.. admonition:: Tasks
    
    #. Modify the code to start at a randomly chosen letter.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to start at a randomly chosen letter.

                .. code-block:: python
                                        
                    from microbit import *
                    import radio
                    import random  # Import the random module

                    # Turn on the radio
                    radio.on()
                    # Choose own group in pairs 0-255
                    radio.config(group=8)

                    # Define the string
                    s = "ABCDEFG"
                    # Initialize the index
                    inc = 1
                    # Initialize the time to display a letter
                    showtime = 100

                    while True:
                        # send
                        if button_a.was_pressed():
                            start_letter = random.choice(s)  # Choose a random letter from s
                            radio.send(start_letter)  # Send the random letter
                        # receive
                        incoming_message = radio.receive()
                        if incoming_message is not None:
                            if button_b.was_pressed():
                                # Clear the radio queue by calling radio.receive()
                                while radio.receive() is not None:
                                    sleep(100)
                            else:
                                display.show(incoming_message)
                                sleep(showtime)
                                index_next = (s.index(incoming_message) + inc) % len(s)
                                radio.send(s[index_next])

----

Speed ups
--------------

| Below is code to speed up the resending with each new start via the A-button.

.. code-block:: python

    from microbit import *
    import radio
    import random  # Import the random module

    # Turn on the radio
    radio.on()
    # Choose own group in pairs 0-255
    radio.config(group=8)

    # Define the string
    s = "ABCDEFG"
    # Initialize the index
    inc = 1
    # set the delay after showing a letter
    showtime = 550

    while True:
        # send
        if button_a.was_pressed():
            if showtime == 100:
                # reset delay after showing a letter
                showtime = 500
            else:
                # speed up letter display
                showtime = max(100, showtime - 50)
            # Send the showtime to all microbits
            radio.send('showtime:' + str(showtime))
            start_letter = random.choice(s)  # Choose a random letter from s
            radio.send(start_letter)  # Send the random letter
        # receive
        incoming_message = radio.receive()
        if incoming_message is not None:
            if incoming_message.startswith('showtime:'):
                # Update the showtime from the received message
                showtime = int(incoming_message.split(':')[1])
            elif button_b.was_pressed():
                # Clear the radio queue by calling radio.receive()
                while radio.receive() is not None:
                    sleep(100)
            else:
                display.show(incoming_message)
                sleep(showtime)
                index_next = (s.index(incoming_message) + inc) % len(s)
                radio.send(s[index_next])


.. admonition:: Exercises

    #. Challenge your partner to stop the display on their microbit at a certain letter by pressing B.
