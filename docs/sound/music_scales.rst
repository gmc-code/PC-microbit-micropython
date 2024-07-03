==========================
Music scales
==========================

Scales
----------------------------------------

| The lists below are the notes of scales.
| Press A or B to play a different scale.


.. code-block:: python

    from microbit import *
    import music

    c_major = ['c4', 'd', 'e', 'f', 'g', 'a', 'b', 'c5']
    a_minor = ['a4', 'b', 'c5', 'd', 'e', 'f', 'g', 'a']

    while True:
        if button_a.is_pressed():
            music.play(c_major)
        elif button_b.is_pressed():
            music.play(a_minor)
        sleep(1000)

----

.. admonition:: Tasks

    #. Play the 8 notes of G major. See: https://www.pianoscales.org/major.html
    #. Play the 8 notes of E minor. See: https://www.pianoscales.org/minor.html
    #. Play the G major scale when the A-button is pressed and the E minor scale when the B-button is pressed.
    #. Play the F major scale when the A-button is pressed and the D minor scale when the B-button is pressed.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the 8 notes of G major.

                .. code-block:: python

                    from microbit import *
                    import music

                    g_major = ["G4", "A", "B", "C5", "D", "E", "F#", "G"]

                    while True:
                        music.play(g_major)
                        sleep(1000)


            .. tab-item:: Q2

                Play the 8 notes of E minor.

                .. code-block:: python

                    from microbit import *
                    import music

                    e_minor = ["E4", "F#", "G", "A", "B", "C5", "D", "E"]

                    while True:
                        music.play(e_minor)
                        sleep(1000)


            .. tab-item:: Q3

                Play the G major scale when the A-button is pressed and the E minor scale when the B-button is pressed.

                .. code-block:: python

                    from microbit import *
                    import music

                    g_major = ["G4", "A", "B", "C5", "D", "E", "F#", "G"]
                    e_minor = ["E4", "F#", "G", "A", "B", "C5", "D", "E"]

                    while True:
                        if button_a.is_pressed():
                            music.play(g_major)
                        elif button_b.is_pressed():
                            music.play(e_minor)
                        sleep(1000)

           .. tab-item:: Q4

                Play the F major scale when the A-button is pressed and the D minor scale when the B-button is pressed.

                .. code-block:: python

                    from microbit import *
                    import music

                    g_major = ["F4", "G", "A", "Bb", "C5", "D", "E", "F"]
                    e_minor = ["D4", "E", "F", "G", "A", "Bb", "C5", "D"]

                    while True:
                        if button_a.is_pressed():
                            music.play(g_major)
                        elif button_b.is_pressed():
                            music.play(e_minor)
                        sleep(1000)

    #. Play the F major scale when the A-button is pressed and the D minor scale when the B-button is pressed.


----

Major Scales
----------------------------------------

| See: https://musictheory.pugetsound.edu/mt21c/MajorKeySignatures.html

| The code below plays the Major scales.
| Replacements for sharp major scales; B# = C; E# = F
| Replacements for flat major scales; Cb = B; Fb = E

.. code-block:: python

    from microbit import *
    import music


    # Octaves start on the note C.
    # major scales
    # sharp major scales; B# = C; E# = F
    C_major = {"name": "C", "notes": "C4 D E F G A B C5"}
    G_major = {"name": "G", "notes": "G4 A B C5 D E F# G"}
    D_major = {"name": "D", "notes": "D4 E F# G A B C#5 D"}
    A_major = {"name": "A", "notes": "A4 B C#5 D E F# G# A"}
    E_major = {"name": "E", "notes": "E4 F# G# A B C#5 D# E"}
    B_major = {"name": "B", "notes": "B4 C#5 D# E F# G# A# B"}
    F_sharp_major = {"name": "F#", "notes": "F# G# A# B C#5 D# F F#"}
    C_sharp_major = {"name": "C#", "notes": "C# D# F F# G# A# C5 C#"}

    # flat major scales; Cb = B; Fb = E
    F_major = {"name": "F", "notes": "F4 G A Bb C5 D E F"}
    B_flat_major = {"name": "Bb", "notes": "Bb4 C5 D Eb F G A Bb"}
    E_flat_major = {"name": "Eb", "notes": "Eb4 F G Ab Bb C5 D Eb"}
    A_flat_major = {"name": "Ab", "notes": "Ab4 Bb C5 Db Eb F G Ab"}
    D_flat_major = {"name": "Db", "notes": "Db4 Eb F Gb Ab Bb C5 Db"}
    G_flat_major = {"name": "Gb", "notes": "Gb4 Ab Bb B Db5 Eb F Gb"}
    C_flat_major = {"name": "Cb", "notes": "B3 Db4 Eb E Gb Ab Bb B"}

    circle_of_fifths_sharp_scales = [C_major, G_major, D_major, A_major, 
                                    E_major, B_major, F_sharp_major, C_sharp_major]

    circle_of_fifths_flat_scales = [C_major, F_major, B_flat_major, E_flat_major,
                                    A_flat_major, D_flat_major, G_flat_major, C_flat_major]


    music.set_tempo(ticks=8, bpm=240)
    # Loop over each with 1sec between
    for scale in circle_of_fifths_sharp_scales:
        name = scale["name"]
        notes = scale["notes"].split(" ")
        display.scroll(name, wait=False, delay=60)
        music.play(notes, wait=True)
        sleep(1000)
    # Loop over each with 1sec between
    for scale in circle_of_fifths_flat_scales:
        name = scale["name"]
        notes = scale["notes"].split(" ")
        display.scroll(name, wait=False, delay=60)
        music.play(notes, wait=True)
        sleep(1000)

----

Minor Scales
----------------------------------------

| See: https://musictheory.pugetsound.edu/mt21c/MinorKeySignatures.html

