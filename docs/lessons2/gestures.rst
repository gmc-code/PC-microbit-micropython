====================================================
Gestures
====================================================

| The accelerometer returns the following gestures when titlting and moving the microbit: ``up``, ``down``, ``left``, ``right``, ``face up``, ``face down``, ``freefall``, ``3g``, ``6g``,
``8g``, ``shake``. 
| Gestures are always represented as strings. 
| ``3g``, ``6g`` and ``8g`` gestures occur if the microbit experiences large levels of g-force as when the microbit is moved accelerated very rapidly.
| ``face up`` occurs when the microbit is flat with the front facing upwards.
| ``up`` occurs when the top of the microbit is tilted upwards.
| ``down`` occurs when the top of the microbit is tilted downwards.
| ``left`` occurs when the left of the microbit is tilted downwards.
| ``right`` occurs when the right of the microbit is tilted downwards.

Current gesture
-------------------------

.. py:function:: current_gesture()

    Return the name of the current gesture as a string. The gestures are: ``"up"``, ``"down"``, ``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``, ``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``.


| The code below displays the current gesture. It can be slow to change and may require small movement of the microbit to register properly.

.. code-block:: python

    from microbit import *


    while True:
        gesture = accelerometer.current_gesture()
        display.scroll(gesture)
        sleep(50)


----

.. py:function:: is_gesture(name)

    Return True or False to indicate if the named gesture is currently active.


| The code below displays a happy image if the microbit is face up, or an angry image if it is not.

.. code-block:: python

    from microbit import *


    while True:
        if accelerometer.is_gesture("up"):
            display.show(Image.ARROW_S)
        elif accelerometer.is_gesture("right"):
            display.show(Image.ARROW_E)
        elif accelerometer.is_gesture("down"):
            display.show(Image.ARROW_N)
        elif accelerometer.is_gesture("left"):
            display.show(Image.ARROW_W)
        else:
            display.clear()
        sleep(20)


----

        from microbit import *


        steps=0

        while True:
            if accelerometer.was_gesture('shake'):
                steps += 1
                display.show(steps)


----

.. admonition:: Tasks

    #. Write code to display different arrow images when the microbit is tilted in each direction.


