==========================
errno
==========================

.. py:module:: errno

| The `errno` module in MicroPython provides access to symbolic error codes for `OSError` exceptions.
| These error codes are useful for handling specific error conditions in your code.

Error codes
---------------------

| The code below uses the REPL to print the dictionary of error codes.

.. code-block:: python

    from microbit import *
    import errno

    # print(help(errno))
    print(errno.errorcode)

::

  errorcode -- {1: 'EPERM', 2: 'ENOENT', 5: 'EIO',
  9: 'EBADF', 11: 'EAGAIN', 12: 'ENOMEM',
  13: 'EACCES', 17: 'EEXIST', 19: 'ENODEV',
  21: 'EISDIR', 22: 'EINVAL', 95: 'EOPNOTSUPP',
  98: 'EADDRINUSE', 103: 'ECONNABORTED',
  104: 'ECONNRESET', 105: 'ENOBUFS',
  107: 'ENOTCONN', 110: 'ETIMEDOUT',
  111: 'ECONNREFUSED', 113: 'EHOSTUNREACH',
  114: 'EALREADY', 115: 'EINPROGRESS'}

----

File open error
---------------------

| The code below uses the REPL to print the output.

.. code-block:: python

    # Imports go at the top
    from microbit import *
    import errno

    try:
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
    except OSError as e:
        if e.errno == errno.ENOENT:
            print("Error: File not found.")
        else:
            print("Error: {}".format(e))

----

Error code meanings
------------------------

| See: `<https://docs.python.org/3.12/library/errno.html>`_#module-errno
| Here are the meanings of each error code in the provided list:

1. **EPERM (1)**: Operation not permitted.
2. **ENOENT (2)**: No such file or directory.
3. **EIO (5)**: Input/output error.
4. **EBADF (9)**: Bad file descriptor.
5. **EAGAIN (11)**: Try again (resource temporarily unavailable).
6. **ENOMEM (12)**: Out of memory.
7. **EACCES (13)**: Permission denied.
8. **EEXIST (17)**: File exists.
9. **ENODEV (19)**: No such device.
10. **EISDIR (21)**: Is a directory.
11. **EINVAL (22)**: Invalid argument.
12. **EOPNOTSUPP (95)**: Operation not supported.
13. **EADDRINUSE (98)**: Address already in use.
14. **ECONNABORTED (103)**: Software caused connection abort.
15. **ECONNRESET (104)**: Connection reset by peer.
16. **ENOBUFS (105)**: No buffer space available.
17. **ENOTCONN (107)**: Transport endpoint is not connected.
18. **ETIMEDOUT (110)**: Connection timed out.
19. **ECONNREFUSED (111)**: Connection refused.
20. **EHOSTUNREACH (113)**: No route to host.
21. **EALREADY (114)**: Operation already in progress.
22. **EINPROGRESS (115)**: Operation now in progress.
