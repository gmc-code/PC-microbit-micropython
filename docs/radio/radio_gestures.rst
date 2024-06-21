====================================================
Radio gestures
====================================================

Gestures
--------------------------------

.. py:function::  accelerometer.current_gesture()

    Returns one of the following gesture names as a string: "up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake".

| Use the code below to test gestures. 
| Shake with a quick flick sideways. 
| Tilt it vertically with each edge downwards and observe the gesture.

.. code-block:: python
    
    from microbit import *


    while True:
        gesture = accelerometer.current_gesture()
        display.scroll(gesture, delay=80)
        sleep(200)


.. py:function::  accelerometer.was_gesture(gesture)

    Returns True if the gesture occurred since the last call, otherwise False.

| Use the code below to test for the 'right' gesture by tilting it vertically on its right edge.

.. code-block:: python
    
    from microbit import *


    while True:
        was_right = accelerometer.was_gesture('right')
        if was_right:
            display.scroll('R', delay=80)
        sleep(200)



.. admonition:: Tasks
    
    #. Modify the code to scroll "L" for a 'left' gesture.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to scroll "L" for a 'left' gesture.

                .. code-block:: python
                    
                    from microbit import *


                    while True:
                        was_left = accelerometer.was_gesture('left')
                        if was_left:
                            display.scroll('L', delay=80)
                        sleep(200)


----

Send on shake
--------------------------------

| Set up the group in pairs with a value 0-255.
| Use ``shake()`` to send a message.


.. code-block:: python
    
    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        # sender
        if accelerometer.was_gesture('shake'):
            display.clear()
            radio.send("duck")
        # receiver
        incoming_message = radio.receive()
        if incoming_message:
            display.show(Image.DUCK)

                

----





.. admonition:: Tasks
    
    #. Modify the code to send a giraffe and butterfly on left and right gestures.
    #. 

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to send a giraffe and butterfly on left and right gestures.

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
                        if incoming_message:
                            display.scroll(incoming_message)
                            sleep(1000)



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
                            if incoming_message:
                                if incoming_message == "Y":
                                    display.show(Image.YES)
                                elif incoming_message == "N":
                                    display.show(Image.NO)
                                sleep(1000)

