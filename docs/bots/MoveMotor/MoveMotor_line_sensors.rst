====================================================
MoveMotor line sensors
====================================================

.. image:: images/move-motor.jpg
    :scale: 50 %
    :align: center


MOVEMotor.py module
----------------------------------------

| The MOVEMotor module is required to control the MOVEmotor buggy.
| Download the python file :download:`MOVEMotor.py module <pythonfiles/MOVEMotor.py>`.
| Place it in the mu_code folder: C:\\Users\\username\\mu_code
| The file needs to be copied onto the microbit.
| In Mu editor, with the microbit attached by USB, click the Files icon.
| Files on the microbit are shown on the left.
| Files in the mu_code folder are listed on the right.
| Click and drag the MOVEMotor.py file from the right window to the left window to copy it to the microbit.

Before copying:

.. image:: images/Mu_files.png
    :scale: 50 %

After copying:

.. image:: images/Mu_files_copied.png
    :scale: 50 %


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

    | Read the line sensor value.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup line sensor
    line_sensor = MOVEMotor.MOVEMotorLineSensors()
    line_sensor.line_sensor_calibrate()

----

.. admonition:: Tasks

    #. Write code to drive the left motor at speed 2 for 1 second, stop it, run the right motor at speed 2 for 1 sec then stop it.
    #. Write code to drive the right motor at speed 3 while the left motor runs at speed 2 for 3 sec then stop it.
