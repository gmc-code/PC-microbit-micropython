==========================
usys module
==========================

.. py:module:: usys

| See: `<https://docs.micropython.org/en/latest/library/sys.html>`_
| Some attributes are listed below. Use ``help(usys)`` to get the full list.
| These are values, not functions, so they are used without brackets, e.g. ``usys.platform``.

.. py:data::  version_info

    | The Python language version, as a tuple of ints.
    | e.g. (3, 4, 0)

.. py:data::  version

    | The Python language version, as a string.
    | e.g. 3.4.0

.. py:data::  platform

    | The platform that MicroPython is running on.
    | e.g. microbit

.. py:data::  implementation

    | Information about the current MicroPython implementation, with these attributes:
    | name - string e.g. micropython, from ``usys.implementation.name``
    | version - tuple (major, minor, micro), e.g. (1, 18, 0), from ``usys.implementation.version``

.. py:data::  maxsize

    | The maximum integer value that can be stored in a native integer, which is 2,147,483,647 for a 32-bit system.

.. py:data::  modules

    | A dictionary of loaded modules, not including builtin modules.
    | e.g. {'log': <module 'log'>, 'neopixel': <module 'neopixel'>}

.. py:data::  path

    | A list of directories to search for imported modules.
    | e.g. ['', '.frozen']

.. py:data::  byteorder

    | The byte order of the system ("little" or "big").
    | e.g. little

.. py:data::  argv

    | A list of arguments the current program was started with. e.g. []

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

