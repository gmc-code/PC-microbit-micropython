==========================
Combined models
==========================

Tasks 
--------------------------

| Use at least 2 different types of devices on the **breadboard**, such as an **LED**, a **buzzer**, a **potentiometer**, a **motor** with transistor.
| Use the microbit display to display **text** and **images**.
| Use **button pressing**.
| Use while and **for loops**.

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
    | When B is pressed, play a built in melody and display the image ``Image.MUSIC_CROTCHET``.

    | 2b. Write code that displays a text message to press A or B. 
    | When A is pressed, repeat 4 times turning on and off a green LED and display the image ``Image.YES``. 
    | When B is pressed, play a built in melody and display the image ``Image.MUSIC_QUAVER``.

    | 2c. Write code that displays a text message to press A or B. 
    | When A is pressed, repeat 5 times turning on and off a yellow LED and display the image ``Image.SQUARE``. 
    | When B is pressed, play a built in melody and display the image ``Image.MUSIC_QUAVERS``.

    | 2d. Write code that displays a text message to press A or B. 
    | When A is pressed, repeat 6 times turning on and off a red LED and display the image ``Image.SAD``. 
    | When B is pressed, play a built in melody and display the image ``Image.MUSIC_CROTCHET``.

    | 2e. Write code that displays a text message to press A or B. 
    | When A is pressed, repeat 7 times turning on and off a green LED and display the image ``Image.SMILE``. 
    | When B is pressed, play a built in melody and display the image ``Image.MUSIC_QUAVERS``

    | **3 LED, potentiometer & Buzzer**
    | 3a. Write code that displays a message to press A or B, and turn on an LED with brightness controlled by a potentiometer.
    | When A is pressed, playing a built in melody while displaying an image. 
    | When B is pressed, repeat 3 times turning on and off an LED, and display 3 different images in sequence from a list of images.

    | 3b. Write code that displays a message to press A or B, and turn on an LED with brightness controlled by a potentiometer.
    | When A is pressed, playing a built in melody while displaying an image. 
    | When B is pressed, repeat 4 times turning on and off an LED, and display 4 different images in sequence from a list of images.

    | 3c. Write code that displays a message to press A or B, and turn on an LED with brightness controlled by a potentiometer.
    | When A is pressed, playing a built in melody while displaying an image. 
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

----

Scaffold for Tasks
--------------------------

See : https://pc-python.readthedocs.io/en/latest/python/functions.html
See: https://pc-microbit-micropython.readthedocs.io/en/latest/breadboards/Organising_with_selection_and_definitions.html

| Break the code up into separate blocks using definitions.
| For each different type of action to do on the microbit have a separate definition.
| An example of such a code structure is below.
| In the scaffold, delete all the ``pass`` statements and replace them with the specific code. 

.. code-block:: python 

    from microbit import *
    import music


    def display_startupmessage():
        # replace pass with the code to display some text
        pass


    def display_textA():
        # replace pass with the code to display some text
        pass


    def display_textB():
        # replace pass with the code to display some text
        pass


    def display_imagesA():
        # replace pass with the code to display one or more images
        pass


    def display_imagesB():
        # replace pass with the code to display one or more images
        pass


    def use_LEDsA():
        # replace pass with the code to control one of more LEDS on their pins
        pass


    def use_LEDsB():
        # replace pass with the code to control one of more LEDS on their pins
        pass


    def use_buzzerA():
        # replace pass with the code to control a buzzer
        pass 


    def use_buzzerB():
        # replace pass with the code to control a buzzer
        pass


    def use_motorA():
        # replace pass with the code to control a motor
        pass 


    def use_motorB():
        # replace pass with the code to control a motor
        pass


    display_startupmessage()
    while True:
        if button_a.is_pressed():
            display_textA()
            display_imagesA()
            use_buzzerA()
            use_motorA()
            use_LEDsA()
        elif button_b.is_pressed():
            display_textB()
            display_imagesB()
            use_buzzerB()
            use_motorB()
            use_LEDsB()
        sleep(1000)

----

Sample Edited Scaffold
--------------------------

| Sample task:
| Write code that displays a message "Hi". 
| When A is pressed, turn on the motor for 3 sec. 
| When B is pressed, turn on the green LED for 2 sec.

| From the scaffold, remove def blocks that are not needed, and definition calls in the ``while True`` loop that are not needed.
| Import all required libraries first.
| Place the code for the definitions next.
| Place the main code last with some code before the ``while True`` loop.

.. code-block:: python 

    from microbit import *


    def display_startupmessage():
        display.scroll('Hi')


    def use_motorA():
        # on pin 0
        pin0.write_digital(1)
        sleep(3000)
        pin0.write_digital(0)


    def use_LEDsB():
        # on pin 1
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)


    display_startupmessage()
    while True:
        if button_a.is_pressed():
            use_motorA()
        elif button_b.is_pressed():
            use_LEDsB()
        sleep(100)
