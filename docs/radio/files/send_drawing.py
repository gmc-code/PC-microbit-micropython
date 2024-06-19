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