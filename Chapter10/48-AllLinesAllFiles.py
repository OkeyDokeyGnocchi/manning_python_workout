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
            except OSError:
                pass

def all_lines_modded(walk_dir, find_string=''):
    # Trying a different method to get files
    for dir, subdir, files in os.walk(walk_dir):
        for file_idx, file in enumerate(files):
            try:
                with open(os.path.join(walk_dir, file)) as f:
                    for line_idx, line in enumerate(f):
                        if str(find_string) in line:
                            yield (file, file_idx, line_idx, line)
                        line_idx += 1
            except OSError:
                pass

if __name__ == '__main__':
    file_dir = os.path.dirname(__file__)
    walk_dir = file_dir + "/files"
    for line in all_lines(walk_dir):
        print(line)
    
    # Optionals
    print()
    for line in all_lines_modded(walk_dir):
        print(line)
    print("## Modded with find_string ##")
    for line in all_lines_modded(walk_dir, 1):
        print(line)