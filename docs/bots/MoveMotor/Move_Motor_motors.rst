====================================================
Move Motor motors
====================================================

.. image:: images/move-motor.jpg
    :scale: 50 %
    
KitronikMOVEMotor.py module
----------------------------------------

See :download:`KitronikMOVEMotor.py module <pythonfiles/KitronikMOVEMotor.py>`.

| The KitronikMOVEMotor module is required to control the motors.
| Download the file.
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

