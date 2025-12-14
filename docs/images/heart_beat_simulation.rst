==========================
Heart beat simulation
==========================

Pin touching
----------------

| To simulate being connected to a heart monitor, touching **pin0** (or **pin1** or **pin2**) and the Ground pin (**GND**) will be used.
| Hold the GND pin with thumb and forefinger of the right hand.
| **V2**: Touching the logo pin by itself also works. (**pin_logo**)

.. py:function:: is_touched()

    Return True if the pin is being touched with a finger, otherwise return False. It is best to touch the ground pin with the other hand.

| The code below is for testing pin0 touching. When touched, a **0** will be shown.

.. code-block:: python

    from microbit import *

    while True:
        if pin0.is_touched():
            display.show(0)
            sleep(500)
        else:
            display.clear()
        sleep(100)

----

.. admonition:: Tasks

    #. Add an elif branch to test for pin1 touching and display a **1** when it is.
    #. Add another elif branch to test for pin2 touching and display a **2** when it is.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Add an elif branch to test for pin1 touching and display a **1** when it is.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if pin0.is_touched():
                            display.show(0)
                            sleep(500)
                        elif pin1.is_touched():
                            display.show(1)
                            sleep(500)
                        else:
                            display.clear()
                        sleep(100)

            .. tab-item:: Q2

                Add another elif branch to test for pin2 touching and display a **2** when it is.

                .. code-block:: python

                    from microbit import *

                    while True:
                        if pin0.is_touched():
                            display.show(0)
                            sleep(500)
                        elif pin1.is_touched():
                            display.show(1)
                            sleep(500)
                        elif pin2.is_touched():
                            display.show(2)
                            sleep(500)
                        else:
                            display.clear()
                        sleep(100)


----

Pulse design
----------------

| The image below is a design for a heart_beat.
| This is the main shape found in an electrocardiogram.
| To simulate a heart monitor animate this shape from right to left across the 5 by 5 grid.

.. image:: images/heart_beat.png
    :scale: 20 %
    :align: center

|

.. admonition:: Tasks

    #. Plan the design of 7 images to simulate the above heart beat being scrolled from right to left starting with the left edge of the pulse and ending with a flat line. Attempt to complete the code for the 7 images before reading on.

----

| The code has 7 heart beat images which are combined in a list called **heart_beat**.
| When pin0 is touched, the sequence of images is show with 100ms between images.

.. code-block:: python

    from microbit import *

    hb1 = Image("00009:00009:00009:99999:00000")
    hb2 = Image("00090:00090:00090:99999:00009")
    hb3 = Image("00900:00900:00900:99999:00090")
    hb4 = Image("09000:09000:09000:99999:00900")
    hb5 = Image("90000:90000:90000:99999:09000")
    hb6 = Image("00000:00000:00000:99999:90000")
    hb7 = Image("00000:00000:00000:99999:00000")

    heart_beat = [hb1, hb2, hb3, hb4, hb5, hb6, hb7]

    display.show(hb7)

    while True:
        if pin0.is_touched():
            display.show(heart_beat, delay=100, wait=True)


----

| The delay can be adjusted to match particular heart rates (in beats per minute).
| Use the formula to calculate the delay: delay = 60000/(HR * 7)
| For a heart rate of 65 bpm (beats per minute), the delay is 132.

| Use google metronome `<https://g.co/kgs/Rjdr6e.
| Use `<https://www.musicca.com/metronome as an alternative metronome.

