==========================
Music Rhythms
==========================

Rhythm: Shave and a hair cut: two bits
-----------------------------------------

| See: `<https://en.wikipedia.org/wiki/Shave_and_a_Haircut
| The rhythm below is given by saying aloud: "Shave and a hair cut: two bits".
| Play this rhythm.

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=120)
    rhythm = ["C4:4", "C4:2", "C4:2", "C4:4", "C4:4", "R:4", "C4:4", "C4:4", "R:4"]


    while True:
        music.play(rhythm)

----

.. admonition:: Tasks

    .. image:: images/shave_and_a_haircut.png
        :scale: 100 %

    #. Modify the notes to match the image notes in the key of G.
    #. Modify the notes to match the image notes, but in the key of C.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the notes to match the image notes in the key of G.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=120)
                    rhythm = ["G4:4", "D4:2", "D4:2", "E4:4", "D4:4", "R:4", "F#4:4", "G4:4", "R:4"]

                    while True:
                        music.play(rhythm)

            .. tab-item:: Q2

                Modify the notes to match the image notes, but in the key of C.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=120)
                    rhythm = ["C5:4", "G4:2", "G4:2", "A4:4", "G4:4", "R:4", "B4:4", "C5:4", "R:4"]

                    while True:
                        music.play(rhythm)


----

Rhythm: Famous movie series 1
--------------------------------

| Play this rhythm.
| Can you identify the movie theme?

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=90)
    rhythm = ["C4:3", "C4:1", "R:2", "C4:2", "C4:2", "C4:2", "R:1", "C4:1", "R:2", "C4:2", "C4:2"]

    while True:
        music.play(rhythm)


----

.. admonition:: Tasks

    #. Replace the notes with: G, G, Bb, C5, G, G, F, F#.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the notes with: G, G, Bb, C5, G, G, F, F#.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=90)
                    rhythm = ["G4:3", "G4:1", "R:2", "Bb4:2", "C5:2", "G4:2", "R:1", "G4:1", "R:2", "F4:2", "F#4:2"]

                    while True:
                        music.play(rhythm)


----

Rhythm: Famous movie series 2
--------------------------------

| Play this rhythm.
| Can you identify the movie theme?

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=116)
    rhythm = ["R2", "C5:1", "C5:1", "C5:2", "C5:2", "C5:2", "C5:2", "R:4",
                "R:4", "C5:2", "C5:1", "C5:1", "C5:2", "C5:2", "R:4"]

    while True:
        music.play(rhythm)


----

.. admonition:: Tasks

    #. Replace the notes with: C, C, E, C, D, Bb, C, C, C, Bb, C.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the notes with: C, C, E, C, D, Bb, C, C, C, Bb, C.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=90)
                    rhythm = ["R2", "C5:1", "C5:1", "E5:2", "C5:2", "D5:2", "Bb4:2", "R:4", "R:4", "C5:2", "C5:1", "C5:1", "Bb4:2", "C5:2", "R:4"]

                    while True:
                        music.play(rhythm)






