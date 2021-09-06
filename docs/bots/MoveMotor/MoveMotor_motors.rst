====================================================
MoveMotor motors
====================================================


Set up the buggy
----------------------------------------

.. py:class:: MOVEMotorMotors() 

| Set up the buggy motors for use.
| Use ``buggy = MOVEMotor.MOVEMotorMotors()`` to be able to use the motor methods on the buggy.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

----

Duration parameter
----------------------------------------

| The Buggy methods that drive the motors have a duration parameter. 
| The duration parameter specifies how long the motor runs for.
| The default duration is ``None``. If the duration is ``None`` or is not specified the motor will run continuously until another command is sent to it.
| e.g. using the duration parameter: ``buggy.forward(10, duration=5000)``  the buggy stops after 5 sec.
| e.g. not using the duration parameter: ``buggy.forward(10)`` the buggy runs forward continuously.

----

Independent motor control
----------------------------------------

| The left and right motors can be run independently using the four methods below:
| ``left_motor(speed=1, duration=None)`` runs the left motor.
| ``right_motor(speed=1, duration=None)`` runs the right motor.
| ``stop_left()`` stops the left motor.
| ``stop_right()`` stops the right motor.

left_motor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: left_motor(speed=1, duration=None)

    | Make the left motor run. 
    | ``speed`` values are integers or floats (decimals) from -10 to 10.
    | Default ``speed`` is 1.
    | If speed < 0 the motor turns the wheel backward.
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

| The code below, using ``left_motor(2, 5000)``,  runs the left motor at speed 2 for 5 sec.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.left_motor(2, 5000)

----

right_motor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: right_motor(speed=1, duration=None)

    | Make the left motor run. 
    | ``speed`` values are integers or floats (decimals) from -10 to 10.
    | Default ``speed`` is 1.
    | If speed < 0 the motor turns the wheel backward.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping.

| ``right_motor()`` and ``right_motor(1)`` and ``right_motor(speed=1)`` all set the speed to 1.
| ``right_motor(2, 1000)`` and ``right_motor(2, duration=1000)`` and ``right_motor(speed=2, duration=1000)`` all run the right motor at speed 2 for 1sec.

| The code below, using ``right_motor(speed=4, duration=3000)``, runs the right motor at speed 4 for 3 sec.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.right_motor(speed=4, duration=3000)

| The code below, using ``right_motor(-10)``, runs the right motor backward at full speed.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.right_motor(-10)


----

stop_left
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: stop_left()

    | Stop the left motor.


| The code below runs the left motor continuously, but after 1 sec, it stops it.
| The motor keeps running during the sleep.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.left_motor()
    sleep(1000)
    buggy.stop_left()


----

stop_right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: stop_right()

    | Stop the right motor.


| The code below runs the right motor at speed 4, then after 2 sec, stops it.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.right_motor(4)
    sleep(2000)
    buggy.stop_right()

----

Stop both motors
----------------------------------------

.. py:method:: stop()

    | Stop both motors.


| The code below runs the left motor at speed 5 and the right motor at speed 2, then after 1500ms stops them both.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()
    
    buggy.left_motor(5)
    buggy.right_motor(2)
    sleep(1500)
    buggy.stop()


----

.. admonition:: Tasks

    #. Write code to drive the left motor at speed 2 for 1 second, stop it, run the right motor at speed 2 for 1 sec then stop it.
    #. Write code to drive the right motor at speed 3 while the left motor runs at speed 2 for 3 sec then stop it.
    #. Write code to drive the left motor at speed 3 while the right motor runs at speed 2 for 3 sec then stop it.
    #. Write code that drives the left side faster than the right side then the right side faster the left side so that it zig zags for 5 sec then stop it.
    #. Write code so that the buggy repetitively zig zags forward for 5 zigs and zags then backward backward for 5 zigs and zags.
    #. Modify the zig zag code so that it uses variables for the 2 motor speeds, the number of zig zags forward and backward, and the time for each zig and zag.

----

