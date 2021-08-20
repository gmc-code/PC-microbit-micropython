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
    * Place the microbit on a paper towel in the freezer or fridge for 2 min and read teh temperature.
    * Use an if block so that one image is shown when it is below 20 degrees and another image is shown when it is above 20 degrees.
    * Use the A button to store the temperature in the variable ``tempA``. Use the B button to store the temperature in the variable ``tempB``, then calculate the difference between them using ``tempA - tempB`` then scroll the difference.

----

.. admonition:: Project

    * Keep track of the lowest and highest temperatures recorded by using 3 variables: current_temp is the current temperature reading, max_temp is the maximum temperature and min_temp is the minimum temperature. At the start, set all 3 variables to the same value and scrolls that value. Then use a while loop to take a reading every second and put it in current_temp, then update the max_temp or min_temp depending on the new reading. If current_temp is less than (<) min_temp, update min_temp. If the current_temp is greater than (>) max_temp, update max_temp. Use the A button to scroll min_temp. Use the B button to scroll max_temp. Press down both A and B buttons together to scroll the difference between the max and min temperatures


