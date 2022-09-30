====================================================
Guess the number
====================================================

Guess the number level 1
--------------------------

| Build a guessing game in which the player has to guess a number between 1 and 9.
| Scroll the text "1-9?" at the start then display "5" as the starting number for your guess.
| Use random.randint(x,y)  for random integers.
| Use while True for the event loop.
| Use and in the if statements to make sure that pressing A & B together is detected properly.  
| e.g. button_a.is_pressed() and button_b.is_pressed()
| For separate A or B presses use and not to rule out the other button. 
| e.g. button_a.is_pressed() and not button_b.is_pressed()
| Use the A button to decrease the guess number by 1.  Use the special operator += to add 1 to the variable. 
| e.g. variablename += 1 
| Use the B button to increase the guess number by 1.   Use the special operator -= to subtract 1 from the variable.  e.g. variablename -= 1 
| Use A & B to make a guess.
| Use A & B to also receive feedback with ARROW_N for try higher and ARROW_S to try lower
| Use a 400ms sleep before displaying the current guess again.
| Show a tick when correct.

----

.. admonition:: Tasks

    #. Build a guessing game.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    .. code-block:: python

                        from microbit import *
                        import random


                        def get_secret(min_num=1, max_num=9):
                            # default to from 1 to 9
                            return random.randint(min_num, max_num)


                        def select_number(num, min_num=1, max_num=9):
                            # limit to 1 to 9; repeat until both buttons pressed together
                            while True:
                                display.show(num)
                                if button_a.is_pressed() and button_b.is_pressed():
                                    return num
                                elif button_a.is_pressed() and not (button_b.is_pressed()):
                                    if num > min_num:
                                        num -= 1
                                elif button_b.is_pressed() and not (button_a.is_pressed()):
                                    if num < max_num:
                                        num += 1
                                sleep(200)


                        def check_guess(secret_num, guess, game_guesses):
                            if guess == secret_num:
                                display.show(Image.YES)
                                sleep(400)
                                display.scroll(str(game_guesses) + " GUESSES", delay=80)
                                sleep(400)
                                return True
                            elif guess > secret_num:
                                display.show(Image.ARROW_S)
                                sleep(400)
                                display.show(str(guess))
                            else:
                                display.show(Image.ARROW_N)
                                sleep(400)
                                display.show(str(guess))
                            return False


                        game_guesses = 0
                        secret_num = get_secret()
                        guess = 5
                        
                        while True:
                            guess = select_number(guess, min_num=1, max_num=9)
                            game_guesses += 1
                            guessed = check_guess(secret_num, guess, game_guesses)
                            if guessed:
                                # new game
                                secret_num = get_secret()
                                game_guesses = 0

----

Guess the number level 2
--------------------------

| Enhance the guessing game.
| Limit the affect of A and B buttons so that only numbers 1 to 9 can be chosen. Do this by using an if statement that checks that the variable is above 0 or below 9 as needed, after pressing A or B.
| Store the total games played and the total guesses in the variables: totalgames, totalguesses. 
| e.g. def startguesses():
| See: https://microbit-challenges.readthedocs.io/en/latest/basics/functions.html 
| or https://www.w3schools.com/python/python_functions.asp
| To use the variables in a function block pass the variables to the funciton and return any changes to them.
| See: https://www.w3schools.com/python/python_variables.asp
| Use shake to restart to 0 games played.
| Set the games played and total guesses back to 0.
| Scroll the avarage guesses per game when a number is guessed correctly.
| Use Pin 0 (pin0.is_touched()) to scroll the avarage guesses per game.
| See: https://microbit-micropython.readthedocs.io/en/latest/tutorials/io.html
| Use the round function to calculate the average, rounded to 1 decimal place. 
| See: https://www.w3schools.com/python/ref_func_round.asp
