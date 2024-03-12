# Animals
#  - Create a class of Animal and subclasses for a zoo
#    - All objects instances should have num_legs, species, and color
#    - Subclasses: Sheep, Wolves, Snakes, Parrots
#    - Should be able to print (__repr__) and have it produce a string of attributes

from random import choice

class Animal():
    num_legs = 4
    def __init__(self, color):
        self.color = color
    
    def __repr__(self):
        return f'This {self.species} has {self.num_legs} legs and is {self.color}'

class Sheep(Animal):
    species = "sheep"

class Wolf(Animal):
    species = "wolf"

class Snake(Animal):
    species = "snake"
    num_legs = 0

class Parrot(Animal):
    species = "parrot"
    num_legs = 2

def create_one_animal(animal_class, color):
    return animal_class(color)

def create_zoo_animals(num_each_animal=1):
    colors = [
        "white",
        "grey",
        "brown",
        "green",
        "red",
        "orange"
    ]
    animals = [
        Sheep,
        Wolf,
        Snake,
        Parrot
    ]
    zoo_animals = []

    # List comprehension feels a little less straightfoward to read, but it's good practice for using them
    return [create_one_animal(animal, choice(colors)) for animal in animals for i in range(num_each_animal)]
"""
    for animal in animals:
        for i in range(num_each_animal):
            zoo_animals.append(create_one_animal(animal, choice(colors)))
    
    return zoo_animals
"""


if __name__ == '__main__':
    sheep_1 = Sheep("white")
    wolf_1 = Wolf("grey")
    snake_1 = Snake("green")
    parrot_1 = Parrot("red")

    animal_list = create_zoo_animals(2)
    for animal in animal_list:
        print(animal)