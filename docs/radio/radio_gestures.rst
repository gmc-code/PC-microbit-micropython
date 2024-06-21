====================================================
Radio gestures
====================================================

| Gestures on the microbit refer to the way you hold or move the device. 

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
    #. Modify the code to scroll "U" for an 'up' gesture.
    #. Modify the code to scroll "D" for a 'down' gesture.

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

            .. tab-item:: Q2

                Modify the code to scroll "U" for an 'up' gesture.

                .. code-block:: python
                    
                    from microbit import *


                    while True:
                        was_up = accelerometer.was_gesture('up')
                        if was_up:
                            display.scroll('U', delay=80)
                        sleep(200)

            .. tab-item:: Q3

                Modify the code to scroll "D" for a 'down' gesture.

                .. code-block:: python
                    
                    from microbit import *


                    while True:
                        was_down = accelerometer.was_gesture('down')
                        if was_down:
                            display.scroll('D', delay=80)
                        sleep(200)


Advanced gesture usage
-----------------------------

| The code below uses a dictionary of key:value pairs to store the response for each gesture.
| THe code loops through the items in the dictionary assigning each key: value pair to the variables gesture and char.
| If the gesture has occurred, the corresponding character is scrolled. 

.. code-block:: python
                    
    from microbit import *

    # Define a dictionary to map gestures to display characters
    gesture_map = {
        'right': 'R',
        'left': 'L',
        'up': 'U',
        'down': 'D'
    }

    while True:
        for gesture, char in gesture_map.items():
            if accelerometer.was_gesture(gesture):
                display.scroll(char, delay=80)

.. admonition:: Challenges
    
    #. Modify the code so that arrows pointing to the ground are shown instead of letters scrolled.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code so that arrows pointing to the ground are shown instead of letters scrolled.

                .. code-block:: python
                    
                    from microbit import *

                    # Define a dictionary to map gestures to arrows
                    gesture_map = {
                        'right': Image.ARROW_E,
                        'left': Image.ARROW_W,
                        'up': Image.ARROW_S,
                        'down': Image.ARROW_N,
                    }

                    while True:
                        for gesture, img in gesture_map.items():
                            if accelerometer.was_gesture(gesture):
                                display.show(img)


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

