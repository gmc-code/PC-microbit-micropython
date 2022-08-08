==========================
Potentiometer
==========================

| The potentiometer is a variable resistor.
| Turn it one way to reduce the resistance. Turn it the other way to increase it.

Model
----------------------------------------

#.  Place the potentiomter.
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


Visual display of potentiometer level
----------------------------------------

| The code below takes an analog value from the potentiometer and displays it on the microbit LEDs.
| See the custom images lesson for more on ``display.set_pixel``.
| Firstly, all pixels are set to 0 via ``display.set_pixel(x, y, 0)``.
| The maximum potentiometer reading is 1023, so this can be treated as 1000 for simplicity.
| This gives 5 levels in steps of 200.
| Each row step of 200 can be divided into 10 steps fo brightness from 0 to 9.
| **ylist** has the rows which are at brightness of 9.
| **yval** is the row with variable brightness.


.. code-block:: python
     
    def display_level(level):
        xlist = [0, 1, 2, 3, 4]
  
      # clear:
        ylist = [0, 1, 2, 3, 4]
        for x in xlist:
            for y in ylist:
                display.set_pixel(x, y, 0)

        # display
        val = int((level % 200) * 9 / 200)
        if level < 200:
            yval = 4
            ylist = None
        elif level < 400:
            yval = 3
            ylist = [4]
        elif level < 600:
            yval = 2
            ylist = [3, 4]
        elif  < 800:
            yval = 1
            ylist = [2, 3, 4]
        elif level < 1000:
            yval = 0
            ylist = [1, 2, 3, 4]
        else:
            yval = None
            ylist = [0, 1, 2, 3, 4]

        for x in xlist:
            if yval is not None:
                display.set_pixel(x, yval, val)
            if ylist is not None:
                for y in ylist:
                    display.set_pixel(x, y, 9)


| Try the full code.

.. code-block:: python
    
    from microbit import *


    def display_level(level):
        xlist = [0, 1, 2, 3, 4]
  
      # clear:
        ylist = [0, 1, 2, 3, 4]
        for x in xlist:
            for y in ylist:
                display.set_pixel(x, y, 0)

        # display
        val = int((level % 200) * 9 / 200)
        if level < 200:
            yval = 4
            ylist = None
        elif level < 400:
            yval = 3
            ylist = [4]
        elif level < 600:
            yval = 2
            ylist = [3, 4]
        elif  < 800:
            yval = 1
            ylist = [2, 3, 4]
        elif level < 1000:
            yval = 0
            ylist = [1, 2, 3, 4]
        else:
            yval = None
            ylist = [0, 1, 2, 3, 4]

        for x in xlist:
            if yval is not None:
                display.set_pixel(x, yval, val)
            if ylist is not None:
                for y in ylist:
                    display.set_pixel(x, y, 9)


    def display_potentiometer_value(pin=pin2):
        potval = pin.read_analog()
        display_level(potval)


    while True:
        display_potentiometer_value()
        sleep(20)

