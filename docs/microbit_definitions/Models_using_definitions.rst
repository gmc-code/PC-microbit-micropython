==========================
Models using definitions
==========================

| The following examples use write_digital to power a device connected to a given pin number.
| In most examples, pin0 is used, but pin1 or pin2 could just as easily be used.

----

Moving code to definitions
-----------------------------

| Beginning with the code below, restructure it to use definitions.
| Reorganising the code without changing what is does is called **refactoring**.


.. code-block:: python 

    from microbit import *

    while True:
        if button_a.is_pressed():
            # turn on device on pin0
            pin0.write_digital(1)
        elif button_b.is_pressed():
            # turn off device on pin0
            pin0.write_digital(0)
        else:
            # helpful indication that athe A button or B needs pressing
            display.scroll('A or B', delay=80)

| The restructured code is below.

.. code-block:: python 

    from microbit import *


    def A_action():
        # turn on device on pin0
        pin0.write_digital(1)

    def B_action():
        # turn off device on pin0
        pin0.write_digital(0)

    def no_action():
        # helpful indication that athe A button or B needs pressing
        display.scroll('A or B')

    while True:
        if button_a.is_pressed():
            A_action()
        elif button_b.is_pressed():
            B_action()
        else:
            no_action()


----

Building on each definition
-----------------------------

| Beginning with the code above, the ``A_action()`` and ``B_action()`` defs have scrolling text added to them.
| The special `wait` parameter is set to `False` so that the scrolling is non-blocking.
 
.. code-block:: python 

    from microbit import *


    def A_action():
        # turn on device on pin0
        display.scroll('ON', wait=False, delay=70)
        pin0.write_digital(1)

    def B_action():
        # turn off device on pin0
        display.scroll('OFF', wait=False, delay=70)
        pin0.write_digital(0)

    def no_action():
        # helpful indication that athe A button or B needs pressing
        display.scroll('A or B')

    while True:
        if button_a.is_pressed():
            A_action()
        elif button_b.is_pressed():
            B_action()
        else:
            no_action()

----

.. admonition:: Tasks

    Modify the def blocks to add the functionality described below.

    #. Modify the A_action() def to turn on the device for 3sec. Modify the B_action() def to on and off with a delay of 0.3sec 3 times using a for-loop.
    #. Modify the A_action() def to play a `c4:8` note 3 tiems with 0.5 sec between them and scroll the play times. Modify the B_action() def to play an `e5:4` note 5 times with 0.5 sec between them and scroll the play times.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the A_action() def to turn on the device for 3sec. Modify the B_action() def to on and off with a delay of 0.5sec 3 times using a for-loop.

                    .. code-block:: python 

                        from microbit import *


                        def A_action():
                            # turn on for 3 seconds
                            pin0.write_digital(1)
                            sleep(3000)
                            pin0.write_digital(0)

                        def B_action():
                            # turn on and off with 0.5 sec delays, 3 times
                            for _ in range(3)
                                pin0.write_digital(1)
                                sleep(500)
                                pin0.write_digital(0)
                                sleep(500)

                        def no_action():
                            display.scroll('A or B')

                        while True:
                            if button_a.is_pressed():
                                A_action()
                            elif button_b.is_pressed():
                                B_action()
                            else:
                                no_action()

                .. tab-item:: Q2

                    Modify the A_action() def to play a `c4:8` note 3 tiems with 0.5 sec between them and scroll the play times. Modify the B_action() def to play an `e5:4` note 5 times with 0.5 sec between them and scroll the play times.

                    .. code-block:: python

                        from microbit import *
                        import music

                        speaker.off()

                        def A_action():
                            speaker.on()
                            note = 'c4:8'
                            for n in range(3):
                                display.scroll(n, wait=False, delay=50)
                                music.play(note)
                                sleep(500)

                        def B_action():
                            speaker.off()
                            note = 'e5:4'
                            for n in range(5):
                                display.scroll(n, wait=False, delay=50)
                                music.play(note)
                                sleep(500)

                        def no_action():
                            display.scroll('A or B')

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
        # turn on the motor on pin0, wait 3 sec, then off
        pin0.write_digital(1)
        sleep(3000)
        pin0.write_digital(0)


    def use_LEDsB():
        # turn on the LEDS on pin1, wait 2 sec, then off
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

| Imagine that button pressing will control 5 things: text displayed, images shown, LEDS, the motor and the buzzer.
| For each different type of action to do on the microbit have a separate definition.
| An example of such a code structure is below.
| To use the scaffold, delete the unwanted def blocks and threir calls. 

.. code-block:: python 

    from microbit import *
    import music


    def display_startupmessage():
        display.scroll('A or B')


    def display_textA():
        display.scroll('A')


    def display_textB():
        display.scroll('B')


    def display_imagesA():
        display.show(Image.YES)


    def display_imagesB():
        display.show(Image.NO)


    def use_LEDsA():
        pin1.write_digital(1)


    def use_LEDsB():
        pin1.write_digital(1)


    def use_buzzerA():
        music.play("c4:8")


    def use_buzzerB():
        music.play("e5:2")


    def use_motorA():
        pin2.write_digital(1)


    def use_motorB():
        pin2.write_digital(0)


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

