from microbit import *
import radio
radio.config(group=8)
radio.on()


def display_level(level):
    x_list = [0, 1, 2, 3, 4]
    # display
    if level < 2:
        y_val = 4
        y_list = None
        y_clear_list = [0, 1, 2, 3]
    elif level < 4:
        y_val = 3
        y_list = [4]
        y_clear_list = [0, 1, 2]
    elif level < 6:
        y_val = 2
        y_list = [3, 4]
        y_clear_list = [0, 1]
    elif level < 8:
        y_val = 1
        y_list = [2, 3, 4]
        y_clear_list = [0]
    elif level < 10:
        y_val = 0
        y_list = [1, 2, 3, 4]
        y_clear_list = None
    else:
        y_val = None
        y_list = [0, 1, 2, 3, 4]
        y_clear_list = None

    for x in x_list:
        if y_val is not None:
            display.set_pixel(x, y_val, val)
        if y_list is not None:
            for y in y_list:
                display.set_pixel(x, y, 9)
        if y_clear_list is not None:
            for y in y_clear_list:
                display.set_pixel(x, y, 0)


while True:
    message = radio.receive_full()
    if message:
        signal = int(message[1])
        # scale signal strength to levels 0 to 9
        # the values here may need adjusting(-116, -17)
        level = scale(signal, from_=(-116, -17), to=(0, 9))
        display_level(level)
