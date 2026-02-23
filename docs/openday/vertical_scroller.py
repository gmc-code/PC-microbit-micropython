from microbit import *
import random


def draw(track, t, x, y):
    img = Image(track)
    img.set_pixel(x, y, t * 4 + 1)
    return img


def play_game():
    # lines of track
    track_bits = ["50005:", "53005:", "50305:", "50035:"]
    # starting track
    track = "50005:50005:50005:50005:50005:"
    # co-ordinates of player character
    x = 2
    y = 4
    # time variable for blinking
    tick = 0
    score = 0
    # track pace
    sleep_delay = 150
    last = 0
    alive = True
    while alive == True:
        tt = draw(track, tick, x, y)
        if button_a.was_pressed() and x != 1:
            x = x - 1
        elif button_b.was_pressed() and x != 3:
            x = x + 1
        # update ticks
        tick += 1
        # show track
        display.show(tt)
        # every third tick
        if tick == 3:
            # update score
            score += 1
            # check for collision
            if tt.get_pixel(x, y - 1) != 0:
                alive = False
            # reset ticks
            tick = 0
            # delete bottom row of track
            track = track[:-6]
            # update track
            if last == 0:
                last = random.randint(0, len(track_bits) - 1)
            else:
                last = 0
            track = track_bits[last] + track
            # redraw screen
            tt = draw(track, tick, x, y)
            display.show(tt)
        sleep(sleep_delay)
    display.scroll(score, delay=80)


def main():
    while True:
        if button_a.was_pressed():
            play_game()
            sleep(3000)
        sleep(50)


main()
