==========================
Music
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. py:module:: music

----

Random notes Task
----------------------------------------

| Design code to play random notes, using each feature of a note:
* note name
* octave
* length
| Make each part of the note a string.
| Build the full note specification by concatenating each part.
| note name + octave + ":" + length
| e.g. c4:2

| Create a list of notes, a list of octaves and a list of durations that are to be used.
| Create a defintion that takes as parameters the list of notes, the list of octaves and the list of durations, then randomly chooses one from each and joins them together and returns a full note.

| Play randomly generated notes.

.. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1
                
                .. code-block:: python

                from microbit import *
                import random
                import music

                notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
                octaves = [3, 4, 5]
                durations = [1, 2, 4, 8]

                def get_random_note(notes, octaves, durations):
                    note = random.choice(notes)
                    # convert numbers to strings so they ccan be joined
                    octave = str(random.choice(octaves))
                    duration = str(random.choice(durations))
                    full_note = note + octave + ":" + duration
                    return full_note

                while True:
                    random_note = get_random_note(notes, octaves, durations)
                    music.play(random_note)

----

.. admonition:: Tasks

    #. Include a note modification parameter to sharpen, flatten or leave the note unchanged.
    #. Create a function to return a random list of notes, given the number of notes, then play the list.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Include a note modification parameter to sharpen, flatten or leave the note unchanged.

                .. code-block:: python

                    from microbit import *
                    import random
                    import music


                    notes = ["c", "d", "e", "f", "g", "a", "b"]
                    modifiers = ["#", "b", ""]
                    octaves = [3, 4, 4, 4, 4, 5]
                    durations = [2, 3, 4, 2, 3, 4, 2, 3, 4, 8]


                    def get_random_note(notes, modifiers, octaves, durations):
                        note = random.choice(notes)
                        modifier = random.choice(modifiers)
                        octave = str(random.choice(octaves))
                        duration = str(random.choice(durations))
                        full_note = note + modifier + octave + ":" + duration
                        return full_note


                    while True:
                        random_note = get_random_note(notes, modifiers, octaves, durations)
                        music.play(random_note)


            .. tab-item:: Q2

                Create a function to return a random list of notes, given the number of notes, then play the list.

                .. code-block:: python

                    from microbit import *
                    import random
                    import music

                    notes = ["c", "d", "e", "f", "g", "a", "b"]
                    octaves = [3, 4, 4, 4, 4, 5]
                    durations = [2, 3, 4, 2, 3, 4, 2, 3, 4, 8]


                    def get_random_note(notes, octaves, durations):
                        note = random.choice(notes)
                        octave = str(random.choice(octaves))
                        duration = str(random.choice(durations))
                        full_note = note + octave + ":" + duration
                        return full_note


                    def get_random_notes(note_count):
                        tune = []
                        for i in range(note_count):
                            tune.append(get_random_note(notes, octaves, durations))
                        return tune


                    while True:
                        random_notes = get_random_notes(10)
                        music.play(random_notes)
                        sleep(2000)

