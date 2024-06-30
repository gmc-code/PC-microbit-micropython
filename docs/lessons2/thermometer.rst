====================================================
Thermometer
====================================================


Temperature Function
----------------------

The thermometer gets the temperature as an integer in degrees Celsius.

.. py:function:: temperature()

    Return the temperature of the microbit in degrees Celsius.

The temp variable below is an integer. It has to be first converted to a string to join it with the unit symbol, C.

.. code-block:: python

    from microbit import *
    
    while True:
        temp = temperature()
        display.scroll(str(temp) + 'C')
        sleep(500)

The temperature the thermometer measures will typically be higher than the true temperature due to heat from the nearby electronics on the microbit. 

----

.. admonition:: Exercises

    * Plug in the battery pack and move the microbit to a warmer or cooler place. What temperatures do you get?
    * Compare the temperature inside with that outside.    
    * Place the microbit on a paper towel in the freezer or fridge for 2 min and read the temperature.

----

.. admonition:: Tasks

    * Use an if block so that one image is shown when it is below 20 degrees and another image is shown when it is above 20 degrees.
    * Use the A button to store the temperature in the variable ``tempA``. Use the B button to store the temperature in the variable ``tempB``. Calculate the difference between them using ``tempA - tempB`` and scroll this difference.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use an if block so that one image is shown when it is below 25 degrees and another image is shown when it is 20 degrees or higher.

                .. code-block:: python

                    from microbit import *

                    while True:
                        temp = temperature()
                        #display.scroll(temp)
                        if temp < 25:
                            display.show(Image.UMBRELLA)
                        else:
                            display.show(Image.TSHIRT)

            .. tab-item:: Q2

                Use the A button to store the temperature in the variable ``tempA``. Use the B button to store the temperature in the variable ``tempB``. Calculate the difference between them using ``tempA - tempB`` and scroll this difference. To make sure that both temperature variables have a value, set them both before the ``while True`` loop.

                .. code-block:: python

                    from microbit import *

                    tempA = temperature()
                    tempB = temperature()
                    while True:
                        temp = temperature()
                        if button_a.is_pressed():
                            tempA = temp
                        elif button_b.is_pressed():
                            tempB = temp
                        display.scroll(tempA - tempB)
                        sleep(200)

----

.. admonition:: Project

    | Keep track of the lowest and highest temperatures recorded by using 3 variables: current_temp is the current temperature reading, max_temp is the maximum temperature and min_temp is the minimum temperature. 
    | At the start, set all 3 variables to the same value and scroll that value. Then use a while loop to take a reading every second and put it in current_temp, then update the max_temp or min_temp depending on the new reading. 
    | If current_temp is less than (<) min_temp, update min_temp. 
    | If the current_temp is greater than (>) max_temp, update max_temp. 
    | Use the A button to scroll min_temp. 
    | Use the B button to scroll max_temp. 
    | Press down both A and B buttons together to scroll the difference between the max and min temperatures.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Project

                .. code-block:: python

                    from microbit import *

                    current_temp = temperature()
                    max_temp = current_temp
                    min_temp = current_temp
                    display.scroll(current_temp, delay=80)
                    while True:
                        current_temp = temperature()
                        if current_temp < min_temp:
                            min_temp = current_temp
                        elif current_temp > max_temp:
                            max_temp = current_temp
                        if button_a.is_pressed() and button_b.is_pressed():
                            display.scroll(max_temp - min_temp, delay=80)
                        elif button_a.is_pressed():
                            display.scroll(min_temp, delay=80)
                        elif button_b.is_pressed():
                            display.scroll(max_temp, delay=80)
                        sleep(1000)
