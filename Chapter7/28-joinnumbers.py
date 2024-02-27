# Join Numbers
#  - Create a function join_numbers()
#    - Takes a range of integers
#    - Returns them as a string with commas between numbers

def join_numbers(int_range):
    # The extra space wasn't requested, but I like it
    return ', '.join([str(num) for num in int_range])

def join_numbers_under(int_range, max_num=10):
    return ', '.join([str(num) for num in int_range if num <= max_num])

if __name__ == '__main__':
    print(join_numbers(range(15))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
    print(join_numbers_under(range(15), 12)) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    print(join_numbers_under(range(15))) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10