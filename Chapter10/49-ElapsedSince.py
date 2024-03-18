# Elapsed Since
#  - Create a generator function
#    - Takes one argument:
#      - Iterable
#    - Should yield tuple: (int(seconds_since_last_iter), iterable_element)
#    - Recommended to use time.perf_counter()

import os
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
# Minimum sleep timer
#  - Add a minimum sleep timer to elapsed_since
#    - Should sleep if time elapsed < min_sleep
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

# File usage timing function
#  - For file in directory:
#    - Should give access time, mod time, creation time
def file_usage_timing(directory):
    for file in os.listdir(directory):
        filename = os.path.join(directory, file)
        try:
            stats = os.stat(filename)
            atime, mtime, ctime = stats.st_atime, stats.st_mtime, stats.st_ctime
            yield f'{filename}:\nAccess Time: {atime}, Mod Time: {mtime}, Creation Time: {ctime}\n'
        except OSError:
            pass


if __name__ == '__main__':
    """
    for char in elapsed_since_gen('abcdefg'):
        print(char)
        sleep_time = random.randint(0, 3)
        time.sleep(sleep_time)
    """
    
    # Optionals
    # Minimum sleep elapsed_since_gen
    """
    for char in elapsed_since_gen_mk2('123456', 3):
        print(char)
        sleep_time = random.randint(2, 6)
        time.sleep(sleep_time)
    """

    # file_usage_timing
    directory = os.path.dirname(__file__) + "/files"
    for file in file_usage_timing(directory):
        print(file)