Straight line control
----------------------------------------

| The left and right motors can be run so that the buggy moves forward or backward in a straight line:
| ``forward(speed=1, duration=None, decrease_left=0, decrease_right=0)``
| ``backward(speed=1, duration=None, decrease_left=0, decrease_right=0)``
| ``decrease_left`` is used to reduce the motor speed on the left side in case the buggy drifts to the right due to the left motor being slightly faster than the right.
| ``decrease_right`` is used to reduce the motor speed on the right side in case the buggy drifts to the left due to the right motor being slightly faster than the left.
| Any ``decrease_left`` and ``decrease_right`` values used to give a straight line are best found by experimentation.

forward
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: forward(speed=1, duration=None, decrease_left=0, decrease_right=0)

    | Drive the buggy forward.
    | ``speed`` values are integers or floats (decimals) from 0 to 10.
    | Default ``speed`` is 1.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping.
    | ``decrease_left`` and ``decrease_right`` take numbers from 0 to 20. These are converted to a percentage of the maximum analog motor speed of 255 (speed setting 10) so they have similar effect at any speed.
    | ``decrease_left`` and ``decrease_right`` default values are 0.


| ``forward(10, None, 6)`` and ``forward(10, None, 6, 0)`` and ``forward(speed=10, decrease_left=6)`` all set the speed to 10 with the left wheel slowed by roughly 2% (6/255).

| The code below, has an adjustment of 6 to the left motor. 
| This is roughly a 2% (6/255) decrease in speed.
| It drives the buggy forward at speed 10 for 5 secs.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.forward(speed=10, duration=5000, decrease_left=6, decrease_right=0)


----

backward
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: backward(speed=1, duration=None, decrease_left=0, decrease_right=0)

    | Drive the buggy backward.
    | ``speed`` values are integers or floats (decimals) from 0 to 10.
    | Default ``speed`` is 1.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping.
    | ``decrease_left`` and ``decrease_right`` take numbers from 0 to 20. These are converted to a percentage of the maximum analog motor speed of 255 (speed setting 10) so they have similar effect at any speed.
    | ``decrease_left`` and ``decrease_right`` default values are 0.


| ``backward(10, None, 0, 3)`` and ``backward(speed=10, decrease_right=3)`` both set the speed to 10 with the right wheel slowed by roughly 1% (3/255).

| The code below, has an adjustment of 3 to the right motor. 
| This is roughly a 1% (3/255) decrease in speed.
| The parameter names have been omitted in ``forward(8, 4000, 0, 3)``; instead values are in their specified order.
| It drives the buggy backward at speed 8 for 4 secs.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.backward(8, 4000, 0, 3)



----

.. admonition:: Tasks

    #. Write code to drive the buggy as close as possible to a straight line by experimenting with the ``decrease_left`` and ``decrease_right`` values.

----

Turning
----------------------------------------

| The left and right motors are adjusted to turn the buggy with a given radius:
| ``left(speed=1, radius=25)``
| ``right(speed=1, radius=25)``
| When turning left, the left wheel is slowed based on the radius value.
| When turning right, the right wheel is slowed based on the radius value.
| The turning radius is approximate only, and is automatically calculated using 8.5 cm as the distance between the 2 wheels.

left
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: left(speed=1, radius=25, duration=None)

    | Drive the buggy to the left.
    | ``speed`` values are integers or floats (decimals) from -10 to 10.
    | ``speed`` values above 0 drive the buggy forward to the left.
    | ``speed`` values below 0 drive the buggy backward to the left.
    | Default ``speed`` is 1.
    | ``radius`` values are 4 to 800 (in cm)
    | Default ``radius`` is 25 (in cm).
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping, until another command is sent to the motor.

| ``left()`` and ``left(1, 25)`` and ``left(speed=1, radius=25)`` all set the speed to 1 with a left turn of radius 25cm.
| ``left(2, 50, 1000)`` and ``left(2, radius=50, duration=1000)`` and ``left(speed=2, radius=50, duration=1000)`` all set the speed to 2 with a left turn of radius 50cm for 1sec.

