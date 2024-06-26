from microbit import *

def draw_meter(level):
    # Ensure level is within 0 to 25
    level = max(0, min(25, level))
    # Iterate over all the pixels
    for i in range(25):
        x = i % 5
        y = 4 - i // 5 
        # If this pixel should be lit, set its brightness to 9
        if i < level:
            display.set_pixel(x, y, 9)
        # Otherwise, clear this pixel
        else:
            display.set_pixel(x, y, 0)


while True:
    # 0-255
    lvl = display.read_light_level()
    lvl_scaled = scale(lvl, from_=(0, 255), to=(0,25))
    draw_meter(lvl_scaled)

    
