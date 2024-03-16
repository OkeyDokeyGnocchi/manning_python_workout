# My Enumerate
#  - Create a class MyEnumerate()
#    - Should function like enumerate
#    - Given elements:
#      - for loop should return index and element

class MyEnumerate():
    def __init__(self, iterable, user_idx=0):
        self.iterable = iterable
        self.user_idx = user_idx
    
    def __iter__(self):
        return MyEnumerateIterator(self.iterable, self.user_idx)
    
    def __next__(self):
        if self.index < len(self.iterable):
            val = self.iterable[self.index]
            idx = self.user_idx
            self.index += 1
            self.user_idx += 1
            return (idx, val)
        else:
            raise StopIteration

class MyEnumerateIterator(MyEnumerate):
    def __init__(self, iterable, user_idx):
        self.iterable = iterable
        self.index = 0
        self.user_idx = user_idx
    
    def __iter__(self):
        return self


        
# Generator function
def MyEnumerateGen(iterable, start_idx=0):
    idx, user_idx = 0, start_idx

    while idx < len(iterable):
        yield user_idx, iterable[idx]
        idx += 1
        user_idx += 1


if __name__ == '__main__':
    myEnum = MyEnumerate('abc')
    for idx, val in myEnum:
        print(f'{idx}: {val}')
    for idx, val in myEnum:
        print(f'{idx}: {val}')
    
    # Optionals
    print()
    myEnumIdx = MyEnumerate('efg', 2)
    for idx, val in myEnumIdx:
        print(f'{idx}: {val}')

    print()
    for idx, val in MyEnumerateGen('abcd', 2):
        print(f'{idx}: {val}')
