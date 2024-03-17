# All Lines All Files
#  - Create a generator function all_lines()
#    - Takes one argument:
#      - Directory
#    - Should yield line for line in file for all files in directory

import os

def all_lines(walk_dir):
    for finding in os.walk(walk_dir):
        for file in finding[2]:
            try:
                with open(walk_dir + "/" + file) as f:
                        for line in f:
                            # Added .strip() to stop all the newlines
                            yield line.strip()
            except OsError:
                pass


if __name__ == '__main__':
    file_dir = os.path.dirname(__file__)
    walk_dir = file_dir + "/files"
    for line in all_lines(walk_dir):
         print(line)