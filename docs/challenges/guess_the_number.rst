====================================================
Guess the number
====================================================

| The code to play the **guess the number** game is developed in stages below.

----

Random integer
-----------------

| The microbit needs to pick a random integer between 1 and 9 that will be guessed by the user.
| The function, **get_secret**, returns a random integer from 1 to 9 inclusive.

.. code-block:: python

    from microbit import *
    import random

    def get_secret():
        return random.randint(1, 9)


.. admonition:: Tasks

    #. Add parameters to the **get_secret** function, **min_num** and **max_num** to specify the lowest and highest possible returned integers.
    #. Modify the parameters to have a default of 1 for **min_num** of 9 for  **max_num**.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Add parameters to the **get_secret** function, **min_num** and **max_num** to specify the lowest and highest possible returned integers.

                    .. code-block:: python

                        from microbit import *
                        import random
                        
                        def get_secret(min_num, max_num):
                            return random.randint(min_num, max_num)

                .. tab-item:: Q2

                    Modify the parameters to have a default of 1 for **min_num** of 9 for  **max_num**.

                    .. code-block:: python

                        from microbit import *
                        import random
                        
                        def get_secret(min_num=1, max_num=9):
                            return random.randint(min_num, max_num)

----

Select number
-----------------

| The user needs to use the buttons to select a guess number to make the guess with.
| The function, **select_number(start_num, min_num, max_num)**, was developed in the **number_chooser** page.

----

Check the guess
-----------------

| The guess number needs to be compared with the secret number.
| The function, **check_guess(secret_num, guess)**, returns True if the **secret_num** and the **guess** match. It returns False if they don't match.
| Visual feedback is added via images: YES for correct, arrows to hint at the guess direction.
| When wrong, the guess number needs to be re-shown after the feedback, as a reminder of the last guess.

| The code is scaffolded below, but needs completion.

.. code-block:: python

    def check_guess(secret_num, guess):
        if guess == secret_num:
            display.show.........
            sleep(400)
            return .........
        elif guess > secret_num:
            display.show(.........)
            sleep(400)
            display.show(guess)
            return .........
        else:
            display.show(.........)
            sleep(400)
            display.show(guess)
            return .........


.. admonition:: Tasks

    #. Complete the code for the check_guess function.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: check_guess

                    .. code-block:: python
   
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


----

Guess the number version 1
-----------------------------

| Build a guessing game in which the player has to guess a number between 1 and 9.
| Scroll the text "1-9?" at the start then display "5" as the starting number for the user's guess.
| Use random.randint(min_num=1, max_num=9) for the secret number to be guessed.
| Use select_number(start_num, min_num, max_num) to select the number for the guess.
| Use the A button to increase the guess number by 1.
| Use the B button to make a guess.
| Give feedback with ARROW_N to go higher and ARROW_S to go lower
| Show a tick when correct.
| Use a while loop that stops when the secret number has been guessed. Set the flag: **guessed = False** before the loop.

----

.. admonition:: Tasks

    #. Build Guess the number version 1.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Version 1

                    .. code-block:: python

                        from microbit import *
                        import random


                        def get_secret(min_num=1, max_num=9):
                            return random.randint(min_num, max_num)


                        def select_number(start_num, min_num=1, max_num=9):
                            counter = start_num
                            display.show(counter, delay=200)
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    counter += 1
                                    if counter > max_num:
                                        counter = min_num
                                    display.show(counter, delay=200)
                                sleep(200)
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
                        guessed = False
                        display.scroll("1-9?")
                        while guessed is False:
                            guess = select_number(guess, min_num=1, max_num=9)
                            guessed = check_guess(secret_num, guess)


----

New versions:
-------------------------

| Modify the while loop so that a new game is automatically started.
| Add counting of the number of guesses made and display it at the end of a game.
| Add tracking of the total number of games played and the best score.

----


Guess the number version 2
-----------------------------

| Modify the while loop so that a new game is automatically started.
| Do this by moving the condition out of the while loop and test it in an if statement.

