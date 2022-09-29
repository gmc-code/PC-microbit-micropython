====================================================
Number chooser
====================================================


| Use the A button to cycle through the digits from 0 to 9, and continue again from 0.
| Use the B button to select the number.

----

.. code-block:: python

    from microbit import *


    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    max_char_index = len(chars)
    middle_index = int(max_char_index / 2)


    def select_number():
        counter = middle_index
        display.show(chars[counter])
        while button_b.was_pressed() is False:
            if button_a.is_pressed():
                counter += 1
                if counter == max_char_index:
                    counter = 0
                display.show(chars[counter])
            sleep(200)
        return counter


    while True:
        num = select_number()
        display.scroll(chars[num])
        sleep(200)


----

| The moodified code, below, for the while loop, uses the ARROW_W as the starting point with an A button press to repeat hte process of choose a number.

.. code-block:: python

    from microbit import *


    while True:
        display.show(Image.ARROW_W)
        if button_a.is_pressed():
            display.clear()
            sleep(300)
            a = button_a.was_pressed()
            num = select_number()
            display.scroll(chars[num])
        sleep(200)