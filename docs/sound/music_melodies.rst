==========================
Music built in melodies
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. py:module:: music

Built in music
----------------------------------------

| There are built-in melodies that can be found by typing ``music.``
| Melodies can be played using ``music.play(melody)`` where the melody is music. and a melody name in capitals.

.. code-block:: python

    from microbit import *
    import music

    music.play(music.POWER_UP)

| The code below uses a for-loop to loop through each melody in a given ``melodies_list`` and play it.


.. code-block:: python

    from microbit import *
    import music

    melodies_list = [music.DADADADUM, music.POWER_DOWN]
    for melody in melodies_list:
        music.play(melody)

----

All Built in melodies
----------------------------------------

| For a list of built-in melodies see: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html
| The code below plays all the melodies.
| the A-button can be used to stop all sounds by first breaking out of the ``for`` loop, then the ``while True`` loop.

.. code-block:: python

    from microbit import *
    import music

    built_in_tunes = [music.DADADADUM, music.ENTERTAINER, music.PRELUDE,
                      music.ODE, music.NYAN, music.RINGTONE, music.FUNK, music.BLUES,
                      music.BIRTHDAY, music.WEDDING, music.FUNERAL, music.PUNCHLINE,
                      music.PYTHON, music.BADDY, music.CHASE, music.BA_DING,
                      music.WAWAWAWAA, music.JUMP_UP, music.JUMP_DOWN, music.POWER_UP,
                      music.POWER_DOWN]

    while True:
        for tune in built_in_tunes:
            music.play(tune)
            sleep(1000)
            if button_a.is_pressed():
                break
        if button_a.is_pressed():
            break
----

.. admonition:: Tasks

    #. Play any 3 melodies using a list.
    #. Use the choice function to randomly pick melodies from a melody list. See: https://www.w3schools.com/python/ref_random_choice.asp

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play any 3 melodies using a list.

                .. code-block:: python

                    from microbit import *
                    import music

                    melodies_list = [music.POWER_UP, music.DADADADUM, music.POWER_DOWN]
                    for melody in melodies_list:
                        music.play(melody)

            .. tab-item:: Q2

                Use the choice function to randomly pick melodies from a melody list. See: https://www.w3schools.com/python/ref_random_choice.asp

                .. code-block:: python

                    from microbit import *
                    import random
                    import music

                    melodies_list = [music.POWER_UP, music.DADADADUM, music.POWER_DOWN]

                    while True:
                        music.play(random.choice(melodies_list))
                        sleep(1000)

