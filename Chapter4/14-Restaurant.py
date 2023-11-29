# Restaurant
#  - Create a constant dict MENU
#    - Should represent items at a restaurant MENU['Item'] = {'Item':int(Price)}
#  - Create function restaurant()
#    - Should allow the user to enter item to order and record running tally of items and cost
#    - Should re-prompt for more items
#    - Should not allow ordering of items not on the menu, just warning message and reprompt
#    - Empty string to quit. Print total amount

MENU = {
    'sandwich':10,
    'pizza':15,
    'tea':5,
    'soda':5,
    'water':0
}

def restaurant():
    order_total = 0
    items_ordered = []

    while True:
        cust_request = input("Order: ").strip()
        if not cust_request:
            break
        elif cust_request not in MENU:
            print(f"I'm sorry, we don't have {cust_request}")
        else:
            order_total += MENU[cust_request]
            items_ordered.append(cust_request)
            print(f"{cust_request} costs ${MENU[cust_request]}. Your current total is ${order_total}")
    
    return print(f"Your total is ${order_total} for {', '.join(items_ordered)}")


# Define simple example login system using dict of usernames and passwords
USERS = {
    'admin':'admin123',
    'someguy':'password'
}

def login_sys():
    while True:
        username = input("Username: ").strip()

        if username in USERS:
            if test_password(username):
                return print(f"Login for {username} successful!")

def test_password(username):
    login_attempts = 0
    while True:
        password = input("Password: ")
        login_attempts += 1

        if password == USERS[username]:
            return True
        else:
            if login_attempts == 3:
                print("Incorrect user/password.")
                return False
        



if __name__ == '__main__':
    #restaurant()
    login_sys()