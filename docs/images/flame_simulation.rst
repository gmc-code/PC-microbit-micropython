====================================================
Flame simulation
====================================================


The Flame simulation
-------------------------

| See: `<https://github.com/bbcmicrobit/micropython/blob/master/examples/flame_simulation.py
| The simulation uses a mask to multiply the brightness of each pixel by a given factor.
| Pixels are shifted up the display, taking into account the pixel brightness of those around them.

.. code-block:: python

    # ed GMC 2022
    # ## Flame simulation on the Microbit.
    # ## Author: M. Schafer 2016 in the public domain.

    import microbit
    import random

    # User adjustable values for speed of animation; use B-button
    MIN_SLEEP = 0
    MAX_SLEEP = 100
    # set button-B value to adjust sleep times in increments
    INC_SLEEP = 20

    # User adjustable values for interpolation; use a button
    MAX_percent_increment = 55
    MIN_percent_increment = 5

    # User adjustable values for range of brightness in flames.
    MIN_BRIGHTNESS = 2
    MAX_BRIGHTNESS = 8

    #  fixed for the Microbit; can;t be above 5, can use smaller part of screen though > 1
    DISPLAY_WIDTH = 5
    DISPLAY_HEIGHT = 5

    # flame can be oriented in either direction; True has top of flame at top of microbit
    INVERT_DISPLAY = True

    # MASK to create fire shape. multiplies values %
    MASK = [
        [88, 100, 100, 100, 88],
        [60, 95, 100, 95, 60],
        [50, 88, 90, 88, 50],
        [33, 75, 88, 75, 33],
        [10, 33, 66, 33, 10],
    ]


    # Generate a new bottom row of random values for the flames
    def generate_line(start=MIN_BRIGHTNESS, end=MAX_BRIGHTNESS):
        "start and end define range of dimmest to brightest 'flames'"
        return [start + random.randrange(end - start) for i in range(DISPLAY_WIDTH)]


    # shift all values in the grid up one row
    def shift_up(grid, newline):
        "Shift up lines in grid, add newline at bottom"
        for y in range(DISPLAY_HEIGHT - 1, 0, -1):
            grid[y] = grid[y - 1]
        # lowest line
        for x in range(DISPLAY_WIDTH):
            grid[0] = newline


    # write a frame to the screen.
    # Interpolate values based on percent
    def interpolate_frame(screen, pcnt, grid, line):
        """Interpolate new values by reading from grid and
        writing to the screen"""
        # each row interpolates with the one before it
        for y in range(DISPLAY_HEIGHT - 1, 0, -1):
            for x in range(DISPLAY_WIDTH):
                mask = MASK[y][x]
                new_val = ((100 - pcnt) * grid[y][x] + pcnt * grid[y - 1][x]) / 100.0
                new_val = mask * new_val / 100.0
                if INVERT_DISPLAY:
                    screen.set_pixel(x, DISPLAY_HEIGHT - y - 1, int(new_val))
                else:
                    screen.set_pixel(x, y, int(new_val))
        # first row interpolates with the "next" line; y == 1 from loop above
        for x in range(DISPLAY_WIDTH):
            mask = MASK[y][x]
            new_val = ((100 - pcnt) * grid[0][x] + pcnt * line[x]) / 100.0
            new_val = mask * new_val / 100.0
            if INVERT_DISPLAY:
                screen.set_pixel(x, DISPLAY_HEIGHT - 1, int(new_val))
            else:
                screen.set_pixel(x, 0, int(new_val))


    # # Setup
    line = generate_line()
    grid = [[0 for i in range(DISPLAY_WIDTH)] for i in range(DISPLAY_HEIGHT)]
    # grid = [[0,0,0,0,0],
    #        [0,0,0,0,0],
    #        [0,0,0,0,0],
    #        [0,0,0,0,0],
    #        [0,0,0,0,0]]
    SCREEN = microbit.display
    percent = 0  # counter to see when to re-interpolate
    sleep_time = 0  # delay between updates
    percent_increment = 25  # how fast we interpolate fire


    # loop forever
    while True:
        if percent > 100:
            # move everything up a line, insert new bottom row
            line = generate_line()
            shift_up(grid, line)
            percent = 0
        # Check Buttons to see if changing
        # button_a = smoothness
        if microbit.button_a.was_pressed():
            percent_increment += 5
            if percent_increment > MAX_percent_increment:
                percent_increment = MIN_percent_increment
            print("percent interpolate=", percent_increment)
        # button_b = delay
        if microbit.button_b.was_pressed():
            sleep_time += INC_SLEEP
            if sleep_time > MAX_SLEEP:
                sleep_time = MIN_SLEEP
            print("sleep_time=", sleep_time)
        # draw frame and sleep
        interpolate_frame(SCREEN, percent, grid, line)
        microbit.sleep(sleep_time)
        # update main counters
        percent += percent_increment

