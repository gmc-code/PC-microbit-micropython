====================================================
MoveMotor line sensors
====================================================

Use MOVEMotor library
----------------------------------------

| To use the MOVEMotor module, import it via: ``import MOVEMotor``.

.. code-block:: python

    from microbit import *
    import MOVEMotor


Set up the line sensors
----------------------------------------

.. py:class:: MOVEMotorLineSensors() 

| Set up the line sensors for use.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup line sensor
    line_sensor = MOVEMotor.MOVEMotorLineSensors()

----

Calibrate the line sensors
----------------------------------------

| The line sensors need to be calibrated while over a consistent surface, so that there is no major differences in the left and right sensor readings.
| ``line_sensor_calibrate()`` will store relative differences in the line sensor reading during calibration and use these to make adjustments to any further readings.

.. py:method:: line_sensor_calibrate()

    | Calibrates the line sensors to allow for any slight differences between them.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup line sensor
    line_sensor = MOVEMotor.MOVEMotorLineSensors()

    line_sensor.line_sensor_calibrate()

----

Read values from the line sensors
----------------------------------------

.. py:method:: line_sensor_read(sensor)

    | Return the line sensor value. 
    | Typical values over white are 150 to 200, while over black they are often around 50.
    | ``sensor`` is 'left' or 'right'

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup line sensor
    line_sensor = MOVEMotor.MOVEMotorLineSensors()
    line_sensor.line_sensor_calibrate()

    left_reading = line_sensor.line_sensor_read('left')
    display.scroll(left_reading)

----

.. admonition:: Tasks

    #. Write code to read the right line sensor and display its value.
    #. Write code to read both the left and the right line sensor and display their values with 'L' before the left reading and 'R' before the right reading.

