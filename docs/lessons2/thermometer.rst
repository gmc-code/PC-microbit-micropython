====================================================
Thermometer
====================================================


Temperature Function
----------------------

The thermometer gets the temperature as an integer in degrees Celsius.

.. py:function:: temperature()

    Return the temperature of the microbit in degrees Celsius.


.. code-block:: python

    from microbit import *
    
    while True:
        temp = temperature()
        display.scroll(str(temp) + 'C')
        sleep(500)

The temperature the thermometer measures will typically be higher than the true temperature because due to the nearby the electronics on the microbit. 

----

.. admonition:: Tasks

    * Plug in the battery pack and move the microbit to a warmer or cooler place. What temperatures do you get?
    * Compare the temperature inside with that outside.
    * Use an if block so that one image is shown when it is below 20 degrees and another image is shown when it is above 20 degrees.
    * Use the A button to store the temperature in the variable ``tempA``. Use the B button to store the temperature in the variable ``tempB``, then calculate the difference between them using ``tempA - tempB`` then scroll the difference.

