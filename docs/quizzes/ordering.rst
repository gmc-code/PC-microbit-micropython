

================================================
Ordering Directive Documentation
================================================

The ordering directive creates an interactive code-reordering exercise. Users can drag and drop code lines into their correct sequence and adjust indentation levels.

Syntax
-------------------

.. code-block:: rst

    .. ordering::

        code lines to be arranged in the correct order

options for the ordering directive
--------------------------------------

+------------------+--------+-----------------------------------------------------------+
| Option           | Type   | Description                                               |
+==================+========+===========================================================+
| ``:theme:``      | string | Set the visual theme. Options are ``light`` (default)     |
|                  |        | or ``dark``.                                              |
+------------------+--------+-----------------------------------------------------------+
| ``:no-solution:``| flag   | If present, hides the "Show Solution" button from the     |
|                  |        | user.                                                     |
+------------------+--------+-----------------------------------------------------------+

| Indentation: The directive automatically calculates the indentation level based on groups of 4 spaces. Ensure your input text uses consistent 4-space indentation for nested code blocks.
| Shuffling: Items are automatically shuffled on page render and on Reset button click to eliminate pattern memorization giveaways.
| Visual Badges: When validated, inline symbols provide quick feedback right alongside choices.
| Empty Lines: You may include empty lines within the block; the directive will render them as placeholders that users can drag to maintain formatting structure.
| Structure: The directive creates an interactive <div> block with handle controls (☰) for reordering and buttons («, ») for adjusting indentation.



----

Example 1: light theme
------------------------------------

| The default theme is light. The following example demonstrates the ordering directive with the light theme. `:theme: light` is optional since it is the default.

.. code-block:: rst

    .. ordering::
        :theme: light

        def hello_world():
            print("Hello World")

.. ordering::
    :theme: light

    def hello_world():
        print("Hello World")

----

Example 2: dark theme
------------------------------------


.. code-block:: rst

    .. ordering::
        :theme: dark

        def hello_world():
            print("Hello World")

.. ordering::
    :theme: dark

    def hello_world():
        print("Hello World")


----

Example 3: no solution button
-------------------------------

| The following example demonstrates the ordering directive with the "Show Solution" button hidden.
| `:no-solution:` is used to hide the solution button.

.. code-block:: rst

    .. ordering::
        :no-solution:

        def add(num1, num2):
            return num1 + num2

        print(add(5, 3))


.. ordering::
    :no-solution:

    def add(num1, num2):
        return num1 + num2

    print(add(5, 3))

----

Example 4: multiple indent levels
-------------------------------------

| The following example demonstrates the ordering directive with multiple indentation levels. The directive automatically calculates the indentation level based on groups of 4 spaces.

.. code-block:: rst

    .. ordering::

        def find_max(numbers):
            max_val = numbers[0]
            for num in numbers:
                if num > max_val:
                    max_val = num
            return max_val

Reorder the following code snippets to create a function that finds the maximum value in a list of numbers.

.. ordering::

    def find_max(numbers):
        max_val = numbers[0]
        for num in numbers:
            if num > max_val:
                max_val = num
        return max_val

----

Example 5: blanks lines
-------------------------------------

| The following example demonstrates the ordering directive with blank lines included. The directive will render them as placeholders that users can drag to maintain formatting structure.

.. code-block:: rst

    .. ordering::

        def rect_perimeter(width, height):
            return 2 * (width + height)

        def rect_area(width, height):
            area = width * height
            return area

        print(f'Perimeter: {rect_perimeter(5, 3)}')
        print(f'Area: {rect_area(5, 3)}')


| Write functions that returns the total perimeter and area of a rectangle in that order.
| Print the perimeter and area of a rectangle with width 5 and height 3.

.. ordering::

    def rect_perimeter(width, height):
        return 2 * (width + height)

    def rect_area(width, height):
        area = width * height
        return area

    print(f'Perimeter: {rect_perimeter(5, 3)}')
    print(f'Area: {rect_area(5, 3)}')



