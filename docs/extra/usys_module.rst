==========================
usys module
==========================


| See: `<https://docs.micropython.org/en/latest/library/sys.html>`_
| Some functions are listed below. Use ``print(help(usys))`` to get the full list.

.. py:function::  usys.version_info

    | Returns the Python language version, as a tuple of ints.
    | e.g. (3, 4, 0)

.. py:function::  usys.version

    | Returns the Python language version, as a string.
    | e.g. 3.4.0

.. py:function::  usys.platform

    | Returns the platform that MicroPython is running on.
    | e.g. microbit

.. py:function::  usys.implementation

    | Returns a tuple, (name='micropython', version=(1, 18, 0)), with information about the current MicroPython implementation with following attributes:
    | name - string e.g. micropython. Also returned directly by: usys.implementation.name
    | version - tuple (major, minor, micro), e.g. (1, 18, 0) Also returned by: usys.implementation.version

.. py:function::  usys.maxsize

    | Returns the maximum integer value that can be represented on the platform, which is 2,147,483,647 for a 32-bit system.

.. py:function::  usys.modules

    | Returns a dictionary of loaded modules, not including builtin modules.
    | e.g. {'log': <module 'log'>, 'neopixel': <module 'neopixel'>}

.. py:function::  usys.path

    | Returns a list of directories to search for imported modules.
    | e.g. ['', '.frozen']

.. py:function::  usys.byteorder

    | Returns the byte order of the system ("little" or "big").
    | e.g. little

.. py:function::  usys.argv

    | Returns a list of arguments the current program was started with. e.g. []

----

| The code below uses the REPL to print the output.

.. code-block:: python

    from microbit import *
    import usys

    # print(help(usys))
    print('version_info:', usys.version_info)
    print('version:', usys.version)
    print('platform:', usys.platform)
    print('implementation name:', usys.implementation.name)
    print('implementation version:', usys.implementation.version)
    print('maxsize:', usys.maxsize)
    if usys.maxsize > 2147483648:
        print('64-bit')
    else:
        print('32-bit')
    print('path:', usys.path)
    print('modules:', usys.modules)
    print('byteorder:', usys.byteorder)
    print('argv:', usys.argv)

    '''
    version_info: (3, 4, 0)
    version: 3.4.0
    platform: microbit
    implementation name: micropython
    implementation version: (1, 18, 0)
    maxsize: 2147483647
    32-bit
    path: ['', '.frozen']
    modules: {}
    byteorder: little
    argv: []
    '''

