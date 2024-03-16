# Zoo
#  - Builds on 44-Cages
#  - Create class Zoo
#    - Should be able to add arbitary number of cages
#    - Should be able to print (__repr__) and provide all cages with ID and animals inside
#    - Should have 3 additional methods
#      - animals_by_color(color) should return list of Animal objects with color 'color'
#      - animals_by_legs(num_legs) should return list of Animal objects with num_legs
#      - number_of_legs() should get total number of legs of animals @ zoo for socks

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
    
    def remove_animals(self, *animals):
        for one_animal in animals:
            self.animals.remove(one_animal)
            self.free_space += one_animal.space_required
                

    def __repr__(self):
        # Defining this because python < 3.12 can't do '\' in {} for f-string
        animal_newlines = "\n".join(str(animal) for animal in self.animals)
        return f'Cage {self.id} has {self.free_space} meters left.  Currently houses:\n{animal_newlines}\n'

class Zoo():
    def __init__(self, name):
        self.name = name
        self.cages = []
    
    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)
    
    def animals_by_color(self, *colors):
        # Returned after first pass b/c book mentioned list comp
        # So worked out list comp instead of nested statements
        """
        animal_list = []
        for cage in self.cages:
            for animal in cage.animals:
                if animal.color == color:
                    animal_list.append(animal)
        
        return f'The following animals are the color {color}:\n{animal_list}'
        """
        if not colors:
            raise Exception("No colors were passed!")
        return [animal for cage in self.cages
                for animal in cage.animals
                for color in colors
                if animal.color == color]
    
    def animals_by_legs(self, legs):
        return [animal for cage in self.cages
                for animal in cage.animals
                if animal.num_legs == int(legs)]
    
    def number_of_legs(self):
        return sum(animal.num_legs for cage in self.cages
                   for animal in cage.animals)

    def __repr__(self):
        # Same issue as above, f-string doesn't play nicely with {\}
        cage_newlines = "\n".join(str(cage) for cage in self.cages)
        return f'{self.name} has the following:\n\n{cage_newlines}'


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
    snake_1 = Snake("white")
    snake_2 = Snake("purple")
    parrot_1 = Parrot("red")

    cage_1 = Cage(1)
    cage_1.add_animals(sheep_1, sheep_2, parrot_1)
    cage_2 = Cage(2)
    cage_2.add_animals(snake_1, wolf_1)

    z1 = Zoo("City Zoo")
    z1.add_cages(cage_1, cage_2)
    print(z1)
    print(z1.animals_by_color("white"))
    print(z1.animals_by_legs(4))
    print(z1.number_of_legs())
    
    # Optional exercise additions
    #print(z.animals_by_color())
    print(z1.animals_by_color("white", "brown"))
    print()
