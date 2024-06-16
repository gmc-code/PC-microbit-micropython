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
        if button_a.was_pressed():
            radio.send("A")
        elif button_b.was_pressed():
            radio.send("B")
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)
            sleep(250)
            if incoming_message == "A":
                radio.send("B")
            elif incoming_message == "B":
                radio.send("A")


.. admonition:: Tasks

    #. Modify the code to limit the number of receiver based sends to 5 for each letter.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to limit the number of receiver based sends to 5 for each letter.

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
                        if button_a.was_pressed():
                            radio.send("A")
                        elif button_b.was_pressed():
                            radio.send("B")
                        incoming_message = radio.receive()
                        if incoming_message is not None:
                            display.scroll(incoming_message)
                            sleep(250)
                            if incoming_message == "A" and counter_A < 5:
                                radio.send("B")
                                counter_A += 1
                                display.show("A" + str(counter_A))
                            elif incoming_message == "B" and counter_B < 5:
                                radio.send("A")
                                counter_B += 1
                                display.show("B" + str(counter_B))
                            sleep(250)

