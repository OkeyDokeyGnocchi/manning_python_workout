# Flip a Dictionary
#  - Create a function flipped_dict()
#    - Takes a dict as input
#    - Returns a dict with the key:value pairs flipped
#      - {'a':1, 'b':2} -> {1:'a', 2:'b'}

def flipped_dict(input_dict):
    return {val:key for key,val in input_dict.items()}


if __name__ == '__main__':
    input_dict = {'a':1, 'b':2, 'c':3}
    print(flipped_dict(input_dict))