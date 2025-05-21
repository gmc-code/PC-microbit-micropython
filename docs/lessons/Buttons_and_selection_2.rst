====================================================
EXT: Buttons and selection
====================================================

if - else with break
----------------------------------------

| ``break`` is used to stop the while true loop.


| The code below counts up in steps of 1 from 1 to a target number, display the number till the target number is reached after which program breaks out of the loop and displays the message "target reached".

.. code-block:: python

    from microbit import *

    num = 1
    target = 5
    while True:
        display.scroll(num)
        if num == target:
            break
        else:
            num = num + 1
        sleep(200)
    display.scroll("target reached", delay=50)

| The code below counts up in steps of 1 from 1 up to but not including the target number, displaying the number till the target number is reached after which program breaks out of the loop and displays the message "target reached".
| Notice that the condition uses "less than" rather than "equal".

.. code-block:: python

    from microbit import *

    num = 1
    target = 5
    while True:
        if num < target:
            display.scroll(num, delay=50)
            num = num + 1
        else:
            break
        sleep(200)
    display.scroll("target reached", delay=50)

----

break on button pressing
----------------------------------------

| The code below counts up in steps of 1 from 1 till the A button is pressed, after which program breaks out of the loop and displays the message "A pressed".

.. code-block:: python

    from microbit import *

    num = 1
    while True:
        display.scroll(num)
        if button_a.is_pressed():
            break
        else:
            num = num + 1
        sleep(200)
    display.scroll("A pressed", delay=50)

----

String slices
-----------------

.. py:attribute:: string[start_value:stop_value]

    | returns character at index (position) start_value to the character at the index before the stop_value character.
    | "Hello"[0:3] returns characters 0 to 2, "Hel", with "H" being index 0.

----

Converting a Boolean to a string initial
---------------------------------------------------

| The Booleans True and False are not strings.
| The code below, ``str(button_a.is_pressed())``, coverts the boolean values of True or False to a string. True becomes "True" and False becomes "False".
| Then ``[0:1]`` takes a string slice giving the first letter only.
| So True becomes "T" and False becomes "F".

.. code-block:: python

    from microbit import *

    while True:
        true_or_false = str(button_a.is_pressed())
        t_or_f = true_or_false[0:1]
        display.show(t_or_f)
        sleep(500)

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

    #. Edit the code to adjust the scroll delay in steps of 20.
    #. Write code to alter a ``guess_number`` variable in steps of 1 by the buttons. Use both buttons to set the number and show it. Start the number at 5 and limit it to a minimum of 1 and a maximum of 9.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Edit the code to adjust the scroll delay in steps of 20.

                .. code-block:: python

                    from microbit import *

                    delay_time = 80
                    delay_time_step = 20

                    while True:
                        if button_a.is_pressed():
                            delay_time = min(400, delay_time + delay_time_step)
                        elif button_b.is_pressed():
                            delay_time = max(50, delay_time - delay_time_step)
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


