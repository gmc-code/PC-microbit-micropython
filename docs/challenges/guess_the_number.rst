====================================================
Guess the number
====================================================

| The code to play the **guess the number** game is developed in stages below.

----

| The microbit needs to pick a random integer between 1 and 9 that will be guessed by the user.

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

| The user needs to use the buttons to select a guess number to make the guess with.

Select number
-----------------

| The function, **select_number(start_num, min_num, max_num)**, was developed in the **number_chooser** page.

----

| The guess number needs to be compared with the secret number.

Check the guess
-----------------

| The function, **check_guess(secret_num, guess)**, returns True if the **secret_num** and **guess** match. It returns False if they don't match.
| Visual feedback is added via images: YES for correct, arrows to hint at the guess direction.
| When wrong, the guess number needs to be reshown after the feedback, as a reminder of the last guess.

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

    #. Complete the code for teh check_guess function.

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
