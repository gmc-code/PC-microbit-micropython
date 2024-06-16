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
    #. Modify the code to send "T" or "F" from button pressing so it can be used to response True or False questions.
    #. Modify the code to send "Y" or "N" from button pressing so it can be used to response Yes or No questions.
    #. Modify the code to send "Y" or "N" from button pressing and then show the Image.YES if "Y" is received, and the Image.NO if "N" is received.


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

                Modify the code to send "Y" or "N" from button pressing so it can be used to response Yes or No questions.

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
                            radio.send("Y")
                        elif button_b.was_pressed():
                            radio.send("N")
                        # receive
                        incoming_message = radio.receive()
                        if incoming_message is not None:
                            display.scroll(incoming_message)

            .. tab-item:: Q4

                Modify the code to send "Y" or "N" from button pressing and then show the Image.YES if "Y" is received, and the Image.NO if "N" is received.

                .. code-block:: python

                    from microbit import *
                    import radio

                    # Turn on the radio
                    radio.on()
                    # Choose own group in pairs 0-255
                    radio.config(group=8)

                    while True:
                        if button_a.was_pressed():
                            radio.send("Y")
                        elif button_b.was_pressed():
                            radio.send("N")
                        incoming_message = radio.receive()
                        if incoming_message is not None:
                            if incoming_message == "Y":
                                display.show(Image.YES)
                            elif incoming_message == "N":
                                display.show(Image.NO)

