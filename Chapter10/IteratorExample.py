# Iterator Example
#  - Not an exercise
#  - Just following the example for practice

class ExampleIterator():
    # Added tabs to match example in the book
    def __init__(self, data):
        print('\tIn __init__')
        self.data = data
        self.index = 0

    def __iter__(self):
        print('\tIn __iter__')
        return(self)

    def __next__(self):
        print('\tIn __next__')
        if self.index < len(self.data):
            val = self.data[self.index]
            print(f'Current index {self.index} is less than length of self.data, return {val}')
            self.index += 1
            return val
        else:
            print(f'Current index {self.index} greater than length of self.data, raise StopIteration')
            raise StopIteration
        

if __name__ == '__main__':
    example = ExampleIterator([1, '2', 'c'])
    for item in example:
        print(item)