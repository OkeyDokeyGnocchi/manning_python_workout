# Ice Cream Bowl
#  - Builds on 38-IceCreamScoop
#  - Represents a bowl which contains instances of Scoop()
#    - Should have function add_scoops()
#      - Should allow user to add scoops to the bowl

class Bowl():
    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *scoops):
        for scoop in scoops:
            self.scoops.append(scoop)
    
    def __repr__(self):
        return ', '.join(scoop.flavor for scoop in self.scoops)

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops(flavors=["Chocolate", "Vanilla", "Strawberry"]):
    return [Scoop(flavor) for flavor in flavors]

# Beyond Exercise: Books and Shelves
#  - Class Book()
#    - Has title, author, price
#  - Class Shelf()
#    - Contains Books
#    - Has a function total_price()
#      - Gets total price of books on the Shelf

class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Shelf():
    def __init__(self):
        self.books = []
    
    def add_books(self, *books):
        for book in books:
            self.books.append(book)

    def total_price(self):
        return print(f'The total price for this bookshelf is: ${sum(book.price for book in self.books)}')
    
    def __repr__(self):
        return ", ".join(book.title for book in self.books)

if __name__ == '__main__':
    scoops = create_scoops()
    b = Bowl()
    for scoop in scoops:
        b.add_scoops(scoop)
    print(f'The bowl of ice cream contains: {b}')
    print()

    book1 = Book("Frankenstein", "Mary Shelley", 10.99)
    book2 = Book("The Ultimate Hitchiker's Guide to the Galaxy", "Douglas Adams", 39.99)
    book3 = Book("The Foundation Trilogy", "Isaac Asimov", 40.00)
    books = [book1, book2, book3]

    bookshelf = Shelf()
    for book in books:
        bookshelf.add_books(book)
    print(bookshelf)
    bookshelf.total_price()