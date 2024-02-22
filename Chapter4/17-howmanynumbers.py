# DictDiff
#  - Create a function how_many_different_numbers
#    - Should take a list of integers of arbitrary length
#    - Should output how many different integers are present

def how_many_different_numbers(numbers_list):
    unique_numbers = set()
    for num in numbers_list:
        if num not in unique_numbers:
            unique_numbers.add(num)

    # Could have been done as unique_numbers = set(numbers_list)
    # Set will only have one of each
        
    return print(f'The list {numbers_list} contains {len(unique_numbers)} unique numbers.')

if __name__ == '__main__':
    dict1 = [1, 2, 3, 1, 2, 3, 4, 1]
    how_many_different_numbers(dict1)

    dict2 = [1, 2, 3, 1, 2, 3, 4, 1, 5, 5, 10, 13, 23, 1111]
    how_many_different_numbers(dict2)