# My Enumerate
#  - Create a class MyEnumerate()
#    - Should function like enumerate
#    - Given elements:
#      - for loop should return index and element

class MyEnumerate():
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.iterable):
            val = self.iterable[self.index]
            idx = self.index
            self.index += 1
            return (idx, val)
        else:
            raise StopIteration
        

if __name__ == '__main__':
    myEnum = MyEnumerate('abc')
    for idx, val in myEnum:
        print(f'{idx}: {val}')