====================================================
Buzzer Music Code Ordering
====================================================

Question 1
-----------------

| Put the code lines in order to play a single note on the microbit built-in speaker follow by a brief pause before repeating the note.

.. ordering::
    :theme: light

    from microbit import *
    import music

    note = "c"
    while True:
        music.play(note)
        sleep(100)

----

Question 2
------------------

| Arrange these lines sequentially to play a short note list on the microbit built-in speaker follow by a brief pause before repeating the note list.

.. ordering::
    :theme: light

    from microbit import *
    import music

    tune = ["c", "e", "g"]
    while True:
        music.play(tune)
        sleep(100)

----

Question 3
--------------------

| Order lines below to play a short tune on the microbit built-in speaker while Button A is pressed. The tune should be played once and then the program should pause for a short delay before checking the button state again.

.. ordering::
    :theme: light

    from microbit import *
    import music

    tune = ["c4:1","c4:1","d4:2","c4:2","f4:2","e4:4"]
    while True:
        if button_a.is_pressed():
            music.play(tune)
        sleep(100)

----

Question 4
----------------------

| Put the code snippets in order to play a built-in melody on the breadboard buzzer when Button A is pressed. The melody should be played once and then the program should pause for a short delay before checking the button state again.

.. ordering::
    :theme: light

    from microbit import *
    import music

    speaker.off()
    while True:
        if button_a.is_pressed():
            music.play(music.RINGTONE)
        sleep(100)

----

Question 5
-------------------

| Arrange the blocks below to assemble an interactive musical instrument.
| The instrument should play a custom tune on the buzzer when Button A is pressed.
| The instrument should play a built-in melody on the microbit speaker when Button B is pressed.

.. ordering::
    :theme: light
    :no-padding:

    from microbit import *
    import music

    tune = ["c4:1","c4:1","d4:2","c4:2","f4:2","e4:4"]
    while True:
        if button_a.is_pressed():
            speaker.off()
            music.play(tune)
        elif button_b.is_pressed():
            speaker.on()
            music.play(music.BADDY)
        sleep(100)

