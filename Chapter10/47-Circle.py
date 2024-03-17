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

# Circle generator function
def circle_gen(iterable, num_elem):
    idx = 0
    while idx < num_elem:
        yield iterable[idx % len(iterable)]
        idx += 1

# MyRange class
class MyRange():
    def __init__(self, start, stop, step=1):
        if start == None:
            self.start, self.stop = 0, stop
        else:
            self.start, self.stop = start, stop
        self.step = step
    
    def __iter__(self):
        return MyRangeIterator(self.start, self.stop, self.step)

class MyRangeIterator(MyRange):
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = self.start
    
    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        else:
            val = self.current
            self.current += self.step
            return val

    

if __name__ == '__main__':
    c1 = Circle('abc', 5)
    print(list(c1))

    # Optional exercise
    for v in circle_gen('abc', 5):
        print(v)

    print("\n## Range(1,3) ##")
    for i in range(1, 3):
        print(i)
    for i in MyRange(1, 3):
        print(i)
    
    print("## Range(2, 10, 2) ##")
    for i in range(2, 10, 2):
        print(i)
    for i in MyRange(2, 10, 2):
        print(i)
    
    print('## Range(10, 2, -2)')
    for i in range(10, 2, -2):
        print(i)
    for i in MyRange(10, 2, -2):
        print(i)