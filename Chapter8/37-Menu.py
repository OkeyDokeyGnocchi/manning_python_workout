# Menu
#  - Create a module menu.py
#  - All functions and supporting data should be in menu.py

from menu import menu

def func_a():
    return "A"

def func_b():
    return "B"

if __name__ == '__main__':
    print(menu(a=func_a, b=func_b))