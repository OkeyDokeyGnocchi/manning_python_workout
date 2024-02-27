# Password Generator
#  - Create a function create_password_generator()
#    - Should take a string of allowed characters
#    - Should be able to generate different password functions
#      - alpha_password = create_password_generator('abcdef')
#      - print(alpha_password(5))    # efeaa
#    - Should return the solution

from random import choice

def create_password_generator(char_string):
    def password_generator(pass_length):
        password = ""
        for i in range(pass_length):
            password += choice(char_string)

        return password
    
    return password_generator

if __name__ == '__main__':
    alpha_password = create_password_generator('abcdef')
    symbol_password = create_password_generator('!@#$%')
    
    print(alpha_password(5))
    print(alpha_password(10))

    print(symbol_password(5))
    print(symbol_password(10))