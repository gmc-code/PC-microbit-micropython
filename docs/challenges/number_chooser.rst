====================================================
Number chooser
====================================================

| A number chooser can be used for a variety purposes, including, sending data, via radio, to other microbits.

----

Number chooser: simple version
-------------------------------

| The code below, sets a variable, **num**, to a starting number, 5.
| When the A-button is pressed, **num** is increased by 1. 
| To make sure **num** doesn't just keep increasing without limit, if it is reaches 9 when the A-button is pressed, it is reset to 0.

.. code-block:: python
    
    from microbit import *

    num = 5
    display.show(num)
    while True:
        if button_a.is_pressed():
            num += 1
            if num > 9:
                num = 0
            display.show(num)
        sleep(200)


----

Number chooser: by function
-------------------------------

| The code below chooses a number from 0 to 9. These limits are set in the **select_number** function.
| In the main while-loop, the function, **select_number**, is called to choose a number, **num**, which is then displayed.
| The function, **select_number**, starts the variable, **counter**, at 5.
| The while-loop keeps running until the B-button is pressed, then the variable, **counter**, is returned.
| In the while-loop, button-A pressing is used to increase the variable, **counter**, until it gets to its biggest allowed value, 9, then it restarts at 0. 

.. code-block:: python
    
    from microbit import *


    def select_number():
        counter = 5
        display.show(counter)
        while button_b.was_pressed() is False:
            if button_a.is_pressed():
                num += 1
                if counter > 9:
                    counter = 0
                display.show(counter)
            sleep(200)
        return counter


    while True:
        num = select_number()
        display.scroll(num)
        sleep(200)


----

.. admonition:: Tasks

    #. Add the parameters, **min_num** and **max_num**, to the **select_number** function so that the numbers are not limited to 0 to 9. Test with numbers 10 to 19. Modify the initial **counter** value to be the average of the **min_num** and **max_num** values. Add a short delay to **display.show** so the **counter** values are shown faster.
    #. Add a **start_num** parameter to **select_number**, so it looks like: **select_number(start_num, min_num, max_num)**.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container
 
            .. tab-set::

                .. tab-item:: Q1

                    Add the parameters, **min_num** and **max_num**, to the **select_number** function so that the numbers are not limited to 0 to 9. Test with numbers 10 to 19. Modify the initial **counter** value to be the average of the **min_num** and **max_num** values. Add a short delay to **display.show** so the **counter** values are shown faster.

                    .. code-block:: python

                        from microbit import *


                        def select_number(min_num, max_num):
                            counter = int((min_num + max_num)/2)
                            display.show(counter, delay=200)
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    counter += 1
                                    if counter > max_num:
                                        counter = min_num
                                    display.show(counter, delay=200)
                                sleep(200)
                            return counter


                        while True:
                            num = select_number(10, 19)
                            display.scroll(num)
                            sleep(200)

                .. tab-item:: Q2

                    Add a **start_num** parameter to **select_number**, so it looks like: **select_number(start_num, min_num, max_num)**

                    .. code-block:: python

                        from microbit import *


                        def select_number(start_num, min_num, max_num):
                            counter = start_num
                            display.show(counter, delay=200)
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    counter += 1
                                    if counter > max_num:
                                        counter = min_num
                                    display.show(counter, delay=200)
                                sleep(200)
                            return counter


                        num = 14
                        while True:
                            num = select_number(num, 10, 19)
                            display.scroll(num)
                            sleep(200)


