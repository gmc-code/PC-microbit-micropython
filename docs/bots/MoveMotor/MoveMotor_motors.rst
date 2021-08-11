====================================================
MoveMotor motors
====================================================

.. image:: images/move-motor.jpg
    :scale: 50 %
    
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

.. image:: images/Mu_files.PNG
    :scale: 50 %

After copying:

.. image:: images/Mu_files_copied.PNG
    :scale: 50 %


Use MOVEMotor library
----------------------------------------

| To use the MOVEMotor module, import it via: ``import MOVEMotor``.

.. code-block:: python

    from microbit import *
    import MOVEMotor


Set up buggy
----------------------------------------

.. py:function:: MOVEMotor.MOVEMotor_motors()

    Set up the buggy motors for use.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

----

Independent motor control
----------------------------------------

| The left and right motors can be run independently using the four methods below:
| ``left_motor(speed=1)`` runs the left motor.
| ``right_motor(speed=1)`` runs the right motor.
| ``stop_left()`` stops the left motor.
| ``stop_right()`` stops the right motor.

.. py:function:: left_motor(speed=1)

    | Make the left motor run. 
    | Speed values are integers or floats (decimals) from -10 to 10.
    | Default speed is 1.
    | If speed < 0 the motor goes in backward.


| The code below, using ``left_motor(5)``,  runs the left motor at about half speed.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

    buggy.left_motor(5)

----

.. py:function:: right_motor(speed=1)

    | Make the left motor run. 
    | Speed values are integers or floats (decimals) from -10 to 10.
    | Default speed is 1.
    | If speed < 0 the motor goes in backward.


| The code below, using ``right_motor(-10)``, runs the right motor in backward at full speed.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

    buggy.right_motor(-10)

----

.. py:function:: stop_left()

    | stops the left motor.


| The code below runs the left motor then stops it.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

    buggy.left_motor()
    sleep(1000)
    buggy.stop_left()


----

.. py:function:: stop_right()

    | stops the right motor.


| The code below runs the right motor then stops it.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

    buggy.right_motor()
    sleep(1000)
    buggy.stop_right()

----

Stop both motors
----------------------------------------

.. py:function:: stop()

    | Stops both motors.


| The code below runs the left motor at about half speed.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()
    
    buggy.left_motor(5)
    buggy.right_motor()
    sleep(1000)
    buggy.stop()


----

.. admonition:: Tasks

    #. Write code to drive the left motor at speed 2 for 1 second, stop it, run the right motor at speed 2 for 1 sec then stop it.
    #. Write code to drive the right motor at speed 3 while the left motor runs at speed 2 for 3 sec then stop it.
    #. Write code to drive the left motor at speed 3 while the right motor runs at speed 2 for 3 sec then stop it.
    #. Write code that drives the left side faster than the right side then the right side faster the left side so that it zig zags for 5 sec then stop it.
    #. Write code that it repetitively zig zags forwards for 5 zigs and zags then backwards backwards for 5 zigs and zags.
    #. Modify the zig zag code so that it uses variables for the 2 motor speeds, the number of zig zags forwards and in backward, and the time for each zig and zag.

----

Straight line control
----------------------------------------

| The left and right motors can be run so that the buggy moves forwards or backwards in a straight line:
| ``forward(speed=1, decrease_left=0, decrease_right=0)``
| ``backward(speed=1, decrease_left=0, decrease_right=0)``

.. py:function:: forward(speed=1, decrease_left=0, decrease_right=0)

    | Drive the buggy forwards.
    | Speed values are integers or floats (decimals) from -10 to 10.
    | Default speed is 1.
    | decrease_left and decrease_right take numbers from 0 to 20. These are converted to a percentage of the maximum analog motor speed of 255 (speed setting 10) so they have similar effect at any speed.
    | decrease_left and decrease_right default values are 0.
    | What works to give a straight line is best found by experimentation.


| The code below, has an adjustment of 6 to the left motor. This is roughly a 2% (6/255) decrease in speed.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

    buggy.forward(speed=10, decrease_left=6, decrease_right=0)
    sleep(3000)
    buggy.stop()

----

.. py:function:: backward(speed=1, decrease_left=0, decrease_right=0)

    | Drive the buggy backwards.
    | Speed values are integers or floats (decimals) from -10 to 10.
    | Default speed is 1.
    | decrease_left and decrease_right are used to adjust the motor speed on each side in case the buggy doesn't go straight due to one motor being slightly faster than the other.
    | decrease_left and decrease_right take numbers from 0 to 20. These are converted to a percentage of the maximum analog motor speed of 255 (speed setting 10) so they have similar effect at any speed.
    | decrease_left and decrease_right default values are 0.
    | What works to give a straight line is best found by experimentation.


| The code below, has an adjustment of 3 to the right motor. This is roughly a 1% (3/255) decrease in speed.
| The parameter names have been omitted in ``forward(10, 0, 3)``; instead values are in their specified order.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

    buggy.forward(10, 0, 3)
    sleep(3000)
    buggy.stop()


----

.. admonition:: Tasks

    #. Write code to drive the buggy as close as possible to a straight line by experimenting with the decrease_left and decrease_right values.

----

Turning
----------------------------------------

| The left and right motors can be run so that the buggy moves forwards or backwards in a straight line:
| ``Left(self, speed=1, tightness='standard')``
| ``Right(self, speed=1, tightness='standard')``

.. py:function:: forward(speed=1, decrease_left=0, decrease_right=0)

    | Drive the buggy forwards.
    | Speed values are integers or floats (decimals) from -10 to 10.
    | Default speed is 1.
    | decrease_left and decrease_right take numbers from 0 to 20. These are converted to a percentage of the maximum analog motor speed of 255 (speed setting 10) so they have similar effect at any speed.
    | decrease_left and decrease_right default values are 0.
    | What works to give a straight line is best found by experimentation.


| The code below, has an adjustment of 6 to the left motor. This is roughly a 2% (6/255) decrease in speed.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotor_motors()

    buggy.forward(speed=10, decrease_left=6, decrease_right=0)
    sleep(3000)
    buggy.stop()

----





