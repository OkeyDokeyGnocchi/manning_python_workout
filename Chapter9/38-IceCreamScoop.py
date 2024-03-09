# Ice Cream Scoop
#  - Create a class Scoop
#  - Represents a single scoop of ice cream
#    - Should have a single attr.: flavor (string)
#  - Create a function create_scoops()
#    - Should create 3 instances of Scoop
#    - Each should be a different flavor
#  - Put the scoops in list scoops[]
#    - Iterate over scoops[] && print the flavors

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops(flavors=["Chocolate", "Vanilla", "Strawberry"]):
    return [Scoop(flavor) for flavor in flavors]

# Create class Beverage for beyond the exercise
#  - Should have two attr.: Name and Temperature
#    - If Temp isn't specified, it should default to 75 degrees

class Beverage():
    def __init__(self, name, temp=75):
        self.name = name
        self.temp = temp
    
    def bev_info(self):
        return print(f'{self.name} is served at {self.temp} degrees')


if __name__ == '__main__':
    scoops = create_scoops()
    for scoop in scoops:
        print(scoop.flavor)
    
    scoops2 = create_scoops(["Rocky Road", "Mint Chip", "Cookie Dough", "Birthday Cake"])
    for scoop in scoops2:
        print(scoop.flavor)

    water = Beverage("water", 50)
    coffee = Beverage("coffee")
    tea = Beverage("tea", 65)
    water.bev_info()
    coffee.bev_info()
    tea.bev_info()