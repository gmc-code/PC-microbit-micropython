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

    #. Modify the code to display a North arrow when the microbit gesture is ``down``.
    #. Modify the code to display a West arrow when the microbit gesture is ``left``.
    #. Modify the code to display an East arrow when the microbit gesture is ``right``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to display a North arrow when the microbit gesture is ``down``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("down"):
                            display.show(Image.ARROW_N)
                        else:
                            display.clear()
                        sleep(100)

            .. tab-item:: Q2

                Modify the code to display a West arrow when the microbit gesture is ``left``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("left"):
                            display.show(Image.ARROW_W)
                        else:
                            display.clear()
                        sleep(100)

            .. tab-item:: Q3

                Modify the code to display an East arrow when the microbit gesture is ``right``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("right"):
                            display.show(Image.ARROW_E)
                        else:
                            display.clear()
                        sleep(100)

----

is_gesture counts
-------------------------

| The code below keeps track of tilting to the right.
| Best results are seen when tilting the microbit to the right, then returning it back to a flat position.
| Each new tilt to the right tends to increase the count.
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

    #. Modify the code to reset the count back to 0 when the A button is pressed.
    #. Modify the code to reset the count to a number 10 less than the current count when the B button is pressed.
    #. Modify the code to reset the count to a number 10 less than the current count, but not lower than 0, when the B button is pressed.
    #. Modify the code to include both the A button and B button actions.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to reset the count back to 0 when the A button is pressed.

                .. code-block:: python

                    from microbit import *

                    count = 0
                    display.show(count)
                    while True:
                        if button_a.is_pressed():
                            count = 0
                            display.scroll(count, delay=60)
                            sleep(200)
                       if accelerometer.is_gesture('right'):
                            count += 1
                            display.scroll(count, delay=60)
                        sleep(20)

            .. tab-item:: Q2

                Modify the code to reset the count to a number 10 less than the current count when the B button is pressed.

                .. code-block:: python

                    from microbit import *

                    count = 0
                    display.show(count)
                    while True:
                        if button_b.is_pressed():
                            count = count - 10
                            display.scroll(count, delay=60)
                            sleep(200)
                        if accelerometer.is_gesture('right'):
                            count += 1
                            display.scroll(count, delay=60)
                        sleep(20)

            .. tab-item:: Q3

                Modify the code to reset the count to a number 10 less than the current count, but not lower than 0, when the B button is pressed.

                .. code-block:: python

                    from microbit import *

                    count = 0
                    display.show(count)
                    while True:
                        if button_b.is_pressed():
                            count = max(0, count - 10)
                            display.scroll(count, delay=60)
                            sleep(200)
                        if accelerometer.is_gesture('right'):
                            count += 1
                            display.scroll(count, delay=60)
                        sleep(20)

            .. tab-item:: Q4

                Modify the code to include both the A button and B button actions.

                .. code-block:: python

                    from microbit import *

                    count = 0
                    display.show(count)
                    while True:
                        if button_a.is_pressed():
                            count = 0
                            display.scroll(count, delay=60)
                            sleep(200)
                        elif button_b.is_pressed():
                            count = max(0, count - 10)
                            display.scroll(count, delay=60)
                            sleep(200)
                        if accelerometer.is_gesture('right'):
                            count += 1
                            display.scroll(count, delay=60)
                        sleep(20)

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

    #. Modify the code to display a North arrow when the microbit gesture was ``down``.
    #. Modify the code to display a West arrow when the microbit gesture was ``left``.
    #. Modify the code to display an East arrow when the microbit gesture was ``right``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to display a North arrow when the microbit gesture was ``down``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.was_gesture("down"):
                            display.show(Image.ARROW_N)
                        else:
                            display.clear()
                        sleep(100)

            .. tab-item:: Q2

                Modify the code to display a West arrow when the microbit gesture was ``left``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.was_gesture("left"):
                            display.show(Image.ARROW_W)
                        else:
                            display.clear()
                        sleep(100)

            .. tab-item:: Q3

                Modify the code to display an East arrow when the microbit gesture was ``right``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("right"):
                            display.show(Image.ARROW_E)
                        else:
                            display.clear()
                        sleep(100)

----

was_gesture counts
-------------------------

