# Summing Anything
#  - Create a function mysum()
#  - Should take an arbitrary number of elements of the same type
#  - Should return the arguments summed "+"

def mysum(*args):
    if not args:
        return print("Object list was empty.")
    else:
        result = args[0]
        for arg in args[1:]:
            result += arg
    
    return print(f'{result}')

def mysum_bigger_than(threshold, *args):
    # Take in arbitrary number of arguments
    # Return "+" of all that are > the args[0]
    started_summing = False
    for arg in args:
        if arg > threshold:
            if started_summing:
                result += arg
            else:
                started_summing = True
                result = arg
    
    return print(f'{result}')
    
if __name__ == '__main__':
    mysum()
    mysum('abc', 'def')
    mysum([1,2,3], [4,5,6])
    mysum(1,2,3)

    mysum_bigger_than(10, 5, 20, 30, 6)
    mysum_bigger_than('c', 'a', 'd', 'b', 'e')