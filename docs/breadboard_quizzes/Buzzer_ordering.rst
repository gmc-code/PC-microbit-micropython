====================================================
Buzzer Music Code Ordering
====================================================

Question 1
-----------------

| Put the code snippets in order to play a single, clean quarter note on the microbit built-in speaker.

.. ordering::
    :theme: light

    from microbit import *
    import music

    while True:
        music.play("c4:4")
        sleep(250)

----

Question 2
------------------

| Arrange these lines sequentially to play a custom melody on the microbit built- in speaker.

.. ordering::
    :theme: light

    from microbit import *
    import music

    tune = ["c4:4", "e4:4", "g4:4"]
    while True:
        music.play(tune)
        sleep(500)

----

Question 3
--------------------

| Order the snippets below to create an interactive button-activated chord loop.

.. ordering::
    :theme: light

    from microbit import *
    import music

    chord = ["c4:4", "e4:4", "g4:4"]
    while True:
        if button_a.is_pressed():
            music.play(chord)

----

Question 4
----------------------

| Put the code snippets in order to safely set up a breadboard buzzer task.
| Remember the warning theory: you must turn off the internal built-in speaker first so it does not conflict with your external breadboard hardware component before playing a built-in melody.

.. ordering::
    :theme: light

    from microbit import *
    import music

    speaker.off()
    while True:
        music.play(music.RINGTONE)

----

Question 5
-------------------

| Arrange the blocks below to assemble an interactive musical instrument.
| The instrument should play a custom melody on the buzzer when Button A is pressed.
| The instrument should play a built-in melody on the microbit speaker when Button B is pressed.

.. ordering::
    :theme: light
    :no-padding:

    from microbit import *
    import music

    chord = ["c4:4", "e4:4", "g4:4"]
    while True:
        if button_a.is_pressed():
            speaker.off()
            music.play(chord)
        elif button_b.is_pressed():
            speaker.on()
            music.play(music.BADDY)

----

Question 6
-----------------

| Order the lines below to build an E Minor emergency manual exit sounds system.
| The system must sequentially iterate through the custom frequencies array but must break out of the playback loop if the user strikes Button A.

.. ordering::
    :theme: light
    :no-padding:

    from microbit import *
    import music

    speaker.off()
    Em_freqs = [659, 784, 988]
    while True:
        for freq in Em_freqs:
            music.pitch(freq, duration=400)
        if button_a.is_pressed():
            break

