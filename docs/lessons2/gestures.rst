====================================================
Gestures
====================================================

| The accelerometer returns the following gestures when titlting and moving the microbit: ``up``, ``down``, ``left``, ``right``, ``face up``, ``face down``, ``freefall``, ``3g``, ``6g``,
``8g``, ``shake``. 
| Gestures are always represented as strings. 
| ``3g``, ``6g`` and ``8g`` gestures occur if the microbit experiences large levels of g-force as when the microbit is moved accelerated very rapidly.
| ``face up`` occurs when the microbit is flat with the front facing upwards.
| ``face down`` occurs when the microbit is flat with the front facing downwards.
| ``up`` occurs when the top of the microbit is tilted upwards.
| ``down`` occurs when the top of the microbit is tilted downwards.
| ``left`` occurs when the left of the microbit is tilted downwards.
| ``right`` occurs when the right of the microbit is tilted downwards.

----

current_gesture
-------------------------

.. py:function:: current_gesture()

    Return the name of the current gesture as a string. The gestures are: ``"up"``, ``"down"``, ``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``, ``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``.


| The code below displays the current gesture. 
| It can be laggy, with the scrolled text lagging behind the actual tilt of the microbit.

.. code-block:: python

    from microbit import *


    while True:
        gesture = accelerometer.current_gesture()
        display.scroll(gesture)
        sleep(50)

----

is_gesture
-------------------------

.. py:function:: is_gesture(name)

    Return True or False to indicate if the named gesture is currently active.


| The code below displays an arrow indicating the direction of tilt when the top is tilted up with the bottom being tilted down.
| The arrow will continue to be displayed when the microbit is continuously tilted with the top up.

.. code-block:: python

    from microbit import *


    while True:
        if accelerometer.is_gesture("up"):
            display.show(Image.ARROW_S)
        else:
            display.clear()
        sleep(100)

----

.. admonition:: Tasks

    #. Add code to display a North arrow when the microbit gesture is ``down``.
    #. Add code to display a West arrow when the microbit gesture is ``left``.
    #. Add code to display an East arrow when the microbit gesture is ``right``.

----

is_gesture counts
-------------------------

| The code below keeps track of tilting to the right.
| Best results are seen when tilting the microbit to the right, then returning it back to a flat position.
| Each new tilt to the right tends to increase the count by about 6.
| Maintaining the tilt causes the count to increase while tilted.

.. code-block:: python

    from microbit import *


    count = 0
    display.show(count)
    while True:
        if accelerometer.is_gesture('right'):
            count += 1
            display.scroll(count, delay=60)
        sleep(20)

----

.. admonition:: Tasks

    #. Add code to reset the count back to 0 when the A button is pressed.
    #. Edit code to reset the count to a number 10 less than the current count when the B button is pressed.

----

was_gesture
-------------------------

.. py:function:: was_gesture(name)

    | Return True or False to indicate if the named gesture was active since the last check. 
    | ``was_gesture`` will not return True again for the same gesture unless another gesture has occurred.


| The code below displays an arrow indicating the direction of tilt when the top of the microbit is tilted up with the bottom being tilted down.
| The arrow will only be displayed briefly when the microbit is continuously tilted with the top up.

.. code-block:: python

    from microbit import *


    while True:
        if accelerometer.was_gesture("up"):
            display.show(Image.ARROW_S)
        else:
            display.clear()
        sleep(100)

----

.. admonition:: Tasks

    #. Add code to display a North arrow when the microbit gesture is ``down``.
    #. Add code to display a West arrow when the microbit gesture is ``left``.
    #. Add code to display an East arrow when the microbit gesture is ``right``.

----

was_gesture counts
-------------------------

| The code below starts at 10 then counts down 1 with each tilt to the right.
| Maintaining the tilt does not change the count further.

.. code-block:: python

from microbit import *


    count = 10
    display.scroll(count)
    while True:
        if accelerometer.was_gesture('right'):
            count -= 1
            display.scroll(count, delay=60)
        sleep(20)

----

.. admonition:: Tasks

    #. Edit the code to reset the count back to 10 when the count gets to 0.
    #. Edit code to reset the count to 10 when the A button is pressed.
    #. Edit code to reset the count to 10 when the A button is pressed and raise the count by 5 when the B button is pressed.

----

shake step counter
-------------------------

| The code below checks for a shake gesture and adds 1 to the count variable it the gesture is True.

.. code-block:: python

    from microbit import *


    count = 0

    while True:
        if accelerometer.was_gesture('shake'):
            count += 1
            display.show(count)


----

tilt sideways counter
-------------------------

| The code below checks for a sideways tilt and adds 1 to the count variable if the microbit has been tilted left or right.
| The two calls to the accelerometer are connected by a logical ``or`` which returns True if one of them is True.
| The backslash, ``\``, is a continuation character, that breaks up long lines for easier reading.

.. code-block:: python

    from microbit import *


    count = 0
    display.show(count)
    while True:
        if accelerometer.was_gesture('left') or \
        accelerometer.was_gesture('right'):
            count += 1
            display.scroll(count, delay=60)
        sleep(20)


----

.. admonition:: Tasks

    #. Add code to reset the count back to 0 when the A button is pressed.
    #. Edit the code to reset the count to a number 5 less than the current count when the B button is pressed.
    #. Write code to count the total number of tilts to the left or right.
    #. Write code to count the total number of tilts to the front or back.
    #. Write code to count the total number of tilts to the left or right or front or back.

----

get_gestures() counts
-------------------------

| The code below


.. code-block:: python

    from microbit import *


    while True:
        gestures = accelerometer.get_gestures()
        if len(gestures) > 0:
            for g in gestures:
                display.scroll(g, delay=60)
        sleep(20)


