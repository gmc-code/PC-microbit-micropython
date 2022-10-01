====================================================
Guess the number
====================================================

| The code to play the **guess the number** game is developed in stages below.

----

Random integer
-----------------

| The function, **get_secret**, returns a random integer from 1 to 9 inclusive.

.. code-block:: python

    from microbit import *
    import random

    def get_secret():
        return random.randint(1, 9)


.. admonition:: Tasks

    #. Add parameters to the **get_secret** function, **min_num** and **max_num** to specify the lowest and highest possible returned integers.
    #. Change the parameters use have a default **min_num** of 1 and  **max_num** of 9.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    .. code-block:: python

                        from microbit import *
                        import random
                        
                        def get_secret(min_num, max_num):
                            return random.randint(min_num, max_num)

                .. tab-item:: Q2

                    .. code-block:: python

                        from microbit import *
                        import random
                        
                        def get_secret(min_num=1, max_num=9):
                            # default to 1 to 9
                            return random.randint(min_num, max_num)


----

Guess the number level 1
--------------------------

| Build a guessing game in which the player has to guess a number between 1 and 9.
| Scroll the text "1-9?" at the start then display "5" as the starting number for your guess.
| Use random.randint(x,y) for random integers.
| Use while True for the event loop.
| Use the A button to decrease the guess number by 1.  Use the special operator += to add 1 to the variable. e.g. variablename += 1 
| Use the B button to make a guess.
| Give feedback with ARROW_N to go higher and ARROW_S to go lower
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
| Store the total games played and the total guesses in the variables: totalgames, totalguesses. 
