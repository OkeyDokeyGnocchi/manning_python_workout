# Created for exercise 37 - Menu
#  - Should provide a function menu()
#    - Takes any number of arguments:
#      - Arguments should be key-val pairs
#      - Values should be callable
#      - When invoked, should ask user to enter input
#        - If input is a keyword argument in menu() it should return the value
#        - If input is not a keyword arg it should error and ask user to try again

def menu(**kwargs):
    while True:
        menu_options = ", ".join(kwargs)
        user_input = input(f'Please select your menu option: {menu_options}\n')
        if user_input in kwargs:
            return kwargs[user_input]()
        else:
            print(f'{user_input} was not found in options list for this menu. Please enter a valid menu option.\n')