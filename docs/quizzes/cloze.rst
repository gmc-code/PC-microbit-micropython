================================================
Cloze Directive Documentation
================================================

The cloze directive creates an interactive drag-and-drop fill-in-the-blanks puzzle.
Users can drag keywords from a randomized word bank tray and drop them into target drop zones nested inline inside code snippets or descriptive text.

Syntax
-------------------

.. code-block:: rst

    .. cloze::

        Code text containing *[ target_keyword ]* markup blocks.

Options for the cloze directive
--------------------------------------

.. list-table::
   :widths: 35 20 40
   :header-rows: 1

   * - Option
     - Type
     - Description
   * - ``:auto-distract:``
     - flag
     - | If present, dynamically harvests distractors from
       | the surrounding text or alternate gap parameters.
   * - ``:theme:``
     - string
     - | Sets the visual styling theme for the block layout.
       | Acceptable values are ``light`` (default) or ``dark``.


| Indentation: When working with formatted blocks, ensure standard white space indentation remains aligned.
| Single Items: An implicit markup pattern like ``*[ yield ]*`` designates a target drop field.
| Multiple Choice: You can explicitly supply choices by separating alternatives with slashes: ``*[ choices / alternatives ]*``.
| Distractor Harvesting: Applying the ``:auto-distract:`` flag commands the backend to look ahead, read the code context, and feed vocabulary selections automatically as distractors.
| Structure: The directive creates a word bank container layer holding randomized draggable buttons and embeds corresponding drop target fields within the code passage layout.

----

Example 1: Basic Alternative Choices
-------------------------------------------

The following example explicitly supplies alternative keyword targets separated by slashes.

.. code-block:: rst

    .. cloze::

        When creating a function in Python, you define it using the *[ def / function ]* keyword.


.. cloze::

    When creating a function in Python, you define it using the *[ def / function ]* keyword.


----

Example 2: Dark theme
-------------------------------------------

| The following example demonstrates the cloze directive with the dark theme.
| `:theme: dark` is optional since it is not the default.

.. code-block:: rst

    .. cloze::
        :theme: dark

        To send a result back to the caller, you use *[ return / print ]*.

.. cloze::
    :theme: dark

    To send a result back to the caller, you use *[ return / print ]*.


----

Example 3: Auto-Distract Flag Implementation
---------------------------------------------

| The following example relies on the ``:auto-distract:`` flag option.
| The word bank will automatically pull vocabulary terms out of the block to act as distractors.

.. code-block:: rst

    .. cloze::
        :auto-distract:

        An *[ array ]* is a sequential structure that stores data elements.
        You can look up specific data instances via an integer *[ index ]*.

.. cloze::
    :auto-distract:

    An *[ array ]* is a sequential structure that stores data elements.
    You can look up specific data instances via an integer *[ index ]*.

----

Example 4: Indentation is retained in code blocks
---------------------------------------------------

| Demonstrating retention of indentation and formatting within a code block, while still allowing for interactive selection of choices from a dropdown menu.

.. code-block:: rst

    .. cloze::

        for number *[ in/of ]* range(1, 10):
            if number % 2 == 0:
                *[ continue / break / pass ]*
            print(number)

.. cloze::

    for number *[ in/of ]* range(1, 10):
        if number % 2 == 0:
            *[ continue / break / pass ]*
        print(number)

