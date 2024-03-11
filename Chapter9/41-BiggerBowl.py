# Bigger Bowl
#  - Builds on 40-BowlLimits
#  - Create a new class BigBowl()
#    - Should allow user to add <= 5 scoops to the bowl via add_scoops()
#    - Should ignore any scoops beyond max of 5
#    - Should inherit from Bowl

class Bowl():
    SCOOP_LIMIT = 3
    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *scoops):
        for scoop in scoops:
            if len(self.scoops) < self.SCOOP_LIMIT:
                self.scoops.append(scoop)
            else:
                return print(f"This bowl is already full, can't add a scoop of {scoop.flavor}!")
    
    def __repr__(self):
        return ', '.join(scoop.flavor for scoop in self.scoops)

class BigBowl(Bowl):
    SCOOP_LIMIT = 5

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
    
    bb = BigBowl()
    for scoop in scoops:
        bb.add_scoops(scoop)
    rainbow_sherbet = Scoop("Rainbow sherbet")
    too_many_scoops = Scoop("Rum raisin")
    bb.add_scoops(mint_chip, rainbow_sherbet, too_many_scoops)
    print(f'The big bowl of ice cream contains: {bb}')