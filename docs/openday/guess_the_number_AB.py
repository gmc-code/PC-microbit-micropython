from microbit import *
import random


def get_secret(min_num=1, max_num=9):
    return random.randint(min_num, max_num)


def select_number(start_num, min_num=1, max_num=9):
    counter = start_num
    display.show(counter, delay=200)

    # Wait until the logo is pressed to confirm
    while pin_logo.is_touched() is False:

        # A decreases, stops at 1
        if button_a.is_pressed():
            if counter > min_num:
                counter -= 1
            display.show(counter, delay=200)
            sleep(200)

        # B increases, stops at 9
        if button_b.is_pressed():
            if counter < max_num:
                counter += 1
            display.show(counter, delay=200)
            sleep(200)

        sleep(100)

    return counter



def check_guess(secret_num, guess):
    if guess == secret_num:
        display.show(Image.YES)
        sleep(400)
        return True
    elif guess > secret_num:
        display.show(Image.ARROW_S)
        sleep(400)
        display.show(guess)
        return False
    else:
        display.show(Image.ARROW_N)
        sleep(400)
        display.show(guess)
        return False


secret_num = get_secret()
guess = 5
game_guesses = 0
guessed = False
display.scroll("1-9?")


while True:
    guess = select_number(guess, min_num=1, max_num=9)
    game_guesses += 1
    guessed = check_guess(secret_num, guess)

    if guessed:
        display.scroll(str(game_guesses) + " GUESSES", delay=80)
        # new game
        secret_num = get_secret()
        guess = 5
        game_guesses = 0
        guessed = False
