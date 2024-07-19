====================================================
EXT: Buttons and selection
====================================================

String slices
-----------------

.. py:function:: string[start_value:stop_value]

    | returns character at index (position) start_value to the character at the index before the stop_value character.
    | "Hello"[0:3] returns characters 1 to 2, "Hel", with "H: being index 0.

----

Converting a Boolean to a string to take a slice
---------------------------------------------------

| The Booleans True and False are not strings.
| The code below, ``str(button_a.is_pressed())``, coverts the boolean values of True or False to a string. True becomes "True" and False becomes "False".
| Then ``[0:1]`` takes a string slice giving the first letter only.
| So True becomes "T" and False becomes "F".

.. code-block:: python

    from microbit import *

    while True:
        display.show(str(button_a.is_pressed())[0:1])
        sleep(1000)

----

Changing values with A and B-buttons
----------------------------------------

| Use the A-button to increase a variable.
| Use the B-button to decrease a variable.
| In the code below, the ``delay_time`` variable is increased in steps of 10 by the A-button admonition decreased in steps of 10 by the B-button. 
| Finally, text is scrolled with a delay of ``delay_time``.

.. code-block:: python

    from microbit import *

    delay_time = 80

    while True:
        if button_a.is_pressed():
            delay_time += 10
        elif button_b.is_pressed():
            delay_time -= 10
        else:
            sleep(100)
        display.scroll("ABC", delay=delay_time)    

| The code above fails when the delay_time goes below 0.
| The variable, ``delay_time``, can be restricted to a set range of values using the min and max functions.
| ``delay_time = min(400, delay_time + 10)`` prevents the ``delay_time`` from going above 400.
| ``delay_time = max(50, delay_time - 10)`` prevents the ``delay_time`` from going below 50.

.. code-block:: python

    from microbit import *

    delay_time = 80

    while True:
        if button_a.is_pressed():
            delay_time = min(400, delay_time + 10)
        elif button_b.is_pressed():
            delay_time = max(50, delay_time - 10)
        else:
            sleep(100)
        display.scroll("ABC", delay=delay_time)  

----

.. admonition:: Tasks

    #. Edit the code to adjust the scroll delay in steps of 25.
    #. Write code to alter a ``guess_number`` variable in steps of 1 by the buttons. Use both buttons to set the number and show it. Start the number at 5 and limit it to a minimum of 1 and a maximum of 9.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Edit the code to adjust the scroll delay in steps of 25.

                .. code-block:: python

                    from microbit import *

                    delay_time = 80

                    while True:
                        if button_a.is_pressed():
                            delay_time += 25
                        elif button_b.is_pressed():
                            delay_time -= 25
                        else:
                            sleep(100)
                        display.scroll("ABC", delay=delay_time) 


            .. tab-item:: Q2

                Write code to alter a ``guess_number`` variable in steps of 1 by the buttons. Use both buttons to set the number and scroll it. Start the number at 5 and limit it to a minimum of 1 and a maximum of 9.

                .. code-block:: python

                    from microbit import *

                    guess_number = 5
                    while True:
                        if button_a.is_pressed() and button_b.is_pressed():
                            display.show(guess_number, delay=80)
                            # now start again
                            guess_number = 5
                        if button_a.is_pressed():
                            guess_number = min(9, guess_number + 1)
                        elif button_b.is_pressed():
                            guess_number = max(1, guess_number - 1)
                        else:
                            sleep(100)
                        display.show(guess_number, delay=80)
                        sleep(200)
