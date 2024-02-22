# FinalLine
#  - Create a function get_final_line
#    - Should take a filename
#    - Should output the file's final line

import os

def get_final_line(file):
    with open(file) as f:
        for line in f:
            current_line = line
    
    return print(current_line)


if __name__ == '__main__':
    execution_dir = os.path.dirname(__file__)
    get_final_line(execution_dir + "/finalLine-input1.txt")
    get_final_line(execution_dir + "/finalLine-input2.txt")