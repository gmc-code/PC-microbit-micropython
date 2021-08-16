====================================================
Direction
====================================================

Compass Readings
--------------------

Use ``compass.heading()`` to get an angle from True North where North is 0.

.. code-block:: python

    from microbit import *

    compass.calibrate()

    while True:
        display.scroll(compass.heading(), delay=80)
        sleep(500)

----

.. admonition:: Tasks

    #. Use the code above and turn the microbit till it reads a number close to 0.    
    #. Turn about 90 degrees clockwise to the East and get the reading.
    #. Turn another 90 degrees clockwise to the South and get the reading.
    #. Turn another 90 degrees clockwise to the West and get the reading.

----


Compass Pointer
--------------------

| The compass has readings from 0 to 360 degrees. 
| This can be divided up into 12 directions like the hours on a clock.
| The code below is to text the formula used.
| For readings from 346 to 15, the clock position should be at 12 or 0 o'clock.
| For readings from 16 to 45, the clock position should be at 1 o'clock.
| 
    from microbit import *


    # compass.calibrate()

    while True:
        display.scroll(compass.heading(), delay=60)
        needle = ((compass.heading()+ 15) // 30) % 12
        display.show(Image.ALL_CLOCKS[needle])
        sleep(500)
