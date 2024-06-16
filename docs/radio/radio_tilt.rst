====================================================
Radio tilt
====================================================

Choose response by tilting
--------------------------------

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
        if button_a.was_pressed():
            radio.send(response)
        # receiver
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)
            sleep(500)
            

----

.. admonition:: Tasks
    
    #. Modify the code to send "Y" or "N" from tilting and button pressing so it can be used to response Yes or No questions.
    #. Modify the code to send "Y" or "N" from tilting and button pressing and then show the Image.YES if "Y" is received, and the Image.NO if "N" is received.


    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to send "Y" or "N" from tilting and button pressing so it can be used to response Yes or No questions.

                    .. code-block:: python
                        
                        from microbit import *
                        import radio

                        # Choose own group in pairs 0-255
                        radio.config(group=8)
                        # Turn on the radio
                        radio.on()

                        while True:
                            # send
                            x_reading = accelerometer.get_x()
                            if x_reading < -200:
                                response = "Y"
                            elif x_reading > 200:
                                response = "N"
                            else:
                                response = "-"
                            display.show(response)
                            if button_a.was_pressed():
                                radio.send(response)
                                sleep(100)
                            # receive
                            incoming_message = radio.receive()
                            if incoming_message is not None:
                                display.scroll(incoming_message)
                                sleep(500)



                .. tab-item:: Q2

                    Modify the code to send "Y" or "N" from tilting and button pressing and then show the Image.YES if "Y" is received, and the Image.NO if "N" is received.

                    .. code-block:: python
                        
                        from microbit import *
                        import radio

                        # Choose own group in pairs 0-255
                        radio.config(group=8)
                        # Turn on the radio
                        radio.on()

                        while True:
                            # send
                            x_reading = accelerometer.get_x()
                            if x_reading < -200:
                                response = "Y"
                            elif x_reading > 200:
                                response = "N"
                            else:
                                response = "-"
                            display.show(response)
                            if button_a.was_pressed():
                                radio.send(response)
                                sleep(100)
                            # receive
                            incoming_message = radio.receive()
                            if incoming_message is not None:
                                if incoming_message == "Y":
                                    display.show(Image.YES)
                                elif incoming_message == "N":
                                    display.show(Image.NO)

