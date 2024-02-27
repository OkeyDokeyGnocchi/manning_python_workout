# Prefix Notation Calculator
#  - Create a function calc()
#    - Should take a string with operator and two numbers
#    - Should use defined functions for the following:
#      - +, -, *, /, %, **
#    - Should return the solution

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def exp(a, b):
    return a ** b

def calc(input_string):
    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide,
        "%" : modulus,
        "**" : exp
    }
    # Can use maxsplit option to set max elements to 3 individual + one combination
    string_components = input_string.split()
    operation = string_components[0]
    a, b = int(string_components[1]), int(string_components[2])
    return operations[operation](a, b)

"""
Per the solution, we could also implement without defining the functions for each as originally asked, e.g.,

import operator

def calc(input_string):
  operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    etc.
  }

  operator, a, b = input_string.split(maxsplit=3)
  a, b = int(a), int(b)
  
  return operations[operator](a, b)
"""

if __name__ == '__main__':
    add_string = "+ 2 3"
    subtract_string = "- 5 2"
    divide_string = "/ 10 3"
    exp_string = "** 2 3"
    print(calc(add_string))
    print(calc(subtract_string))
    print(calc(divide_string))
    print(calc(exp_string))