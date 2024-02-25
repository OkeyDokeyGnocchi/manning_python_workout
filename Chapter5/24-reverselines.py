# Reverse Lines
#  - Create a reverse_lines()
#    - Should take two arguments
#      - input_file with lines to reverse
#      - output_file which writes output of reversed input
#    - Should create a file with reversed input (except "\n"s)

import os

def reverse_lines(input_file, output_file):
    with open(input_file, 'r') as inf, open(output_file, 'w') as outf:
        for line in inf:
            outf.write(f"{line.rstrip()[::-1]}\n")

if __name__ == '__main__':
    working_dir = os.path.dirname(__file__)
    input_file = working_dir + "/24-input.txt"
    output_file = working_dir + "/24-output.txt"

    reverse_lines(input_file, output_file)