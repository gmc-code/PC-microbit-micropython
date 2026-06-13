from microbit import *
import music

# ------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------

SCROLL_SPEED = 70
MENU_SCROLL_SPEED = 75

LOADING_FRAMES = (Image.CLOCK12, Image.CLOCK2, Image.CLOCK4, Image.CLOCK6, Image.CLOCK8, Image.CLOCK10, Image.CLOCK12)

# ------------------------------------------------------------------
# Utility Functions
# ------------------------------------------------------------------

def load():
    for frame in LOADING_FRAMES:
        display.show(frame)
        sleep(80)
    display.clear()
    sleep(250)


# ------------------------------------------------------------------
# Modules
# ------------------------------------------------------------------

def test_ac():
    display.scroll("Test...", SCROLL_SPEED)
    speeds = (300, 750, 1023)
    for level, speed in enumerate(speeds, 1):
        display.show(str(level))
        pin0.write_analog(speed)
        sleep(3000)
        pin0.write_analog(0)
        sleep(1500)
    display.clear()


def test_headlights():
    display.scroll("Test...", SCROLL_SPEED)
    brightness_levels = (100, 500, 1023)
    for level, value in enumerate(brightness_levels, 1):
        display.show(str(level))
        pin.write_analog(value)
        sleep(3000)
        pin.write_analog(0)
        sleep(1500)
    display.clear()


def test_radio():
    display.scroll("Test...", SCROLL_SPEED)
    speaker.off()
    set_volume(255)
    tunes = ((music.ENTERTAINER, 120), (music.BLUES, 80), (music.NYAN, 150))
    for level, (tune, bpm) in enumerate(tunes, 1):
        display.show(str(level))
        music.set_tempo(bpm=bpm)
        music.play(tune, wait=False, pin=pin1)
        sleep(7500)
        music.stop()
        sleep(1500)
    display.clear()


# ------------------------------------------------------------------
# Menu
# ------------------------------------------------------------------

MODULES = (("AC", test_ac), ("Radio", test_radio), ("Headlights", test_headlights))


def show_current_option(selected, last_selected, repeat_counter):
    """
    Returns updated repeat_counter and last_selected.
    """
    if selected != last_selected or repeat_counter > 15:
        display.scroll(MODULES[selected][0], MENU_SCROLL_SPEED)
        repeat_counter = 0
    repeat_counter += 1
    return repeat_counter, selected


# ------------------------------------------------------------------
# Startup
# ------------------------------------------------------------------

display.scroll("WELCOME!", SCROLL_SPEED)
load()

# ------------------------------------------------------------------
# Main Program
# ------------------------------------------------------------------

selected_module = 0
last_selected = -1
repeat_counter = 0

while True:
    repeat_counter, last_selected = show_current_option(selected_module, last_selected, repeat_counter)
    if button_a.was_pressed():
        selected_module = (selected_module + 1) % len(MODULES)
    if button_b.was_pressed():
        load()
        module_function = MODULES[selected_module][1]
        module_function()
        load()
        last_selected = -1
    sleep(50)
