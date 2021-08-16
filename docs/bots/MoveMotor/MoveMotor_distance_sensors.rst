====================================================
MoveMotor distance sensors
====================================================

.. image:: images/move-motor.jpg
    :scale: 50 %
    :align: center


MOVEMotor.py module
----------------------------------------

| The MOVEMotor module is required to control the motors.
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

.. py:class:: MOVEMotorMotors() 

    Set up the buggy motors for use.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

----


Independent motor control
----------------------------------------

| The left and right motors can be run independently using the four methods below:
| ``left_motor(speed=1, duration=None)`` runs the left motor.
| ``right_motor(speed=1, duration=None)`` runs the right motor.
| ``stop_left()`` stops the left motor.
| ``stop_right()`` stops the right motor.

.. py:method:: left_motor(speed=1, duration=None)

    | Make the left motor run. 
    | ``speed`` values are integers or floats (decimals) from -10 to 10.
    | Default ``speed`` is 1.
    | If speed < 0 the motor turns the wheel backwards.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping.

| ``left_motor()`` and ``left_motor(1)`` and ``left_motor(speed=1)`` all set the speed to 1.
| ``left_motor(2, 1000)`` and ``left_motor(2, duration=1000)`` and ``left_motor(speed=2, duration=1000)`` all run the left motor at speed to 2 for 1 sec.

| The code below, using ``left_motor(5)``,  runs the left motor at about half speed.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.left_motor(5)

----

.. admonition:: Tasks

    #. Write code to drive the left motor at speed 2 for 1 second, stop it, run the right motor at speed 2 for 1 sec then stop it.
    #. Write code to drive the right motor at speed 3 while the left motor runs at speed 2 for 3 sec then stop it.
