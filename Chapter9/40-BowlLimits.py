# Bowl Limits
#  - Builds on 39-IceCreamBowl
#  - Add a limitation constant to bowl
#    - Should allow user to add <= 3 scoops to the bowl via add_scoops()
#    - Should ignore any scoops beyond max of 3

class Bowl():
    SCOOP_LIMIT = 3
    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.scoops) < Bowl.SCOOP_LIMIT:
                self.scoops.append(scoop)
            else:
                return print(f"This bowl is already full, can't add a scoop of {scoop.flavor}!")
    
    def __repr__(self):
        return ', '.join(scoop.flavor for scoop in self.scoops)

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops(flavors=["Chocolate", "Vanilla", "Strawberry"]):
    return [Scoop(flavor) for flavor in flavors]


if __name__ == '__main__':
    scoops = create_scoops()
    b = Bowl()
    for scoop in scoops:
        b.add_scoops(scoop)
    print(f'The bowl of ice cream contains: {b}')
    mint_chip = Scoop("Mint chip")
    b.add_scoops(mint_chip)
    print(f'The bowl of ice cream contains: {b}')
