# pet store


from microbit import *
import random

# Built-in animals
animal_icons = {
    "Cow": Image.COW,
    "Duck": Image.DUCK,
    "Giraffe": Image.GIRAFFE,
    "Rabbit": Image.RABBIT,
    "Snake": Image.SNAKE,
}

animals = list(animal_icons.keys())

pet_names = {
    "Cow": ["Daisy", "MooMoo",],
    "Duck": ["Quacker", "Daffy", "Waddles",],
    "Giraffe": ["Stretch", "Lofty"],
    "Rabbit": ["Hoppy", "Bunny", "Bugsy"],
    "Snake": ["Slither", "Fang", "Slinky"],
}

current_animal = None

while True:
    if button_a.was_pressed():
        current_animal = random.choice(animals)
        display.show(animal_icons[current_animal])

    if button_b.was_pressed():
        if current_animal:
            name = random.choice(pet_names[current_animal])
            display.scroll(name + " the " + current_animal)
        else:
            display.scroll("Pick animal first")

    sleep(100)
