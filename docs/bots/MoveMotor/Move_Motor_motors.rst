====================================================
Move Motor motors
====================================================

.. image:: images/move-motor.jpg
    :scale: 50 %
    
KitronikMOVEMotor.py module
----------------------------------------


| The KitronikMOVEMotor module is required to control the motors.
| Download the library python file :download:`KitronikMOVEMotor.py module <pythonfiles/KitronikMOVEMotor.py>`.
| Place it in the mu_code folder: C:\\Users\\username\\mu_code
| The file needs to be copied onto the microbit.
| In Mu editor, with the microbit attached by USB, click the Files icon.
| Files on the microbit are shown on the left.
| Files in the mu_code folder are listed on the right.
| Click and drag the KitronikMOVEMotor.py file from the right window to the left window to copy it to the microbit.

Before copying:

.. image:: images/Mu_files.PNG
    :scale: 50 %

After copying:

.. image:: images/Mu_files_copied.PNG
    :scale: 50 %


Use KitronikMOVEMotor library
----------------------------------------

| To use the KitronikMOVEMotor library, import it: ``import KitronikMOVEMotor``.

.. code-block:: python

    from microbit import *
    import KitronikMOVEMotor


Set up buggy
----------------------------------------

.. py:function:: KitronikMOVEMotor.MOVEMotor()

    Set up the buggy motors for use.

.. code-block:: python

    from microbit import *
    import KitronikMOVEMotor


    # setup buggy
    buggy = KitronikMOVEMotor.MOVEMotor()

----

Independent motor control
----------------------------------------

| The left and right motors can be run independently using the four methods below:
| ``LeftMotor(speed=1)`` runs the left motor.
| ``RightMotor(speed=1)`` runs the right motor.
| ``StopLeft()`` stops the left motor.
| ``StopRight()`` stops the right motor.

.. py:function:: LeftMotor(speed=1)

    | Make the left motor run. 
    | Speed values are integers or floats (decimals) from -10 to 10.
    | Default speed is 1.
    | If speed < 0 the motor goes in reverse.


| The code below runs the left motor at about half speed.

.. code-block:: python

    from microbit import *
    import KitronikMOVEMotor


    # setup buggy
    buggy = KitronikMOVEMotor.MOVEMotor()

    buggy.LeftMotor(5)

----

.. py:function:: RightMotor(speed=1)

    | Make the left motor run. 
    | Speed values are integers or floats (decimals) from -10 to 10.
    | Default speed is 1.
    | If speed < 0 the motor goes in reverse.


| The code below runs the right motor in reverse at full speed.

.. code-block:: python

    from microbit import *
    import KitronikMOVEMotor


    # setup buggy
    buggy = KitronikMOVEMotor.MOVEMotor()

    buggy.RightMotor(-10)

----

.. py:function:: StopLeft()

    | Stops the left motor.


| The code below runs the left motor then stops it.

.. code-block:: python

    from microbit import *
    import KitronikMOVEMotor


    # setup buggy
    buggy = KitronikMOVEMotor.MOVEMotor()

    buggy.LeftMotor()
    sleep(1000)
    buggy.StopLeft()


----

.. py:function:: StopRight()

    | Stops the right motor.


| The code below runs the right motor then stops it.

.. code-block:: python

    from microbit import *
    import KitronikMOVEMotor


    # setup buggy
    buggy = KitronikMOVEMotor.MOVEMotor()

    buggy.RightMotor()
    sleep(1000)
    buggy.StopRight()

----

Stop motors
----------------------------------------

.. py:function:: Stop()

    | Stops both motors.


| The code below runs the left motor at about half speed.

.. code-block:: python

    from microbit import *
    import KitronikMOVEMotor


    # setup buggy
    buggy = KitronikMOVEMotor.MOVEMotor()
    # run left motor
    buggy.LeftMotor(5)

----



