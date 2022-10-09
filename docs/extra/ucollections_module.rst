==========================
ucollections
==========================

.. py:module:: ucollections

| MicroPython contains an ``ucollections`` module based upon the ``collections`` module in the Python standard library.
| This module has 2 collections from the standard python collections module.
| See: http://docs.micropython.org/en/v1.14/library/ucollections.html#module-ucollections
| See: https://mpython.readthedocs.io/en/master/library/pythonStd/ucollections.html



| namedtuple is a function
| OrderedDict is a class

----

ucollections.namedtuple
--------------------------

.. function:: ucollections.namedtuple(name, fields)

    Create a new namedtuple type with a specific name and set of fields. A namedtuple is a subclass of tuple which allows access to its fields not just by numeric index, but also with an attribute access syntax using field names. Fields is a sequence of strings specifying field names. It can also be a a string with space-separated field named (but this is less efficient).


.. code-block:: python

    from microbit import *
    from ucollections import namedtuple as nt

    Point = nt('Point', ['x', 'y'])
    p = Point(3, y=4)     # instantiate with positional or keyword arguments

    print(p[0], p[1])            # indexable like the plain tuple (11, 22)

    x, y = p                # unpack like a regular tuple
    print(x, y)

    print(p.x, p.y)           # fields also accessible by name

    print(p)                       # readable __repr__ with a name=value style


----

ucollections.OrderedDict
--------------------------

| See: http://docs.micropython.org/en/v1.14/library/ucollections.html#module-ucollections

.. function:: ucollections.OrderedDict(name, fields)

    Create a dictionary type subclass which remembers and preserves the order of keys added. When ordered dict is iterated over, keys/items are returned in the order they were added.

Functions:
  clear
  copy
  get
  items
  keys
  pop
  popitem
  setdefault
  update
  values

Methods:
  fromkeys
  
.. code-block:: python

    from microbit import *
    from ucollections import OrderedDict as Od

    # To make benefit of ordered keys, OrderedDict should be initialized
    # from sequence of (key, value) pairs.
    d = Od([("x", 1), ("y", 2)])
    # More items can be added as usual
    d["a"] = 3
    d["b"] = 4
    # print keys and values.
    for k, v in d.items():
        print(k, v)

