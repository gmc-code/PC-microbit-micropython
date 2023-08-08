==========================
Models using definitions
==========================


Moving code to definitions
-----------------------------

| Beginning with the code below, restructure it to use definitions.


.. code-block:: python 

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin0.write_digital(1)
        elif button_b.is_pressed():
            pin0.write_digital(0)
        else:
            display.scroll('a or b')

| The restructured code is below.

.. code-block:: python 

    from microbit import *


    def A_action():
        pin0.write_digital(1)

    def B_action():
        pin0.write_digital(0)

    def no_action():
        display.scroll('a or b')

    while True:
        if button_a.is_pressed():
            A_action()
        elif button_b.is_pressed():
            B_action()
        else:
            no_action()



Building on each definitions
-----------------------------

| Beginning with the code above each def can have several related actions.


.. code-block:: python 

    from microbit import *


    def A_action():
        pin0.write_digital(1)
        sleep(3000)
        pin0.write_digital(0)

    def B_action():
        for _ in range(3)
            pin0.write_digital(1)
            sleep(500)
            pin0.write_digital(0)
            sleep(500)

    def no_action():
        display.scroll('a or b')

    while True:
        if button_a.is_pressed():
            A_action()
        elif button_b.is_pressed():
            B_action()
        else:
            no_action()

----

Better names for definitions
------------------------------

Instead of do_A_action or similar def names, the defs below have more informative names.

| Sample task:
| Write code that displays a message "A or B". 
| When A is pressed, turn on the motor for 3 sec. 
| When B is pressed, turn on the green LED for 2 sec.

| From the scaffold, remove def blocks that are not needed, and definition calls in the ``while True`` loop that are not needed.
| Import all required libraries first.
| Place the code for the definitions next.
| Place the main code last with some code before the ``while True`` loop.

.. code-block:: python 

    from microbit import *


    def display_startupmessage():
        display.scroll('A or B')


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

----

Scaffold for Tasks
--------------------------

| Break the code up into separate blocks using definitions.
| For each different type of action to do on the microbit have a separate definition.
| An example of such a code structure is below.
| To use the scaffold, delete all the ``pass`` statements and replace them with the specific code. 

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

