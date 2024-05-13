====================================================
Radio examples
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

    #. Modify the code to send "B" if the B button was pressed.
    #. Modify the code to send back a "B" if "A" is received and "A" if "B" is received, but not until having first displayed the received message.
    #. Modify the code to send "T" or "F" from button pressing so it can be used to answer True and False questions.
    #. Modify the code to send "T" or "F" from button pressing and then show the Image.YES if "T" is received, and the Image.NO if "F" is received.


    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to send "B" if the B button was pressed.

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

               .. tab-item:: Q3

                    Modify the code to send "T" or "F" from button pressing so it can be used to answer True and False questions.

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

               .. tab-item:: Q4

                    Modify the code to send "T" or "F" from button pressing so it can be used to answer True and False questions.

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
| Use ``button_a.was_pressed()`` to send a message, based on titling forward  or back.
| Use ``button_b.was_pressed()`` to send a message, based on titling left or right.
| Scroll message on sender microbit so message being sent is obvious.
| Scroll any received messages.


.. code-block:: python
    
    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        if button_a.was_pressed():
            y_reading = accelerometer.get_y()
            if y_reading > 200:
                display.scroll("B")
                radio.send("B")
            elif y_reading < -200:
                display.scroll("F")
                radio.send("F")
            else:
                display.scroll("X")
                radio.send("X")
        elif button_b.was_pressed():
            x_reading = accelerometer.get_x()
            if x_reading > 200:
                display.scroll("R")
                radio.send("R")
            elif x_reading < -200:
                display.scroll("L")
                radio.send("L")
            else:
                display.scroll("-")
                radio.send("-")

        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)