.. admonition:: Tasks

    #. Modify the while loop so that a new game is automatically started. Just show the main code, excluding functions.
    #. Show the full code.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Main code modifications

                    .. code-block:: python

                        from microbit import *
                        import random


                        secret_num = get_secret()
                        guess = 5
                        guessed = False
                        display.scroll("1-9?")
                        while True:
                            guess = select_number(guess, min_num=1, max_num=9)
                            guessed = check_guess(secret_num, guess)
                            if guessed:
                                # new game
                                secret_num = get_secret()
                                guess = 5
                                guessed = False 

                .. tab-item:: Full code

                    .. code-block:: python

                        from microbit import *
                        import random


                        def get_secret(min_num=1, max_num=9):
                            return random.randint(min_num, max_num)


                        def select_number(start_num, min_num=1, max_num=9):
                            counter = start_num
                            display.show(counter, delay=200)
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    counter += 1
                                    if counter > max_num:
                                        counter = min_num
                                    display.show(counter, delay=200)
                                sleep(200)
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
                        guessed = False
                        display.scroll("1-9?")
                        while True:
                            guess = select_number(guess, min_num=1, max_num=9)
                            guessed = check_guess(secret_num, guess)
                            if guessed:
                                # new game
                                secret_num = get_secret()
                                guess = 5
                                guessed = False 


----

Guess the number version 3
-----------------------------

| Add counting of the number of guesses made and display it at the end of a game.
| Add a variable **game_guesses** to keep track of the number of guesses made.

.. admonition:: Tasks

    #. Add counting of the number of guesses made and display it at the end of each game. Just show the main code, excluding functions.
    #. Show the full code.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Main code modifications

                    .. code-block:: python

                        from microbit import *
                        import random


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

                .. tab-item:: Full code

                    .. code-block:: python

                        from microbit import *
                        import random


                        def get_secret(min_num=1, max_num=9):
                            return random.randint(min_num, max_num)


                        def select_number(start_num, min_num=1, max_num=9):
                            counter = start_num
                            display.show(counter, delay=200)
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    counter += 1
                                    if counter > max_num:
                                        counter = min_num
                                    display.show(counter, delay=200)
                                sleep(200)
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

----

Guess the number version 4
-----------------------------

| Add tracking of the total number of games played and the best score.
| Add the variables **best_score** and **total_games**.

| Initially, there is no best score value. 
| Rather than setting at an arbitrarily high value such as 98765, it should be set to **None**.

.. admonition:: Tasks

    #. Write a function, **get_best_score**, that gets the lower value from the current **best_score** and **game_guesses** from a finished game. Use an if statement to first check whether **best_score** is **None**.
    
    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: get_best_score

                    .. code-block:: python

                        from microbit import *
                        import random


                        def get_best_score(best_score, game_guesses):
                            if best_score is None:
                                return game_guesses
                            else:
                                return min(best_score, game_guesses)

----

.. admonition:: Tasks

    #. Add tracking of the total number of games played and the best score. Just show the main code.
    #. Show the full code.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Modifications

                    .. code-block:: python

                        from microbit import *
                        import random


                        def get_best_score(best_score, game_guesses):
                            if best_score is None:
                                return game_guesses
                            else:
                                return min(best_score, game_guesses)


                        total_games = 1
                        best_score = None
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
                                best_score = get_best_score(best_score, game_guesses)
                                display.scroll("BEST: " + str(best_score) + " GAMES: " + str(total_games), delay=80)
                                # new game
                                total_games += 1
                                secret_num = get_secret()
                                guess = 5
                                game_guesses = 0
                                guessed = False

                .. tab-item:: Full code.

                    .. code-block:: python

                        from microbit import *
                        import random


                        def get_secret(min_num=1, max_num=9):
                            return random.randint(min_num, max_num)


                        def select_number(start_num, min_num=1, max_num=9):
                            counter = start_num
                            display.show(counter, delay=200)
                            while button_b.was_pressed() is False:
                                if button_a.is_pressed():
                                    counter += 1
                                    if counter > max_num:
                                        counter = min_num
                                    display.show(counter, delay=200)
                                sleep(200)
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


                        def get_best_score(best_score, game_guesses):
                            if best_score is None:
                                return game_guesses
                            else:
                                return min(best_score, game_guesses)


                        total_games = 1
                        best_score = None
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
                                best_score = get_best_score(best_score, game_guesses)
                                display.scroll("BEST: " + str(best_score) + " GAMES: " + str(total_games), delay=80)
                                # new game
                                total_games += 1
                                secret_num = get_secret()
                                guess = 5
                                game_guesses = 0
                                guessed = False

----

Guess the number extension ideas
---------------------------------

| Replace automatic new games with being asked to confirm a new game with a button press.
| At the start of the game, ask for button presses to confirm the number range as 1-9 or 1 - 99.
| For 1-99 games, use sideways tilting to change the guess, with greater tilting used to move in steps of 10.
| Add more feedback at the end of games, including best and worst scores, total games and average. Consider asking the user to confirm this with a button press.



