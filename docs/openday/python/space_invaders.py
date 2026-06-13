from microbit import *
import random


MIN_COORD, MAX_COORD = 0, 4  # Range of valid coordinates for the display.
MAX_MISSILES = 5  # Number of missiles player can have on screen at once.
DIFFICULTY_INCREASE = 0.25  # Increase in difficulty between waves.

ALIEN_START_POSITIONS = [
    # Each row is a unique start pattern, defined as tuples of x,y coordinates.
    [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (3, 1)],
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (2, 1)],
    [(1, 0), (2, 0), (3, 0), (0, 1), (2, 1), (4, 1)],
    [(1, 0), (2, 0), (3, 0), (1, 1), (3, 1), (2, 2)],
]


def wait_for_button():
    """ Wait for either button to be pressed. """
    while not (button_a.was_pressed() or button_b.was_pressed()):
        sleep(1)


def move(sprite, x, y):
    """ Move the given sprite by the given x & y amounts. """
    return sprite[0] + x, sprite[1] + y


def in_bounds(pos):
    """ Return True if the position is within the valid screen coordinates. """
    if pos[0] < MIN_COORD or pos[0] > MAX_COORD:
        return False
    if pos[1] < MIN_COORD or pos[1] > MAX_COORD:
        return False
    return True


class Game:
    """ Game class holds the current game state. """

    def game_reset(self):
        # Initial values
        self.x = 2  # Player x coordinate start (middle).
        self.xf = 2.0  # x coordinate float, allows us to use tilt for move speed.

        self.missiles = []  # Active missiles on screen.
        self.aliens = []  # Active aliens on screen.
        self.alien_velocity_x = 1  # Horizontal speed of aliens.

        self.bombs = 3  # Number of bombs the player has.
        self.active_bomb = 0  # Countdown timer for the current active bomb.

        self.score = 0  # Player score.

        self.tick = 0  # Game loop tick.
        self.level = 0  # Current game level.
        self.difficulty = 20  # Is in reverse, decrement to increase.

    def handle_input(self):
        self.tick += 1
        acc_x = accelerometer.get_x()

        # Use the accelerometer / 512 so the player can move x at speed by tilting more.
        if acc_x < 0:
            self.xf += acc_x / 512
        if acc_x > 0:
            self.xf += acc_x / 512

        # Constrain to the screen dimensions.
        if self.xf > MAX_COORD:
            self.xf = MAX_COORD

        if self.xf < MIN_COORD:
            self.xf = MIN_COORD

        self.x = int(self.xf)

        if button_a.was_pressed():
            # Add missile, at players current x position.
            self.missiles.append((self.x, 4))

        if button_b.was_pressed() and self.bombs:
            # Fire bomb. Flash + remove half the aliens.
            # randint(0,1) will be 50% 1, 50% 0 ..if 0 (False) alien will be skipped.
            self.aliens = [alien for alien in self.aliens if random.randint(0, 1)]
            self.active_bomb = 3  # Reduces 1 per tick. Screen at 3 * bright.
            self.bombs -= 1

    def add_aliens(self):
        # We need to copy, or we'll me modifying the original lists.
        alien_position = self.level % len(ALIEN_START_POSITIONS)
        self.aliens = ALIEN_START_POSITIONS[alien_position].copy()
        self.tick = 0

    def advance_aliens(self):
        """ If aliens have reached the screen edge, advance them all downwards. """
        for alien in self.aliens:
            if (self.alien_velocity_x == -1 and alien[0] == MIN_COORD) or (
                self.alien_velocity_x == +1 and alien[0] == MAX_COORD
            ):
                # If any aliens are at the far edge, increment y, and reverse.
                self.alien_velocity_x = -self.alien_velocity_x
                self.aliens = [move(alien, 0, 1) for alien in self.aliens]
                # This can happen if detached alien slips past bottom.
                self.aliens = [alien for alien in self.aliens if in_bounds(alien)]
                return True  # No other move this time.

    def aliens_can_move(self):
        if self.tick > self.difficulty:
            self.tick = 0
            return True

    def move_aliens(self):
        # Move aliens horizontally.
        self.aliens = [move(alien, self.alien_velocity_x, 0) for alien in self.aliens]

    def move_missiles(self):
        # Advance positions of missiles (upwards)
        self.missiles = [move(missile, 0, -1) for missile in self.missiles]
        self.missiles = [missile for missile in self.missiles if in_bounds(missile)]

    def check_collisions(self):
        for missile in self.missiles[:]:  # Iterate a copy.
            if missile in self.aliens:
                # Since we store by coordinates, we can remove using the missile coords.
                self.aliens.remove(missile)
                self.missiles.remove(missile)
                self.score += 1

        if not self.aliens:
            # Wave complete? Increase difficulty (decrement) and add new aliens.
            self.difficulty -= DIFFICULTY_INCREASE
            self.level += 1
            self.bombs += 1
            self.add_aliens()

    def draw(self):
        display.clear()

        if self.active_bomb:
            # Bomb is drawn as an overlay of gradually decaying light.
            for dx in range(MAX_COORD + 1):
                for dy in range(MAX_COORD + 1):
                    display.set_pixel(dx, dy, self.active_bomb * 3)

            # Decrement so next draw is fainter.
            self.active_bomb -= 1

        # Draw all the aliens.
        for pos in self.aliens:
            display.set_pixel(pos[0], pos[1], 9)

        # Draw all the current player missiles.
        for pos in self.missiles:
            display.set_pixel(pos[0], pos[1], 5)

        # Draw the players spaceship.
        display.set_pixel(self.x, 4, 9)

    def game_over(self):
        return (self.x, 4) in self.aliens


game = Game()  # Create our game object.


while True:

    display.show(Image.TARGET)
    wait_for_button()

    game.game_reset()  # Reset the game state.
    game.add_aliens()

    # Main loop
    while not game.game_over():
        game.handle_input()
        if game.aliens_can_move():
            if not game.advance_aliens():
                game.move_aliens()
        game.move_missiles()
        game.draw()
        game.check_collisions()

        sleep(100)

    display.show(Image.ANGRY)
    sleep(1000)
    display.scroll(game.score)
