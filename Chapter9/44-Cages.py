# Animals
#  - Builds on 43-Animals
#  - Create class Cage
#    - Should pass an ID for Cage (e.g. Cage(1))
#    - Should be able to add arbitary number of animals
#    - Should be able to print (__repr__) and have it produce a string with cage ID and animals in cage

class Animal():
    def __init__(self, color, num_legs):
        self.color = color
        self.species = self.__class__.__name__
        self.num_legs = num_legs
    
    def __repr__(self):
        return f'{self.species}: {self.num_legs} legs, {self.color}'

class Sheep(Animal):
    space_required = 10
    def __init__(self, color):
        super().__init__(color, 4)

class Wolf(Animal):
    space_required = 15
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    space_required = 5
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    space_required = 10
    def __init__(self, color):
        super().__init__(color, 2)

class Cage():
    def __init__(self, id):
        self.id = id
        self.animals = []
        self.free_space = 30
    
    def add_animals(self, *animals):
        for new_animal in animals:
            # Ensure that the new animal doesn't need more space than the cage has
            if new_animal.space_required > self.free_space:
                raise Exception(f"There's only {self.free_space} meters in this cage. {new_animal.species} requires {new_animal.space_required}!")
            # If we have some animals, verify that they can cooperate
            if self.animals:
                for existing_animal in self.animals:
                    if type(new_animal) not in animal_compatibility[type(existing_animal)]:
                        raise Exception(f"You can't put {type(new_animal).__name__} in with {type(existing_animal).__name__}!")

            self.animals.append(new_animal)
            self.free_space -= new_animal.space_required
                

    def __repr__(self):
        # Defining this because python < 3.12 can't do '\' in {} for f-string
        animal_newlines = "\n".join(str(animal) for animal in self.animals)
        return f'Cage {self.id} has {self.free_space} meters left.  Currently houses:\n{animal_newlines}\n'

if __name__ == '__main__':
    animal_compatibility = {
        Sheep: [Sheep, Parrot],
        Wolf: [Wolf, Snake],
        Snake: [Snake, Wolf],
        Parrot: [Parrot, Sheep]
    }
        
    sheep_1 = Sheep("white")
    sheep_2 = Sheep("brown")
    wolf_1 = Wolf("grey")
    snake_1 = Snake("green")
    snake_2 = Snake("purple")
    parrot_1 = Parrot("red")

    cage_1 = Cage(1)
    #cage_1.add_animals(sheep_1, wolf_1)  This raises an exception b/c wolf+sheep is no-go!
    cage_1.add_animals(sheep_1, parrot_1)
    print(cage_1)
    cage_2 = Cage(2)
    #cage_2.add_animals(snake_1, parrot_1)  This raises an exception b/c snake+parrot is no-go!
    cage_2.add_animals(snake_1, wolf_1)
    print(cage_2)

    cage_1.add_animals(sheep_2)
    print(cage_1)
    # This fails to whichever Exception is thrown first since it's over the size and species compat
    cage_1.add_animals(snake_2)