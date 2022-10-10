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

| The code above output was:

::

    * (sysname='microbit', nodename='microbit', release='2.1.0', version='micro:bit v2.1.0+e4321a8 on 2022-09-26; MicroPython v1.18 on 2022-09-26', machine='micro:bit with nRF52833')
    * sysname: microbit
    * nodename: microbit
    * release: 2.1.0
    * version: micro:bit v2.1.0+e4321a8 on 2022-09-26; MicroPython v1.18 on 2022-09-26
    * machine: micro:bit with nRF52833

