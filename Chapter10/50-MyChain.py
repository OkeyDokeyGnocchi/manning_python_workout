# My Chain
#  - Create a generator function mychain()
#  - Should work like itertools chain
#    - Should take arbitrary inputs (iterables)
#    - Should iterate through iterables and return each element

def mychain(*args):
    for iterable in args:
        for item in iterable:
            yield item

# Beyond the exercise
# Recreate zip()
def myzip(first_iterable, second_iterable):
    # Should only go for length of the shorter of the two inputs
    if len(first_iterable) > len(second_iterable):
        iter_size = len(second_iterable)
    else:
        iter_size = len(first_iterable)
    for i in range(iter_size):
        yield (first_iterable[i], second_iterable[i])


if __name__ == '__main__':
    for item in mychain('abc', [1,2,3], {'a':1, 'b':2}):
        print(item)
    
    # myzip
    for pair in myzip('abc', [1,2,3]):
        print(pair)
    for pair in myzip('cba', [1,2]):
        print(pair)
    for pair in myzip('def', [5,6,7,8]):
        print(pair)