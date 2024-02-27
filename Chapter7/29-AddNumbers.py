# Add Numbers
#  - Create a function sum_numbers()
#    - Takes a string from input()
#    - Returns the sum of all found integers in string.split()

import os

def sum_numbers():
    input_string = input("Please enter the string for parsing: \n")
    return sum(int(num) for num in input_string.split() if num.isdigit())


if __name__ == '__main__':
    print(sum_numbers())