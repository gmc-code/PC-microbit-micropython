==========================
os module
==========================

.. py:module:: os

| MicroPython contains an ``os`` module based upon the ``os`` module in the Python standard library. 
| The module provides functions relating to the management of the simple on-device persistent file system and information about the current system.

----

listdir
---------------

.. py:function:: listdir()

    | Returns a list of the names of all the files contained within the local persistent on-device file system.

.. code-block:: python

    from microbit import *
    import os

    print(os.listdir())
 
----

remove
---------------

.. py:function:: remove(filename)

    Removes (deletes) the file named in the argument ``filename``. If the file
    does not exist an ``OSError`` exception will occur.

| The code deletes the file at index 1 in the list.

.. code-block:: python

    from microbit import *
    import os

    file_list = os.listdir()
    print(file_list)
    file_to_delete = file_list[1]
    os.remove(file_to_delete)
    file_list = os.listdir()
    print(file_list)

----

size
---------------

.. py:function:: size(filename)

    Returns the size, in bytes, of the file named in the argument ``filename``.
    If the file does not exist an ``OSError`` exception will occur.

| The code prints the files with their size.

.. code-block:: python

    from microbit import *
    import os

    files = os.listdir()
    for f in files:
        print(f, os.size(f))
 
----

uname
---------------

.. py:function:: uname()

    | Returns information identifying the current operating system. The return value is an object with five attributes:

    * ``sysname`` - operating system name
    * ``nodename`` - name of machine on network (implementation-defined)
    * ``release`` - operating system release
    * ``version`` - operating system version
    * ``machine`` - hardware identifier

.. code-block:: python

    from microbit import *
    import os

    info = os.uname()
    print(info)
    print("sysname:", info.sysname)
    print("nodename:", info.nodename)
    print("release:", info.release)
    print("version:", info.version)
    print("machine:", info.machine) 

| The output from the code above was:

::

    * (sysname='microbit', 
    nodename='microbit', 
    release='2.1.0', 
    version='micro:bit v2.1.0+e4321a8 on 2022-09-26; MicroPython v1.18 on 2022-09-26', 
    machine='micro:bit with nRF52833')
    * sysname: microbit
    * nodename: microbit
    * release: 2.1.0
    * version: micro:bit v2.1.0+e4321a8 on 2022-09-26; MicroPython v1.18 on 2022-09-26
    * machine: micro:bit with nRF52833

----

Micropython version
-------------------------

| The micropython that is flashed to the microbit by different software can be determined.
| **Mu editor v1.1.1**, **micropython online editor v3**  and **Thonny v4** flash their version of micropython to the microbit.
| **os.uname().version** returns a string with micropython version in it.
| The code below uses a custom function to get the version.

| e.g. **v1.18** from  **micro:bit v2.1.0+e4321a8 on 2022-09-26; MicroPython v1.18 on 2022-09-26**
| e.g. **v1.15** from  **micro:bit v2.0.0+b51a405 on 2021-06-30; MicroPython v1.15-64-g1e2f0d280 on 2021-06-30**

| The code uses consecutive splits and list indices.
| Firstly the string is split at "MicroPython " and the first index is chosen.
| So this could return the string:  "v1.18 on 2022-09-26".
| The second split is at the spaces with index 0 being chosen.
| THe third split is only needed if there is a long version with a "-" in it. 


.. code-block:: python

    from microbit import *
    import os

    def micropython_version():
        # micro:bit v2.1.0+e4321a8 on 2022-09-26; MicroPython v1.18 on 2022-09-26
        info = os.uname().version
        # last split "-" in case version has - in it.
        mpv = info.split("MicroPython ")[1].split()[0].split("-",)[0]
        return mpv

    mpv = micropython_version()
    while True:  
        display.scroll(mpv)

