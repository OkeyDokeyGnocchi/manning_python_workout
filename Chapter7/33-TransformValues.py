# Transform Values
#  - Create a function transform_values()
#    - Takes a function and dict as inputs
#    - Returns a dict with key:func(val)

def transform_values(func1, input_dict):
    def check_even(k, v):
        if v % 2 == 0:
            return True
        elif k == 'c':
            return True
        
        return False
    
    return {key:func1(val) for key,val in input_dict.items() if check_even(key, func1(val)) == True}
    

if __name__ == '__main__':
    in_dict = {'a':1, 'b':2, 'c':3}
    print(transform_values(lambda x: x*x, in_dict))
    print(transform_values(lambda x: x-1, in_dict))