.. admonition:: Tasks

    #. Set the google metronome `<https://g.co/kgs/Rjdr6e  to 65 and see if a delay of 132 keeps in time with the metronome.
    #. Set the google metronome `<https://g.co/kgs/Rjdr6e  to 100. Use the formula to calculate the delay required for a HR of 100 bpm. See if this keeps in time with the metronome.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Set the google metronome `<https://g.co/kgs/Rjdr6e  to 65 and see if a delay of 132 keeps in time with the metronome.

                Use:

                .. code-block:: python

                    display.show(heart_beat, delay=132, wait=True)

            .. tab-item:: Q2

                Set the google metronome `<https://g.co/kgs/Rjdr6e  to 100. Use the formula to calculate the delay required for a HR of 100 bpm. See if this keeps in time with the metronome.

                Use:

                .. code-block:: python

                    display.show(heart_beat, delay=85, wait=True)


----

Using a function to calculate the delay for a Heart rate
--------------------------------------------------------------

| Define a function, delay_for_heart_rate(hr), to return the delay needed to simulate a specified heart rate.
| Give the ``hr`` parameter a default value of 60 as in ``def delay_for_heart_rate(hr=60)`` to have a default heart rate of 60 bpm.
| Use the ``int`` function to convert a decimal to a whole number.
| Below is the function.

.. code-block:: python


    def delay_for_heart_rate(hr=60):
        return int(60000/(hr * 7))


| Use the working code below as the starting point for the tasks that follow.

.. code-block:: python

    from microbit import *

    hb1 = Image("00009:00009:00009:99999:00000")
    hb2 = Image("00090:00090:00090:99999:00009")
    hb3 = Image("00900:00900:00900:99999:00090")
    hb4 = Image("09000:09000:09000:99999:00900")
    hb5 = Image("90000:90000:90000:99999:09000")
    hb6 = Image("00000:00000:00000:99999:90000")
    hb7 = Image("00000:00000:00000:99999:00000")

    heart_beat = [hb1, hb2, hb3, hb4, hb5, hb6, hb7]


    def delay_for_heart_rate(hr=60):
        return int(60000/(hr * 7))


    display.show(hb7)

    while True:
        if pin0.is_touched():
            hr_delay = delay_for_heart_rate(60)
            display.show(heart_beat, delay=hr_delay, wait=True)

.. admonition:: Tasks

    #. Add an elif branch to test for pin1 touching and use a heart rate for pin1 of 100 bpm.
    #. Add another elif branch to test for pin2 touching and use a heart rate for pin2 of 150 bpm.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Add an elif branch to test for pin1 touching and use a heart rate for pin1 of 100 bpm.

                .. code-block:: python

                    from microbit import *

                    hb1 = Image("00009:00009:00009:99999:00000")
                    hb2 = Image("00090:00090:00090:99999:00009")
                    hb3 = Image("00900:00900:00900:99999:00090")
                    hb4 = Image("09000:09000:09000:99999:00900")
                    hb5 = Image("90000:90000:90000:99999:09000")
                    hb6 = Image("00000:00000:00000:99999:90000")
                    hb7 = Image("00000:00000:00000:99999:00000")

                    heart_beat = [hb1, hb2, hb3, hb4, hb5, hb6, hb7]


                    def delay_for_heart_rate(hr=60):
                        return int(60000/(hr * 7))


                    display.show(hb7)

                    while True:
                        if pin0.is_touched():
                            hr_delay = delay_for_heart_rate(60)
                            display.show(heart_beat, delay=hr_delay, wait=True)
                        elif pin1.is_touched():
                            hr_delay = delay_for_heart_rate(100)
                            display.show(heart_beat, delay=hr_delay, wait=True)

            .. tab-item:: Q2

                Add another elif branch to test for pin2 touching and use a heart rate for pin2 of 150 bpm.

                .. code-block:: python

                    from microbit import *

                    hb1 = Image("00009:00009:00009:99999:00000")
                    hb2 = Image("00090:00090:00090:99999:00009")
                    hb3 = Image("00900:00900:00900:99999:00090")
                    hb4 = Image("09000:09000:09000:99999:00900")
                    hb5 = Image("90000:90000:90000:99999:09000")
                    hb6 = Image("00000:00000:00000:99999:90000")
                    hb7 = Image("00000:00000:00000:99999:00000")

                    heart_beat = [hb1, hb2, hb3, hb4, hb5, hb6, hb7]


                    def delay_for_heart_rate(hr=60):
                        return int(60000/(hr * 7))


                    display.show(hb7)

                    while True:
                        if pin0.is_touched():
                            hr_delay = delay_for_heart_rate(60)
                            display.show(heart_beat, delay=hr_delay, wait=True)
                        elif pin1.is_touched():
                            hr_delay = delay_for_heart_rate(100)
                            display.show(heart_beat, delay=hr_delay, wait=True)
                        elif pin2.is_touched():
                            hr_delay = delay_for_heart_rate(150)
                            display.show(heart_beat, delay=hr_delay, wait=True)



