# Circle
#  - Create a class Circle()
#    - Should function like enumerate
#    - Takes two arguments:
#      - Iterable
#      - Number of elements to return
#    - Should print elements from iterable until num_elements
#      - Should repeat and loop as necessary if number > len(iterable)

class Circle():
    def __init__(self, iterable, num_elements):
        self.iterable = iterable
        self.num_elements = num_elements
    
    def __iter__(self):
        return CircleIterator(self.iterable, self.num_elements)

class CircleIterator(Circle):
    def __init__(self, iterable, num_elements):
        self.iterable = iterable
        self.num_elements = num_elements
        self.index = 0
    
    def __next__(self): 
        if self.index >= self.num_elements:
            raise StopIteration
        else:
            val = self.iterable[self.index % len(self.iterable)]
            self.index += 1
            return val

def circle_gen(iterable, num_elem):
    idx = 0
    while idx < num_elem:
        yield iterable[idx % len(iterable)]
        idx += 1


if __name__ == '__main__':
    c1 = Circle('abc', 5)
    print(list(c1))

    # Optional exercise
    for v in circle_gen('abc', 5):
        print(v)