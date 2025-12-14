==========================
Modules extra
==========================

----------------
usys
----------------

| See: `<https://docs.micropython.org/en/latest/library/sys.html>`_
| Some functions are listed below. Use ``print(help(usys))`` to get the full list.

.. py:function::  usys.version_info()

    Python language version, as a tuple of ints.

.. py:function::  usys.version()

    Python language version, as a string.

.. py:function::  usys.platform()

    The platform that MicroPython is running on.

.. py:function::  usys.implementation()

    Object with information about the current MicroPython implementation with following attributes:

    name - string "micropython"

    version - tuple (major, minor, micro), e.g. (1, 15, 0)

.. py:function::  usys.maxsize()

    The maximum integer type value that can be saved on the current platform. It returns the number of bytes of heap RAM that are allocated.

| The code below uses the REPL to print the output.

.. code-block:: python

    from microbit import *
    import usys

    # print(help(usys))
    print('version_info', usys.version_info)
    print('version', usys.version)
    print('platform', usys.platform)
    print('implementation', usys.implementation)
    print('maxsize', usys.maxsize)
    if usys.maxsize > 2147483648:
        print('64-bit')
    else:
        print('32-bit')

----

----------------
ustruct
----------------

| See: `<https://mpython.readthedocs.io/en/master/library/pythonStd/ustruct.html>`_
| See: `<https://www.educative.io/answers/what-is-the-python-struct-module
| See: `<https://docs.micropython.org/en/latest/library/struct.html>`_

| The struct module in Python is used to convert native Python data types such as strings and numbers into a string of bytes and vice versa.

Supported size/byte order prefixes: @, <, >, !.

Supported format codes: b, B, h, H, i, I, l, L, q, Q, s, P, f, d (the latter 2 depending on the floating-point support).

Functions:
  * calcsize
  * pack
  * pack_into
  * unpack
  * unpack_from

----

----------------
uerrno
----------------

| The ``uerrno`` module returns errors.
| See: `<https://mpython.readthedocs.io/en/master/library/pythonStd/uerrno.html>`_

.. py:function::  uerrno.errorcode

    Returns the error codes dictionary object.

.. code-block:: python

    from microbit import *
    import uerrno

    print(help(uerrno))
    error_codes = uerrno.errorcode
    print(error_codes)
    print(uerrno.errorcode[uerrno.EINVAL])
    print(uerrno.errorcode[22])

errorcodes:
{1: 'EPERM', 2: 'ENOENT', 5: 'EIO', 9: 'EBADF', 11: 'EAGAIN', 12: 'ENOMEM', 13: 'EACCES', 17: 'EEXIST', 19: 'ENODEV', 21: 'EISDIR', 22: 'EINVAL', 95: 'EOPNOTSUPP', 98: 'EADDRINUSE', 103: 'ECONNABORTED', 104: 'ECONNRESET', 105: 'ENOBUFS', 107: 'ENOTCONN', 110: 'ETIMEDOUT', 111: 'ECONNREFUSED', 113: 'EHOSTUNREACH', 114: 'EALREADY', 115: 'EINPROGRESS'}


