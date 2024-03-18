# Elapsed Since
#  - Create a generator function
#    - Takes one argument:
#      - Iterable
#    - Should yield tuple: (int(seconds_since_last_iter), iterable_element)
#    - Recommended to use time.perf_counter()

import random
import time

def elapsed_since_gen(iterable):
    last_time = 0
    for item in iterable:
        item_time = time.perf_counter()
        time_change = item_time - last_time
        last_time = time.perf_counter()
        yield (time_change, item)

# Optionals
def elapsed_since_gen_mk2(iterable, min_sleep):
    last_time = 0
    for item in iterable:
        item_time = time.perf_counter()
        time_change = item_time - last_time
        if time_change < min_sleep:
            time.sleep(min_sleep - time_change)
            item_time = time.perf_counter()
        time_change = item_time - last_time
        last_time = time.perf_counter()
        yield (time_change, item)
        

if __name__ == '__main__':
    """
    for char in elapsed_since_gen('abcdefg'):
        print(char)
        sleep_time = random.randint(0, 3)
        time.sleep(sleep_time)
    """
    
    # Optionals
    for char in elapsed_since_gen_mk2('123456', 3):
        print(char)
        sleep_time = random.randint(2, 6)
        time.sleep(sleep_time)