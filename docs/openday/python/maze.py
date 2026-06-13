from microbit import *

# FINAL MAZES (converted to 0/1)
MAZES = [
    # 7x7
    [
        "1111111",
        "0000001",
        "1011101",
        "1000101",
        "1110101",
        "1000000",
        "1111111"
    ],
    # 9x9
    [
        "111111111",
        "000000001",
        "101111101",
        "100001001",
        "111101101",
        "100001001",
        "101101101",
        "100000000",
        "111111111"
    ],
    # 11x11
    [
        "11111111111",
        "00000000001",
        "10111111001",
        "10100001001",
        "10101101001",
        "10101001001",
        "10101001101",
        "10100000001",
        "10111111001",
        "10000000000",
        "11111111111"
    ]
]

# Start openings (in wall)
START_OPENINGS = [(0,1), (0,1), (0,1)]
# Player starts inside the maze
STARTS = [(1,1), (1,1), (1,1)]
# Exit openings (in wall)
EXIT_OPENINGS = [(6,5), (8,7), (9,9)]
# Exit tiles inside the maze
EXITS = [(5,5), (7,7), (8,9)]


def draw_window(maze, px, py):
    img = Image(5,5)
    for dy in range(5):
        for dx in range(5):
            mx = px + dx - 2
            my = py + dy - 2
            if 0 <= mx < len(maze[0]) and 0 <= my < len(maze):
                if maze[my][mx] == "1":
                    img.set_pixel(dx, dy, 5)
    img.set_pixel(2,2,9)
    return img


def play_maze(maze, start, start_opening, exit_tile):
    x, y = start
    sx, sy = start_opening
    ex, ey = exit_tile

    # Close the start opening behind the player
    maze[sy] = maze[sy][:sx] + "1" + maze[sy][sx+1:]

    speed = 120  # starting speed (ms)

    while True:
        display.show(draw_window(maze, x, y))

        dx = dy = 0

        # SPEED CONTROL
        if button_a.was_pressed():
            speed = min(300, speed + 20)  # slow down
        if button_b.was_pressed():
            speed = max(40, speed - 20)   # speed up

        # MOVEMENT (tilt)
        if accelerometer.get_x() < -200:
            dx = -1
        elif accelerometer.get_x() > 200:
            dx = 1
        elif accelerometer.get_y() < -200:
            dy = -1
        elif accelerometer.get_y() > 200:
            dy = 1

        # APPLY MOVEMENT
        nx = x + dx
        ny = y + dy
        if maze[ny][nx] == "0":
            x, y = nx, ny

        # EXIT CHECK
        if (x, y) == (ex, ey):
            return

        sleep(speed)


def main():
    while True:
        display.show(Image.HAPPY)
        if button_a.was_pressed():
            for i in range(len(MAZES)):
                maze = MAZES[i].copy()
                play_maze(maze, STARTS[i], START_OPENINGS[i], EXITS[i])
                display.show(Image.YES)
                sleep(1000)
            display.scroll("WIN!")
        sleep(100)

main()
