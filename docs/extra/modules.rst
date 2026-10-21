==========================
Modules
==========================

Module list
----------------

| To get a list of built-in modules for the microbit:

| Open the serial terminal in the microbit online editor (3 white vertical dots drop down next to "Show Serial")
| Type: ``help('modules')``

The output is:

.. table:: Microbit modules
   :widths: auto

   =============     =============     =============     =============
   ``__main__``      machine           power             urandom
   antigravity       math              radio             ustruct
   audio             microbit          speech            usys
   builtins          micropython       this              utime
   gc                music             uarray
   log               neopixel          ucollections
   love              os                uerrno
   =============     =============     =============     =============


| Use the REPL and the reset button (or Ctrl+D) to see the output from the print function after flashing to the microbit.

.. code-block:: python

   from microbit import *

   # print("===========================")
   display.scroll("===========================", delay=80)
   help('modules')



