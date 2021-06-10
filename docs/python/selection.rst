==========================
Selection
==========================

Selection is one of the three basic control structures:

#. Sequence (steps in order)
#. Selection (branching using ``if`` ... ``elif`` ... ``else``)
#. Iteration (repetition or looping using ``while`` or ``for``)

Selection provides choice or branches in the code.

If, elif, else
----------------------------

| ``if`` is used with a condition that results in ``True`` or ``False``.
| When the condition is True, the code indented below the ``if`` statement is executed.
| Alternatives can be provided using ``elif`` with a condition.
| If all conditions are ``False``, ``else:`` can be used to execute other code.
| Note that there must be a colon, ``:``, at the end of each ``if``, ``elif`` and ``else`` statement.

.. code-block:: python

    from microbit import *
    
    scoreA = 88
    scoreB = 85
    while True:
        if scoreA > scoreB:
            display.scroll("A won")
        elif scoreB > scoreA:
            display.scroll("B won")
        else:
            display.scroll("A drew with B")

----

.. admonition:: Tasks

    #. Add the variables ``teamA`` and ``teamB`` and set team names for them. Modify the code to scroll the team name instead of 'A' or 'B'. Hint: To join text use a plus symbol. e.g (myteam + " my text")

----

Nested if 
----------------------------

| Nesting is the inclusion of other ``if`` statements have within ``if`` statements.
| Both the ``if`` and the ``elif`` have a nested ``if`` and ``else`` that are used when their condition is true. 

.. code-block:: python

    from microbit import *

    scoreA = 120
    scoreB = 55
    while True:
        if scoreA > scoreB:
            if scoreA - scoreB > 60:
                display.scroll("A won easily")
            else:
                display.scroll("A won")
        elif scoreB > scoreA:
            if scoreB - scoreA > 60:
                display.scroll("B won easily")
            else:
                display.scroll("B won")
        else:
            display.scroll("A drew with B")


----

.. admonition:: Tasks

    #. Add the variables ``teamA`` and ``teamB`` and set team names for them. Modify the code to scroll the team name instead of 'A' or 'B'. Hint: To join text use a plus symbol. e.g (myteam + " my text")
    #. Modify the code to scroll the winning margins. Use ``str(number)`` to convert numbers to text for joining with other text. Add the variables ``teamAwinby`` and ``teamBwinby``. Calculate those variables using the scoreA and scoreB. e.g ``teamAwinby = scoreA - scoreB``. Replace "A won easily" with code to output "A won easily by 65". Do similar replacements for the other scrolling text.

