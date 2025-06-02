==========================
Combined models
==========================


Scaffold for code:
---------------------

.. code-block:: python

    from microbit import *

    import music
    speaker.off()

    # insert optional code
    while True:
        if button_a.is_pressed():
            # insert code

        elif button_b.is_pressed():
            # insert code

        else:
            # insert code

    # things to include
    # display.scroll("?")
    # display.scroll(Image.YES)
    # mynotes = ["C", "D", "E"]
    # music.play(mynotes)
    # pin1.write_digital(1)
    # pin2.write_digital(1)
    # pin1.write_digital(0)
    # pin2.write_digital(0)
    # sleep(500)
    # for i in range(3):


----

Tasks
--------------------------

| Use at least 2 different types of devices on the **breadboard**, such as an **LED**, a **buzzer**, a **motor** with transistor.
| Use the microbit display to display **text** and **images**.
| Use **button pressing** with button A and button B.
| Use while and **for-loops**.

| Suggestions to complete the task are below.
| Using ``for i in range(n):`` is recommended to repeat a particular action ``n`` times.


.. admonition:: Tasks

    | **1 LED & Buzzer notes**
    | 1a Write code that displays a text message to press A or B.
    | When A is pressed, repeat 3 times turning on and off a red LED and display the image ``Image.NO``.
    | When B is pressed, play 3 different notes and display the image ``Image.MUSIC_CROTCHET``.

    | 1b. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 4 times turning on and off a green LED and display the image ``Image.YES``.
    | When B is pressed, play 4 different notes and display the image ``Image.MUSIC_QUAVER``.

    | 1c. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 5 times turning on and off a yellow LED and display the image ``Image.SQUARE``.
    | When B is pressed, play 5 different notes and display the image ``Image.MUSIC_QUAVERS``.

    | 1d. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 6 times turning on and off a red LED and display the image ``Image.SAD``.
    | When B is pressed, play 6 different notes and display the image ``Image.MUSIC_CROTCHET``.

    | 1e. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 7 times turning on and off a green LED and display the image ``Image.SMILE``.
    | When B is pressed, play 7 different notes and display the image ``Image.MUSIC_QUAVERS``.

    | **2 LED & Buzzer melody**
    | 2a Write code that displays a text message to press A or B.
    | When A is pressed, repeat 3 times turning on and off a red LED and display the image ``Image.NO``.
    | When B is pressed, play a built-in melody and display the image ``Image.MUSIC_CROTCHET``.

    | 2b. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 4 times turning on and off a green LED and display the image ``Image.YES``.
    | When B is pressed, play a built-in melody and display the image ``Image.MUSIC_QUAVER``.

    | 2c. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 5 times turning on and off a yellow LED and display the image ``Image.SQUARE``.
    | When B is pressed, play a built-in melody and display the image ``Image.MUSIC_QUAVERS``.

    | 2d. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 6 times turning on and off a red LED and display the image ``Image.SAD``.
    | When B is pressed, play a built-in melody and display the image ``Image.MUSIC_CROTCHET``.

    | 2e. Write code that displays a text message to press A or B.
    | When A is pressed, repeat 7 times turning on and off a green LED and display the image ``Image.SMILE``.
    | When B is pressed, play a built-in melody and display the image ``Image.MUSIC_QUAVERS``

    | **3 LED, potentiometer & Buzzer**
    | 3a. Write code that displays a message to press A or B, and turn on an LED with brightness controlled by a potentiometer.
    | When A is pressed, playing a built-in melody while displaying an image.
    | When B is pressed, repeat 3 times turning on and off an LED, and display 3 different images in sequence from a list of images.

    | 3b. Write code that displays a message to press A or B, and turn on an LED with brightness controlled by a potentiometer.
    | When A is pressed, playing a built-in melody while displaying an image.
    | When B is pressed, repeat 4 times turning on and off an LED, and display 4 different images in sequence from a list of images.

    | 3c. Write code that displays a message to press A or B, and turn on an LED with brightness controlled by a potentiometer.
    | When A is pressed, playing a built-in melody while displaying an image.
    | When B is pressed, repeat 5 times turning on and off an LED, and display 5 different images in sequence from a list of images.

    | **4 LEDs & Motor**
    | 4a. Write code that displays a message to press A or B.
    | When A is pressed, turn on a green LED, turn on the motor and display the image ``Image.YES``.
    | When B is pressed, turn off the green LED, repeat 2 times turning on and off a red LED, stop the motor and display the image ``Image.NO``.

    | 4b. Write code that displays a message to press A or B.
    | When A is pressed, blink a green LED on and off every 1 sec, turn on and off the motor every 1 sec, and display the image ``Image.YES``.
    | When B is pressed, turn off the green LED, repeat 3 times turning on and off a red LED, stop the motor and display the image ``Image.NO``.

    | 4c. Write code that displays a message to press A or B.
    | When A is pressed, blink a green LED on and off every 2 sec, turn on and off the motor every 2 sec, and display the image ``Image.YES``.
    | When B is pressed, turn off the green LED, repeat 5 times turning on and off a red LED, stop the motor and display the image ``Image.NO``.

    | 4d. Write code that displays a message to press A or B.
    | When A is pressed, blink a green LED on and off every 3 sec, turn on and off the motor every 3 sec, and display the image ``Image.YES``.
    | When B is pressed, turn off the green LED, repeat 10 times turning on and off a red LED, stop the motor and display the image ``Image.NO``.

    | **5 Other combo**
    | 5. Negotiate with teacher.
