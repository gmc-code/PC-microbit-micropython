====================================================
Gestures
====================================================

| The accelerometer returns the following gestures moving the microbit: ``up``, ``down``, ``left``, ``right``, ``face up``, ``face down``, ``freefall``, ``3g``, ``6g``,
``8g``, ``shake``. 
| Gestures are always represented as strings. 
| ``3g``, ``6g`` and ``8g`` gestures apply when the micorbit experiences large levels of g-force.

Current gesture
-------------------------

.. py:function:: current_gesture()

    Return the name of the current gesture as a string. The gestures are: ``"up"``, ``"down"``, ``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``, ``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``.


| The code below displays teh current gesture.

.. code-block:: python

    from microbit import *


    while True:
        gesture = accelerometer.current_gesture()
        display.scroll(gesture)
        sleep(500)


| The code below displays a happy image if the microbit is face up, or an angry image if it is not.

.. code-block:: python

    from microbit import *


    while True:
        gesture = accelerometer.current_gesture()
        if gesture == "face up":
            display.show(Image.HAPPY)
        else:
            display.show(Image.ANGRY)

----

.. admonition:: Tasks

    #. What are the readings for 1 o'clock?

----


-------------


    from microbit import *
    import random

    while True:
        display.show("8")
        if accelerometer.was_gesture("right"):
            display.clear()
            sleep(1000)

