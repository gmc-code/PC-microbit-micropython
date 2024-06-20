====================================================
Radio draw
====================================================

Send Drawn Image
------------------

| This script acts like a simple drawing program on the microbit.
| You can move around the grid by tilting the microbit, toggle LEDs on and off with A button, and send your drawing to another microbit with the B button.

| The `x` and `y` variables represent the current position on the microbit's LED display. 
| The `tick` variable is used to control the blinking of the current position. 
| The `grid` list represents the state of each LED on the display.

| `Toggle(tx, ty)`: toggles the state of the LED at position `(tx, ty)` on the grid.
| The `^=` operator is a bitwise XOR operation that is used here to toggle between 0 and 1. 
| If `grid[tx][ty]` is 0, `grid[tx][ty] ^= 1` will set it to 1, and if `grid[tx][ty]` is 1, `grid[tx][ty] ^= 1` will set it back to 0.


| `Draw(t)`: creates an image representing the current state of the grid and the position `(x, y)`. The position `(x, y)` blinks on and off every other tick.
| It starts by creating a blank image with all LEDs off. 
| Then it loops over each position `(cx, cy)` in the grid. 
| If `grid[cx][cy]` is 1, it sets the pixel at `(cx, cy)` to a brightness of 5 via ``img.set_pixel(cx, cy, grid[cx][cy]*5) ``.
| ``img.set_pixel(x, y, (t % 2)*9)`` creates a blinking effect for the pixel at the current position, `(x, y)`. 
| ``(t % 2)`` gives the remainder then t is divided by 2. ``(t % 2)*9)`` is 0 when `t` is even or 9 if `t` is odd.
| The function returns the created image.


| `ImageString()`: converts the current state of the grid into a string that can be sent over the radio.
| It starts with an empty string, then loops over each position `(cx, cy)` in the grid. 
| It adds the brightness of the pixel at `(cx, cy)` (either 0 or 9) to the string. 
| After each row of the grid, it adds a colon to the string. 
| The resulting string represents the current state of the grid in a format that can be easily sent over the radio and interpreted by another microbit running the same script.

| The accelerometer is used to change the position `(x, y)`. 
| If the microbit is tilted to the left or right, `x` is decreased or increased. 
| If the microbit is tilted forward or backward, `y` is decreased or increased.
| If the A button is pressed, the state of the LED at the current position `(x, y)` is toggled.
| The display is updated to show the current state of the grid and the position `(x, y)`.
| If the B button is pressed, the current state of the grid is sent over the radio.


.. code-block:: python

    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    x = 2
    y = 2
    tick = -1

    grid = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
        ]


    def Toggle(tx, ty):
        # bitwise or swaps 0 for 1 and 1 for 0
        grid[tx][ty] ^= 1
                

    def Draw(t):
        img = Image('00000:'*5)
        for cy in range(0,5):
            for cx in range(0,5):
                img.set_pixel(cx, cy, grid[cx][cy]*5) 
        img.set_pixel(x, y, (t % 2)*9)
        return img


    def ImageString():
        s = ""
        for cy in range(0,5):
            for cx in range(0,5):
                s += str(grid[cx][cy]*9)
            s += ":"
        return s


    while True:
        tick +=1
        if tick==2:
            tick = 0
        # check for movement
        dx = accelerometer.get_x()
        dy = accelerometer.get_y()
        if dx > 300:
            x += 1
            sleep(200)
        if dx < -300:
            x -= 1
            sleep(200)
        if dy > 300:
            y += 1
            sleep(200)
        if dy < -300:
            y -= 1
            sleep(200)
        # keep on grid    
        x = max(0, min(x, 4))
        y = max(0, min(y, 4))
        # check for button press
        if button_a.was_pressed():
            Toggle(x, y)
            sleep(200)
        # update screen
        i = Draw(tick)
        display.show(i)
        if button_b.was_pressed():
            radio.send(ImageString())      
        sleep(50)


| Use this code to receive the image.

.. code-block:: python
    
    from microbit import *
    import radio

   
    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        incoming_message = radio.receive()
        if incoming_message:
            # print(incoming_message)
            i = Image(incoming_message)
            display.show(i)

----

.. admonition:: Exercise

    #. Design a game room with 25 desks in a 5 by 5 grid. On each of these desks, place cards different values according to a drawn map. A copy of the card value maps is given to each controller in each pair. The controllers take it in turns to draws the places to go to on their microbit, directing their playing partner to cards of the highest value. Limit the time for each player to 30 seconds. After all the cards are collected declare the winner with the highest score.
    
    .. image:: images/card_draw.png
            :scale: 60 %
    