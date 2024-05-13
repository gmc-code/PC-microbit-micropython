==========================
Potentiometer
==========================

| The potentiometer is a variable resistor.
| Turn it one way to reduce the resistance. Turn it the other way to increase it.

----

Model
----------------------------------------

#.  Place the potentiometer.
#.  Connect with the jumper wires.

.. image:: images/potentiometer1_bb.png
    :scale: 50 %

.. image:: images/potentiometer_1.jpg
    :scale: 30 %

----

Read analog
----------------------------------------

| To read the value of the potentiometer use ``pin2.read_analog``.
| The code below reads the value and displays it.
| Try turning it from side to side to see the effect.

.. code-block:: python

    from microbit import *

    while True:
        potval = pin2.read_analog()
        display.scroll(potval, delay=80)
        sleep(20)

----

.. admonition:: Tasks

    #. Modify the code to use a function, ``display_potentiometer_value``, that reads the potentiometer and scrolls its value. Include a default parameter for the pin.
    
    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to use a function, ``display_potentiometer_value``, that reads the potentiometer and scrolls its value. Include a default parameter for the pin.

                    .. code-block:: python
                        
                        from microbit import *


                        def display_potentiometer_value(pin=pin2):
                            potval = pin.read_analog()
                            display.scroll(potval, delay=80)


                        while True:
                            display_potentiometer_value()
                            sleep(20)

----


Advanced: Power meter simulation
----------------------------------------

.. sidebar::

    .. image:: images/potentiometer_level.png
        :scale: 50 %
        :align: center

| The code below takes an analog value from the potentiometer and displays it on the microbit LEDs.
| See the custom images lesson for more on ``display.set_pixel``.
| The maximum potentiometer reading is 1023, so this can be treated as 1000 for simplicity.
| This gives 5 levels in steps of 200.
| Each row step of 200 can be divided into 10 steps of brightness from 0 to 9.
| 3 variables are used for each section of the display: **yclearlist** for the blank rows, **ylist** for the full brightness rows and **yval** for the row in between that is of partial brightness.
| **yclearlist** has the rows which are at brightness of 0.
| **ylist** has the rows which are at brightness of 9.
| **yval** is the row with variable brightness.
| Each of these variables is first checked to see if it is ``None`` before setting the pixels it controls.


.. code-block::
     
    def display_level(level):
        xlist = [0, 1, 2, 3, 4]

        # display
        val = int((level % 200) * 9 / 200)
        if level < 200:
            yval = 4
            ylist = None
            yclearlist = [0, 1, 2, 3]
        elif level < 400:
            yval = 3
            ylist = [4]
            yclearlist = [0, 1, 2]
        elif level < 600:
            yval = 2
            ylist = [3, 4]
            yclearlist = [0, 1]
        elif level < 800:
            yval = 1
            ylist = [2, 3, 4]
            yclearlist = [0]
        elif level < 1000:
            yval = 0
            ylist = [1, 2, 3, 4]
            yclearlist = None
        else:
            yval = None
            ylist = [0, 1, 2, 3, 4]
            yclearlist = None

        for x in xlist:
            if yval is not None:
                display.set_pixel(x, yval, val)
            if ylist is not None:
                for y in ylist:
                    display.set_pixel(x, y, 9)
            if yclearlist is not None:
                for y in yclearlist:
                    display.set_pixel(x, y, 0)

| Try the full code.

.. code-block:: python
    
    from microbit import *


    def display_level(level):
        xlist = [0, 1, 2, 3, 4]

        # display
        val = int((level % 200) * 9 / 200)
        if level < 200:
            yval = 4
            ylist = None
            yclearlist = [0, 1, 2, 3]
        elif level < 400:
            yval = 3
            ylist = [4]
            yclearlist = [0, 1, 2]
        elif level < 600:
            yval = 2
            ylist = [3, 4]
            yclearlist = [0, 1]
        elif level < 800:
            yval = 1
            ylist = [2, 3, 4]
            yclearlist = [0]
        elif level < 1000:
            yval = 0
            ylist = [1, 2, 3, 4]
            yclearlist = None
        else:
            yval = None
            ylist = [0, 1, 2, 3, 4]
            yclearlist = None

        for x in xlist:
            if yval is not None:
                display.set_pixel(x, yval, val)
            if ylist is not None:
                for y in ylist:
                    display.set_pixel(x, y, 9)
            if yclearlist is not None:
                for y in yclearlist:
                    display.set_pixel(x, y, 0)


    def display_potentiometer_level(pin=pin2):
        potval = pin.read_analog()
        display_level(potval)


    while True:
        display_potentiometer_level()
        sleep(20)
