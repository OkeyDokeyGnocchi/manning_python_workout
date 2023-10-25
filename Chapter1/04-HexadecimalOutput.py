# Hexadecimal Output
# Create a function hex_output
#  - Should take in numbers that are assumed to be hexadecimal
#  - Should return the decimal equivalent
## Name Triangle
## Create a function name_triangle
##  - Should take in user's name
##  - Should use 1 letter, 2 letters, etc. until full name is printed on the bottom line

def hex_output():
    decimal_number = 0
    hex_number = input("Please enter hex number without '0x': ")

    for i, c in enumerate(reversed(hex_number)):
        # Second location in the int() function is the base, 16 for hex
        decimal_number += int(c, 16) * (16 ** i)
    
    print(decimal_number)

def name_pyramid():
    name = input("Please enter your name: ")

    for i, c in enumerate(name):
        # Slicing stop is stop indicator - 1
        print(f"{name[:i+1]}")

if __name__ == "__main__":
#    hex_output()
    name_pyramid()