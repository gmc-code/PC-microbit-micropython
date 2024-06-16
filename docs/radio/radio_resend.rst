====================================================
Radio A or B
====================================================

Send on button pressing
-------------------------

| Set up the group in pairs with a value 0-255 by modifying the group in: ``radio.config(group=8)``.
| Turn on the radio using: ``radio.on()``
| Use ``button_a.was_pressed()`` to send a message, **"A"**.
| Scroll any received messages.
| ``if incoming_message is not None:`` relies on ``radio.receive()`` returning **None** when there is no message received. 


.. code-block:: python
    
    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        # send
        if button_a.was_pressed():
            radio.send("A")
        # receive
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)

----

.. admonition:: Tasks

    #. Modify the code to add sending "B" if the B button was pressed.
    #. Modify the code to send "T" or "F" from button pressing so it can be used to response True and False questions.
    #. Modify the code to send "T" or "F" from button pressing and then show the Image.YES if "T" is received, and the Image.NO if "F" is received.


    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to add sending "B" if the B button was pressed.

                    .. code-block:: python
                        
                            from microbit import *
                            import radio

                            # Choose own group in pairs 0-255
                            radio.config(group=8)
                            # Turn on the radio
                            radio.on()

                            while True:
                                # send
                                if button_a.was_pressed():
                                    radio.send("A")
                                elif button_b.was_pressed():
                                    radio.send("B")
                                # receive
                                incoming_message = radio.receive()
                                if incoming_message is not None:
                                    display.scroll(incoming_message)

                .. tab-item:: Q2

                    Modify the code to send "T" or "F" from button pressing so it can be used to response True and False questions.

                    .. code-block:: python
                        
                            from microbit import *
                            import radio

                            # Choose own group in pairs 0-255
                            radio.config(group=8)
                            # Turn on the radio
                            radio.on()

                            while True:
                                # send
                                if button_a.was_pressed():
                                    radio.send("T")
                                elif button_b.was_pressed():
                                    radio.send("F")
                                # receive
                                incoming_message = radio.receive()
                                if incoming_message is not None:
                                    display.scroll(incoming_message)

               .. tab-item:: Q3

                    Modify the code to send "T" or "F" from button pressing and then show the Image.YES if "T" is received, and the Image.NO if "F" is received.

                    .. code-block:: python

                        from microbit import *
                        import radio

                        # Turn on the radio
                        radio.on()
                        # Choose own group in pairs 0-255
                        radio.config(group=8)

                        while True:
                            if button_a.was_pressed():
                                radio.send("T")
                            elif button_b.was_pressed():
                                radio.send("F")
                            incoming_message = radio.receive()
                            if incoming_message is not None:
                                if incoming_message == "T":
                                    display.show(Image.YES)
                                elif incoming_message == "F":
                                    display.show(Image.NO)


----

Send on tilting
-----------------

| Set up the group in pairs with a value 0-255.
| Use ``button_a.was_pressed()`` to send a message, T or F, based on tilting left or right.
| Scroll any received messages.


.. code-block:: python
    
    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        # sender
        x_reading = accelerometer.get_x()
        if x_reading < -200:
            response = "T"
        elif x_reading > 200:
            response = "F"
        else:
            response = "-"
        display.show(response)
        if button_a.is_pressed():
            radio.send(response)
            sleep(100)
        # receiver
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)
            sleep(500)
            

----

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
            if incoming_message == "A":
                radio.send("B")
            elif incoming_message == "B":
                radio.send("A")


.. admonition:: Tasks

    #. Write code to send back a "B" if "A" is received and "A" if "B" is received, but not until having first displayed the received message.


    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to send back a "B" if "A" is received and "A" if "B" is received, but not until having first displayed the received message.

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
                                if incoming_message == "A":
                                    radio.send("B")
                                elif incoming_message == "B":
                                    radio.send("A")

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
            if incoming_message == "A" and counter_A < 5:
                radio.send("B")
                counter_A += 1
                display.show("A" + str(counter_A))
            elif incoming_message == "B" and counter_B < 5:
                radio.send("A")
                counter_B += 1
                display.show("B" + str(counter_B))
            sleep(250)