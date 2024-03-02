# Flatten a List
#  - Create a function flatten()
#    - Takes a list of lists
#    - Returns a single list made of the contents of input lists

def flatten(input_list):
    return [item for inner_list in input_list for item in inner_list]

if __name__ == '__main__':
    print(flatten([[1,2], [3,4]]))