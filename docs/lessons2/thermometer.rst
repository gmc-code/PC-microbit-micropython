====================================================
Thermometer
====================================================


Basic Functions
----------------
There is only one basic function for the thermometer – to get the temperature, which is returned as an integer in degrees Celsius:

.. py:function:: temperature()

    Return the temperature of the micro:bit in degrees Celcius.


.. code-block:: python

    from microbit import *
    
    while True:
        temp = temperature()
        display.scroll(str(temp) + 'C')
        sleep(500)

The temperature the thermometer measures will typically be higher than the true temperature because it’s getting heated from both the room and the electronics on the board. 

----

.. admonition:: Tasks

    * Plug in the battery pack and move the microbit to a warmer or cooler place. What temperatures do you get?
    * Compare the temperature inside with that outside.
    * Use an if block so that one image is shown when it is below 20 degrees and another image is shown when it is above 20 degrees.


