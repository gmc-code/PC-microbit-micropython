====================================================
Radio gestures
====================================================

| Gestures on the microbit refer to the way you hold or move the device. 

Gestures
--------------------------------

.. py:function::  accelerometer.current_gesture()

    Returns one of the following gesture names as a string: "up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake".
    This gives you the most recent gesture that was detected, which can be useful if you want your program to react differently depending on the gesture made. 
    However, it might miss gestures if your program is busy doing other things when the gesture occurs.


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
    This is useful in scenarios where you don't want to miss any gestures, even when your program is busy doing other things.


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
| The code loops through the items in the dictionary assigning each key:value pair to the variables gesture and char.
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

Send on gesture
--------------------------------

| Set up the group in pairs with a value 0-255.
| Use ``shake()`` to send a "duck" string.
| The code below displays a duck image on receiving any message.


.. code-block:: python
    
    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        # sender
        gesture = accelerometer.current_gesture()
        if gesture == 'shake':
            display.clear()
            radio.send("duck")
        # receiver
        incoming_message = radio.receive()
        if incoming_message:
            display.show(Image.DUCK)
          
----

.. admonition:: Tasks
    
    #. Modify the code so the duck is only shown if the incoming_message is "duck".
    #. Modify the code to send a cow and butterfly on left and right gestures.
    #. Modify the receiver code so different notes are also played (non-blocking) for each different incoming_message.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code so the duck is only shown if the incoming_message is "duck".

                .. code-block:: python
                    
                    from microbit import *
                    import radio

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    while True:
                        # sender
                        gesture = accelerometer.current_gesture()
                        if gesture == 'shake':
                            display.clear()
                            radio.send("duck")

                        # receiver
                        incoming_message = radio.receive()
                        if incoming_message:
                            if incoming_message == "duck":
                                display.show(Image.DUCK)
                  

            .. tab-item:: Q2

                Modify the code to send a cow and butterfly on left and right gestures.

                .. code-block:: python
                    
                    from microbit import *
                    import radio

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    while True:
                        # sender
                        gesture = accelerometer.current_gesture()
                        if gesture == 'shake':
                            display.clear()
                            radio.send("duck")
                        elif gesture == 'left':
                            display.clear()
                            radio.send("cow")
                        elif gesture == 'right':
                            display.clear()
                            radio.send("butterfly")
                        
                        # receiver
                        incoming_message = radio.receive()
                        if incoming_message:
                            if incoming_message == "duck":
                                display.show(Image.DUCK)
                            elif incoming_message == "cow":
                                display.show(Image.COW)
                            elif incoming_message == "butterfly":
                                display.show(Image.BUTTERFLY)
                            
            .. tab-item:: Q3

                Modify the receiver code so different notes are also played (non-blocking) for each different incoming_message.

                .. code-block:: python
                                        
                    from microbit import *
                    import radio
                    import music

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    while True:
                        # sender
                        gesture = accelerometer.current_gesture()
                        if gesture == 'shake':
                            display.clear()
                            radio.send("duck")
                        elif gesture == 'left':
                            display.clear()
                            radio.send("cow")
                        elif gesture == 'right':
                            display.clear()
                            radio.send("butterfly")
                    
                        # receiver
                        incoming_message = radio.receive()
                        if incoming_message:
                            if incoming_message == "duck":
                                display.show(Image.DUCK)
                                music.play("d", wait=False)
                            elif incoming_message == "cow":
                                display.show(Image.COW)
                                music.play("c", wait=False)
                            elif incoming_message == "butterfly":
                                display.show(Image.BUTTERFLY)
                                music.play("b", wait=False)

                        sleep(100)


----

Happy group
---------------------

| Set all players with the same group number.
| Set ``players`` to the number of players.
| Set the ``player_id`` for each player from 1 to the number of players.

| In the code below, player 1 starts by shaking their microbit.
| The image is cleared and then is sent to another random player.


.. code-block:: python
        
    from microbit import *
    import radio
    import random

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    # set for number of players in game
    players = 2
    # change for each player
    player_id = 1

    # show player ids at the start
    display.show(player_id)
    if player_id == 1:
        has_img = True
    else:
        has_img = False


    while True:
        if accelerometer.was_gesture('shake'):
            # only the player with the img can send it to another
            if has_img:
                player_to_send_to = random.randint(1, players)
                if player_to_send_to != player_id:
                    display.clear()
                    radio.send(str(player_to_send_to))
        incoming_message = radio.receive()
        if incoming_message:
            if incoming_message == str(player_id):
                has_img = True
                display.show(Image.HAPPY)
            else:
                has_img = False


.. admonition:: Challenges
    
    #. Modify the code so that the image is not cleared and incoming messages don't set the has_img to False. Now all players with the happy image can keep shaking it to pass it on to another player. How quickly can the group get everyone with a happy face?

