====================================================
Letter chooser
====================================================

| The letter choose follows a similar coding structure as the number chooser.
| The main difference is that the letters are chosen from a list, so list indexing is needed.

----

Letter chooser: simple version
-------------------------------

| The code below, sets a variable, **char_index**, to a starting number, 2.
| It then displays the character with index 2 in the list, **chars**.
| When the A-button is pressed, **char_index** is increased by 1. 
| To make sure **char_index** doesn't just keep increasing without limit, if it has reached 4 when the A-button is pressed, it is reset to 0.

.. code-block:: python
    
    from microbit import *

    chars = ["A", "B", "C", "D", "E"]

    char_index = 2
    display.show(chars[char_index])
    while True:
        if button_a.is_pressed():
            char_index += 1
            if char_index > 4:
                char_index = 0
            display.show(chars[char_index])
        sleep(200)


----

Letter chooser: by function
-------------------------------

| The code below chooses a letter from a list of letters.
| In the main while-loop, **select_char** is called to choose a letter, **letter**, which is then displayed.
| The function, **select_char(** starts the variable, **char_index**, at the middle index position of the **chars** list. The **middle_index** is previously calculated by halving the length of the **chars** list. **middle_index = int(max_char_index / 2)**
| The while-loop keeps running until the B-button is pressed, then **chars[char_index]** is returned.
| In the while-loop, button-A pressing is used to increase the variable, **char_index**, until it gets to its biggest allowed value, **max_char_index**, then it restarts at 0. 

.. code-block:: python
    
    from microbit import *

    chars = ["A", "B", "C", "D", "E"]
    max_char_index = len(chars) - 1
    middle_index = int(max_char_index / 2)


    def select_char():
        char_index = middle_index
        display.show(chars[char_index])
        while button_b.was_pressed() is False:
            if button_a.is_pressed():
                char_index += 1
                if char_index > max_char_index:
                    char_index = 0
                display.show(chars[char_index])
            sleep(200)
        return chars[char_index]


    while True:
        letter = select_char()
        display.scroll(letter)
        sleep(200)


----

.. admonition:: Tasks

    #. Add the parameter **start_char** parameter to **select_char**, so it looks like: **select_char(start_char)**. Use the index method to get the corresponding index for the letter.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container
 
            .. tab-set::

                .. tab-item:: Q1

                    Add the parameter **start_char** parameter to **select_char**, so it looks like: **select_char(start_char)**. Use the index method to get the corresponding index for the letter.

                    .. code-block:: python

                        from microbit import *

                        chars = ["A", "B", "C", "D", "E"]
                        max_char_index = len(chars) - 1


                        def select_char(start_char): 
                            index = chars.index(start_char)
                            display.show(chars[index])
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    index += 1
                                    if index > max_char_index:
                                        index = 0
                                    display.show(chars[index])
                                sleep(200)
                            return chars[index]


                        letter = "A"
                        while True:
                            letter = select_char(letter)
                            display.scroll(letter)
                            sleep(200)



                