====================================================
EXT: First Use **V2**
====================================================

Firmware
------------

| Some Microbits can have their firmware updated depending on the microbit version.
| See: https://microbit.org/get-started/user-guide/firmware/
| See: https://tech.microbit.org/software/daplink-interface/#daplink-software

----

Out of Box hex file v2
--------------------------

| The hex file that is on new microbits can be found at: https://microbit.org/get-started/user-guide/out-of-box-experience/
| The code below is similar to the out-of-box-experience that occurs when a new microbit is first started.

.. code-block:: python

    from microbit import *
    import music
    import audio

    def on_button_pressed_a():
        audio.play(Sound.SPRING, wait=False)
        display.show(Image.HAPPY)

    def on_button_pressed_b():
        audio.play(Sound.SAD, wait=False)
        display.show(Image.SAD)

    def on_button_pressed_ab():
        if display.read_light_level() > 50:
            music.play(music.POWER_UP, wait=False)
            display.show(Image("90909:09990:99999:09990:90909"))
        else:
            music.play(music.POWER_DOWN, wait=False)
            display.show(Image("00990:00099:00099:00099:00990"))

    def on_logo_touched():
        while pin_logo.is_touched():
            display.show(Image("99999:"*int(microphone.sound_level()/51)))
            # Display a bar graph with a height proportional to the sound level; 255 is max level
            sleep(5)
        display.clear()

    def on_gesture_screen_down():
        # https://microbit-micropython.readthedocs.io/en/stable/audio.html#built-in-sounds-v2
        display.show(Image.ASLEEP)
        sound_effect = audio.SoundEffect(freq_start=5849, freq_end=1, vol_start=255, vol_end=0, duration=1000,
                    waveform=audio.SoundEffect.WAVEFORM_SINE,shape=audio.SoundEffect.SHAPE_LINEAR)
        audio.play(sound_effect, wait=False)

    def on_gesture_shake():
        display.show(Image("09090:00000:00000:99999:00000"))
        sound_effect = audio.SoundEffect(freq_start=3041, freq_end=3923, duration=500, vol_start=59, vol_end=255, waveform=audio.SoundEffect.WAVEFORM_SINE, fx=audio.SoundEffect.FX_WARBLE, shape=audio.SoundEffect.SHAPE_LINEAR)
        audio.play(sound_effect, wait=False)
        sleep(1000)  # Delay for 1000 milliseconds (1 second)
        display.show(Image("09090:00000:09990:90009:09990"))
        sleep(1000)  # Delay for 1000 milliseconds (1 second)
        display.show(Image("09090:00000:00000:99999:00000"))

    audio.play(Sound.HELLO, wait=False)
    display.show(Image.HEART)

    while True:
        if accelerometer.was_gesture("face down"):
            on_gesture_screen_down()
        elif accelerometer.is_gesture("shake"):
            on_gesture_shake()
        if pin_logo.is_touched():
            on_logo_touched()
        elif button_a.is_pressed() and button_b.is_pressed():
            on_button_pressed_ab()
        elif button_a.is_pressed():
            on_button_pressed_a()
        elif button_b.is_pressed():
            on_button_pressed_b()
        else:
            display.show("")
        sleep(500)


