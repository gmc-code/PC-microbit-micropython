====================================================
Letter chooser
====================================================

| The letter choose foolows a similar code=ing structure as the number chooser.

----

Letter chooser simple version
-------------------------------

| The code below chooses a letter from a list of letters.
| In the main while loop, **select_char()** is called to choose a letter, **letter**, which is then displayed.
| The function, **select_char()**, starts the variable, **index_num**, at the middle index position of the **chars** list. The **middle_index** is previously calculated by halving the length of the **chars** list.
| The while loop keeps running until the B button is pressed, then **chars[index_num]** is returned.
| In the while loop, A button pressing is used to increase the variable, **index_num**, until it gets to its biggest allowed value, **max_char_index**, then it restarts at 0. 

.. code-block:: python
    
    from microbit import *

    chars = ["A", "B", "C", "D", "E"]
    max_char_index = len(chars)
    middle_index = int(max_char_index / 2)


    def select_char():
        index_num = middle_index
        display.show(chars[index_num])
        while button_b.was_pressed() is False:
            if button_a.is_pressed():
                index_num += 1
                if index_num == max_char_index:
                    index_num = 0
                display.show(chars[index_num])
            sleep(200)
        return chars[index_num]


    while True:
        letter = select_char()
        display.scroll(letter)
        sleep(200)


----

.. admonition:: Tasks

    #. Add the parameter **start_num** parameter to **select_char**, so it looks like: **select_char(start_num)**

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container
 
            .. tab-set::

                .. tab-item:: Q1

                    Add the parameters, **min_num** and **max_num**, to the **select_char** function so that the numbers are not limited to 0 to 9. Test with numbers 10 to 19. Modify the initial **counter** value to be the average of the **min_num** and **max_num** values. Add a short delay to **display.show** so the **counter** values are shown faster.

                    .. code-block:: python

                        from microbit import *


                        def select_char(min_num, max_num):
                            counter = int((min_num + max_num)/2)
                            display.show(counter, delay=200)
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    counter += 1
                                    if counter == max_num:
                                        counter = min_num
                                    display.show(counter, delay=200)
                                sleep(200)
                            return counter


                        while True:
                            num = select_char(10, 19)
                            display.scroll(num)
                            sleep(200)

                