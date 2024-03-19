# My Chain
#  - Create a generator function mychain()
#  - Should work like itertools chain
#    - Should take arbitrary inputs (iterables)
#    - Should iterate through iterables and return each element

def mychain(*args):
    for iterable in args:
        for item in iterable:
            yield item


if __name__ == '__main__':
    for item in mychain('abc', [1,2,3], {'a':1, 'b':2}):
        print(item)