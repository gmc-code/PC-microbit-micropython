====================================================
Gestures
====================================================

| The accelerometer returns the following gestures moving the microbit: ``up``, ``down``, ``left``, ``right``, ``face up``, ``face down``, ``freefall``, ``3g``, ``6g``,
``8g``, ``shake``. 
| Gestures are always represented as strings. 
| ``3g``, ``6g`` and ``8g`` gestures apply when the micorbit experiences large levels of g-force.

Current gesture
-------------------------

.. py:function:: current_gesture()

    Return the name of the current gesture as a string. The gestures are: ``"up"``, ``"down"``, ``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``, ``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``.


| The code below displays teh current gesture.

.. code-block:: python

    from microbit import *


    while True:
        gesture = accelerometer.current_gesture()
        display.scroll(gesture)
        sleep(500)


| The code below displays a happy image if the microbit is face up, or an angry image if it is not.

.. code-block:: python

    from microbit import *


    while True:
        gesture = accelerometer.current_gesture()
        if gesture == "face up":
            display.show(Image.HAPPY)
        else:
            display.show(Image.ANGRY)

----

.. admonition:: Tasks

    #. What are the readings for 1 o'clock?
    #. What are the readings for 3 o'clock?
    #. What are the readings for 6 o'clock?

----

Magic-8
-------------

A Magic-8 ball is a toy first invented in the 1950s. The idea is to ask
it a yes/no question, shake it and wait for it to reveal the truth. It's rather
easy to turn into a program::

    from microbit import *
    import random

    answers = [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes, definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ]

    while True:
        display.show("8")
        if accelerometer.was_gesture("shake"):
            display.clear()
            sleep(1000)
            display.scroll(random.choice(answers))

Most of the program is a list called ``answers``. The actual game is in the
``while`` loop at the end.

The default state of the game is to show the character ``"8"``. However, the
program needs to detect if it has been shaken. The ``was_gesture`` method uses
its argument (in this case, the string ``"shake"`` because we want to detect
a shake) to return a ``True`` / ``False`` response. If the device was shaken
the ``if`` conditional drops into its block of code where it clears the screen,
waits for a second (so the device appears to be thinking about your question)
and displays a randomly chosen answer.

Why not ask it if this is the greatest program ever written? What could you do
to "cheat" and make the answer always positive or negative? (Hint: use the
buttons.)