| The code below starts at 5 then counts down 1 with each tilt to the right.
| Maintaining the tilt does not change the count further.

.. code-block:: python

    from microbit import *

    count = 5
    display.scroll(count)
    while True:
        if accelerometer.was_gesture('right'):
            count -= 1
            display.scroll(count, delay=60)
        sleep(20)

----

.. admonition:: Tasks

    #. Modify the code to reset the count back to 5 when the count gets to 0.
    #. Keeping the modifications, modify the code further to reset the count to 5 when the A button is pressed.
    #. Keeping the modifications, modify the code further to raise the count by 2 when the B button is pressed.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to reset the count back to 5 when the count gets to 0.

                .. code-block:: python

                    from microbit import *

                    count = 5
                    display.scroll(count)
                    while True:
                        if accelerometer.was_gesture('right'):
                            count -= 1
                            display.scroll(count, delay=60)
                        sleep(20)
                        if count == 0:
                            count = 5
                            display.scroll(count, delay=60)
                            sleep(200)                        

            .. tab-item:: Q2

                Keeping the modifications, modify the code further to reset the count to 5 when the A button is pressed.

                .. code-block:: python

                    from microbit import *

                    count = 5
                    display.scroll(count)
                    while True:
                        if button_a.is_pressed():
                            count = 5
                            display.scroll(count, delay=60)
                            sleep(200)
                        if accelerometer.was_gesture('right'):
                            count -= 1
                            display.scroll(count, delay=60)
                        sleep(20)
                        if count == 0:
                            count = 5
                            display.scroll(count, delay=60)
                            sleep(200)


            .. tab-item:: Q3

                Keeping the modifications, modify the code further to raise the count by 2 when the B button is pressed.

                .. code-block:: python

                    from microbit import *

                    count = 5
                    display.scroll(count)
                    while True:
                        if button_a.is_pressed():
                            count = 5
                            display.scroll(count, delay=60)
                            sleep(200)
                        elif button_b.is_pressed():
                            count = count + 2
                            display.scroll(count, delay=60)
                            sleep(200)
                        if accelerometer.was_gesture('right'):
                            count -= 1
                            display.scroll(count, delay=60)
                        sleep(20)
                        if count == 0:
                            count = 5
                            display.scroll(count, delay=60)
                            sleep(20)

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
    #. Modify the code to count the total number of tilts to the left or right.
    #. Modify the code to count the total number of tilts to the front or back.
    #. Modify the code to count the total number of tilts to the left or right or front or back.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to display a North arrow when the microbit gesture is ``down``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("down"):
                            display.show(Image.ARROW_N)
                        else:
                            display.clear()
                        sleep(100)

            .. tab-item:: Q2

                Modify the code to display a West arrow when the microbit gesture is ``left``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("left"):
                            display.show(Image.ARROW_W)
                        else:
                            display.clear()
                        sleep(100)

----

get_gestures()
-------------------------

.. py:function:: get_gestures()

    | Return a tuple of the gesture history. The most recent is listed last.
    | Also clears the gesture history before returning.


| The code below will typically get 4 to 8 gestures with a 2 sec sleep.
| The gestures tuple can be displayed by using a for loop to each item in the tuple for display.

.. code-block:: python

    from microbit import *

    display.show('-')
    while True:
        gestures = accelerometer.get_gestures()
        if len(gestures) > 0:
            display.show(len(gestures))
            sleep(1000)
            for g in gestures:
                display.scroll(g, delay=60)
            display.scroll('-')
        sleep(2000)

----

.. admonition:: Tasks

    #. Try adjusting the sleep from 2 up to 10 seconds and spinning the microbit on its edge to give the gestures in order: right, down, left, up.
    #. Try adjusting the sleep from 2 up to 10 seconds and spinning the microbit to give the gestures in order: face up, left, face down, right.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to display a North arrow when the microbit gesture is ``down``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("down"):
                            display.show(Image.ARROW_N)
                        else:
                            display.clear()
                        sleep(100)

            .. tab-item:: Q2

                Modify the code to display a West arrow when the microbit gesture is ``left``.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if accelerometer.is_gesture("left"):
                            display.show(Image.ARROW_W)
                        else:
                            display.clear()
                        sleep(100)
