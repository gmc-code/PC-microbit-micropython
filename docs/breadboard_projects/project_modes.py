"""
Vehicle Systems Demonstrator

A micro:bit-based embedded system that demonstrates three vehicle subsystems:
air conditioning, audio, and headlights.

The program provides a menu-driven interface that allows the user to select
a subsystem using Button A and demonstrate it using Button B. Each subsystem is
demonstrated using three predefined output levels to simulate different
operating settings.

Inputs:
    Button A - Change selected subsystem.
    Button B - Run subsystem demonstration.

Outputs:
    pin0 - Motor/fan output.
    pin1 - Audio output.
    pin2 - LED output.

The LED display is used to show menu selections, operating levels, and
system status messages.
"""

from microbit import *
import music

# turn off in built speaker so that the in-built speaker does not also play sounds.
speaker.off()

# Initialise variables
SCROLL_SPEED = 70
MOTORPIN = pin0
AUDIOPIN = pin1
LEDPIN = pin2
DEMO_TIME = 4000
DEMO_GAP_TIME = 1000
DISPLAY_INTERVAL = 2000

last_display_time = running_time()
current_module_selected = 1
previous_module_selected = None



# Loading animation to show when switching from screen to screen.
def load_animation():
    clocks = [Image.CLOCK12, Image.CLOCK3, Image.CLOCK6, Image.CLOCK9, Image.CLOCK12]
    display.show(clocks, delay=120)
    display.clear()
    sleep(250)


# For the display, only repeat text every so often.
def show_current_option():
    global previous_module_selected, last_display_time

    # Display immediately if the module changed, OR if DISPLAY_INTERVAL seconds have passed
    if (previous_module_selected != current_module_selected
            or running_time() - last_display_time > DISPLAY_INTERVAL):

        display_current_option()
        last_display_time = running_time()  # Reset the timer

    previous_module_selected = current_module_selected
    sleep(200)


def display_current_option():
    global current_module_name

    if current_module_selected == 1:
        current_module_name = 'AC'
    elif current_module_selected == 2:
        current_module_name = 'Audio'
    elif current_module_selected == 3:
        current_module_name = 'Lights'

    display.scroll(current_module_name, SCROLL_SPEED)



# Air conditioner module (fan)
def demo_ac():
    display.scroll('Demo...', SCROLL_SPEED)

    for fan_speed in range(1, 4):
        display.show(fan_speed)

        if fan_speed == 1:
            MOTORPIN.write_analog(250)
        elif fan_speed == 2:
            MOTORPIN.write_analog(500)
        elif fan_speed == 3:
            MOTORPIN.write_analog(1023)

        sleep(DEMO_TIME)
        MOTORPIN.write_analog(0)
        sleep(DEMO_GAP_TIME)

    display.clear()


# audio module (buzzer)
def demo_audio():
    display.scroll('Demo...', SCROLL_SPEED)

    for audio_preset in range(1, 4):
        display.show(audio_preset)

        if audio_preset == 1:
            set_volume(155)
            music.set_tempo(bpm=120)
            music.play(music.ENTERTAINER, wait=False, pin=AUDIOPIN)

        elif audio_preset == 2:
            set_volume(200)
            music.set_tempo(bpm=80)
            music.play(music.BLUES, wait=False, pin=AUDIOPIN)

        elif audio_preset == 3:
            set_volume(255)
            music.set_tempo(bpm=150)
            music.play(music.NYAN, wait=False, pin=AUDIOPIN)

        sleep(DEMO_TIME)
        music.stop()
        sleep(DEMO_GAP_TIME)

    display.clear()


# Headlights module (LED)
def demo_headlights():
    display.scroll('Demo...', SCROLL_SPEED)

    for brightness_level in range(1, 4):
        display.show(brightness_level)

        if brightness_level == 1:
            LEDPIN.write_analog(100)
        elif brightness_level == 2:
            LEDPIN.write_analog(500)
        elif brightness_level == 3:
            LEDPIN.write_analog(1023)

        sleep(DEMO_TIME)
        LEDPIN.write_analog(0)
        sleep(DEMO_GAP_TIME)

    display.clear()


###################################################################

# Says welcome and "loads" the head unit
display.scroll('WELCOME!', SCROLL_SPEED)
load_animation()
display.scroll('mode A -> Demo B', SCROLL_SPEED)
load_animation()

# A to choose mode, B to Demo it.
while True:
    show_current_option()

    if button_a.was_pressed():
        current_module_selected += 1

        if current_module_selected > 3:
            current_module_selected = 1

    if button_b.was_pressed():
        load_animation()

        if current_module_selected == 1:
            demo_ac()
        elif current_module_selected == 2:
            demo_audio()
        elif current_module_selected == 3:
            demo_headlights()

        load_animation()
        previous_module_selected = None

    sleep(50)
