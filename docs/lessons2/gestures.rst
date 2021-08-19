====================================================
Gestures
====================================================

| The accelerometer returns the following gestures moving the microbit: ``up``, ``down``, ``left``, ``right``, ``face up``, ``face down``, ``freefall``, ``3g``, ``6g``,
``8g``, ``shake``. 
| Gestures are always represented as strings. 
| ``3g``, ``6g`` and ``8g`` gestures apply when the microbit experiences large levels of g-force.

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

    #. Write code to display different arrow images when the microbit is tilted in each direction.