| The code below plays the minor scales.
| Replacements for sharp minor scales; B# = C; E# = F
| Replacements for flat minor scales; Cb = B; Fb = E

.. code-block:: python

    from microbit import *
    import music

    # Octaves start on the note C.
    # sharp Minor scales; B# = C; E# = F
    A_minor = {"name": "Am", "notes": "A4 B C5 D E F G A"}
    E_minor = {"name": "Em", "notes": "E4 F# G A B C5 D E"}
    B_minor = {"name": "Bm", "notes": "B4 C#5 D E F# G A B"}
    F_sharp_minor = {"name": "F#m", "notes": "F# G# A B C#5 D E F#"}
    C_sharp_minor = {"name": "C#m", "notes": "C# D# E F# G# A B C#5"}
    G_sharp_minor = {"name": "G#m", "notes": "G# A# B C#5 D# E F# G#"}
    D_sharp_minor = {"name": "D#m", "notes": "D# F F# G# A# B C#5 D#"}
    A_sharp_minor = {"name": "A#m", "notes": "A# C5 D D# F G G# A#"}
    # flat Minor scales; Cb = B; Fb = E
    A_minor = {"name": "Am", "notes": "A4 B C5 D E F G A"}
    D_minor = {"name": "Dm", "notes": "D4 E F G A Bb C5 D"}
    G_minor = {"name": "Gm", "notes": "G4 A Bb C5 D Eb F G"}
    C_minor = {"name": "Cm", "notes": "C4 D Eb F G Ab Bb C5"}
    F_minor = {"name": "Fm", "notes": "F4 G Ab Bb C5 Db Eb F"}
    B_flat_minor = {"name": "Bbm", "notes": "Bb C5 Db Eb F Gb Ab Bb"}
    E_flat_minor = {"name": "Ebm", "notes": "Eb F Gb Ab Bb B Db5 Eb"}
    A_flat_minor = {"name": "Abm", "notes": "Ab Bb B Db5 Eb E Gb Ab"}

    circle_of_fifths_sharp_minor_scales = [A_minor, E_minor, B_minor, F_sharp_minor,
                                        C_sharp_minor, G_sharp_minor, D_sharp_minor, A_sharp_minor]

    circle_of_fifths_flat_minor_scales = [A_minor, D_minor, G_minor, C_minor,
                                        F_minor, B_flat_minor, E_flat_minor, A_flat_minor]

    music.set_tempo(ticks=8, bpm=240)
    # Loop over each with 1sec between
    for scale in circle_of_fifths_sharp_minor_scales:
        name = scale["name"]
        notes = scale["notes"].split(" ")
        display.scroll(name, wait=False, delay=60)
        music.play(notes, wait=True)
        sleep(1000)
    # Loop over each with 1sec between
    for scale in circle_of_fifths_flat_minor_scales:
        name = scale["name"]
        notes = scale["notes"].split(" ")
        display.scroll(name, wait=False, delay=60)
        music.play(notes, wait=True)
        sleep(1000)

----

Triads
--------------

| The code below has a list of notes in the 7 triads in the key of C major.
| The tempo is set to play the notes quickly: ticks=8, bpm=240.
| Each of the three notes in a triad are played, with a short sleep to the next triad.

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=8, bpm=240)
    triads = [["C4", "E4", "G4"], ["D4", "F4", "A4"], ["E4", "G4", "B4"], 
            ["F4", "A4", "C5"], ["G4", "B4", "D5"], ["A4", "C5", "E5"], ["B4", "D5", "F5"]]

    while True:
            for triad in triads:
                music.play(triad, wait=True)
                sleep(100)
            sleep(500)

----

.. admonition:: Tasks

    #. Modify the code to only play the triads if the A button has been pressed.
    #. Modify the code to play each triad with their notes in reverse order using triad[::-1].
    #. Modify the code to play the triads if the A button has been pressed and to play them with their notes in reverse order if the B button has been pressed.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to only play the triads if the A button has been pressed.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=8, bpm=240)
                    triads = [["C4", "E4", "G4"], ["D4", "F4", "A4"], ["E4", "G4", "B4"], 
                            ["F4", "A4", "C5"], ["G4", "B4", "D5"], ["A4", "C5", "E5"], ["B4", "D5", "F5"]]

                    while True:
                        if button_a.was_pressed():
                            for triad in triads:
                                music.play(triad, wait=True)
                                sleep(100)
                            sleep(500)


            .. tab-item:: Q2

                Modify the code to play each triad with their notes in reverse order using triad[::-1].

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=8, bpm=240)
                    triads = [["C4", "E4", "G4"], ["D4", "F4", "A4"], ["E4", "G4", "B4"], 
                            ["F4", "A4", "C5"], ["G4", "B4", "D5"], ["A4", "C5", "E5"], ["B4", "D5", "F5"]]

                    while True:
                        for triad in triads:
                            music.play(triad[::-1], wait=True)
                            sleep(100)
                        sleep(500)

            .. tab-item:: Q2

                Modify the code to play the triads if the A button has been pressed and to play them with their notes in reverse order if the B button has been pressed.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=8, bpm=240)
                    triads = [["C4", "E4", "G4"], ["D4", "F4", "A4"], ["E4", "G4", "B4"], 
                            ["F4", "A4", "C5"], ["G4", "B4", "D5"], ["A4", "C5", "E5"], ["B4", "D5", "F5"]]

                    while True:
                        if button_a.was_pressed():
                            for triad in triads:
                                music.play(triad, wait=True)
                                sleep(100)
                            sleep(500)
                        elif button_b.was_pressed():
                            for triad in triads:
                                music.play(triad[::-1], wait=True)
                                sleep(100)
                            sleep(500)