| The code below, ``left(speed=3, radius=20, duration=4000)``, drives the buggy forward at speed 3 while it turns left in a circular path of approximate radius 20 cm for 4 secs.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.left(speed=3, radius=20, duration=4000)


----

.. admonition:: Tasks

    #. Write code to drive the buggy to the left at speed 2 in small circles of 10 cm radius.
    #. Write code to drive the buggy to the left at speed 5 in medium circles of 50 cm radius.
    #. Write code to drive the buggy to the left at speed 8 in circles of 20, 40 and 60 cm radius for 5 seconds each. Use a for loop and a list of the radii.

----

right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:method:: right(speed=1, radius=25, duration=None)

    | Drive the buggy to the right.
    | ``speed`` values are integers or floats (decimals) from -10 to 10.
    | ``speed`` values above 0 drive the buggy forward to the right.
    | ``speed`` values below 0 drive the buggy backward to the right.
    | Default ``speed`` is 1.
    | ``radius`` values are 4 to 800 (in cm)
    | Default ``radius`` is 25 (in cm).
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping, until another command is sent to the motor.

| ``right()`` and ``right(1, 25)`` and ``right(speed=1, radius=25)`` all set the speed to 1 with radius 25cm.
| ``right(2, 50, 1000)`` and ``right(2, radius=50, duration=1000)`` and ``right(speed=2, radius=50, duration=1000)`` all set the speed to 2 with a right turn of radius 50cm for 1sec.

| The code below, ``right(speed=2, radius=40, duration=3000)``, drives the buggy forward at speed 2 while it turns right in a circular path of approximate radius 40 cm for 3 secs.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.right(speed=2, radius=40, duration=3000)

----

.. admonition:: Tasks

    #. Write code to drive the buggy to the right at speed 4 in small circles of 5 cm radius.
    #. Write code to drive the buggy to the right at speed 7 in medium circles of 80 cm radius.
    #. Write code to drive the buggy to the right at speed 10 in circles of increasing size. Use a range function to increase the radius every 4 seconds from 10 to 100 in steps of 10.

----

Spinning
----------------------------------------

| Spin the buggy to the left or right at the chosen speed using:
| ``spin(speed=1, direction='left, duration=None)``
| When spining left, the left wheel goes backward while the right wheel goes forward.
| When spining right, the right wheel goes backward while the left wheel goes forward.


.. py:method:: spin(speed=1, direction='left', duration=None)

    | Spin the buggy on the spot.
    | ``speed`` values are integers or floats (decimals) from 0 to 10.
    | Default ``speed`` is 1.
    | ``direction`` values are ``left`` or ``right``, while any other values will spin the buggy left. 
    | Default ``direction`` is 'left'.
    | ``duration`` values are integers above 0.
    | Default ``duration`` is None.
    | The motor will stop after a given duration in milliseconds.
    | If the duration is None, the motor runs without stopping, until another command is sent to the motor.

| ``spin()`` and ``spin(1, 'left')`` and ``spin(speed=1, direction='left')`` all spin the buggy to the left at speed 1.
| ``spin(3, 'left', 2000)`` and ``spin(3, direction='left', duration=2000)`` and ``spin(speed=3, direction='left', duration=2000)`` all spin the buggy to the left at speed 3 for 2 secs.

| The code below, ``spin(2, 'right', 4000)``, spins the buggy to the right at speed 2 for 4 secs.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    # setup buggy
    buggy = MOVEMotor.MOVEMotorMotors()

    buggy.spin(2, 'right', 4000)

----

.. admonition:: Tasks

    #. Write code to spin the buggy to the left at speed 4 for 5 seconds.
    #. Write code to spin the buggy to the right at speed 6 for 3 seconds.
    #. Write code to spin the buggy to the left for 3 seconds then to right for 3 seconds at speed 6.
    #. Write code to drive the buggy in a polygonal path (many straight sides) by combining short drives forward with short spins.

