# Gematria Pt. 1
#  - Create a function gematria_dict()
#    - No input
#    - Returns a dict where 'a':1, 'b':2, etc.

import os
import string

def gematria_dict(starting_num=1):
    return {key:val for key, val in enumerate(string.ascii_lowercase, starting_num)}

def config_dict(in_file):
    return {key:val for line in open(input_file) for key, val in zip(line.split("=")[0], line.split("=")[1])}


if __name__ == '__main__':
    print(gematria_dict())
    print(gematria_dict(21))

    working_dir = os.path.dirname(__file__)
    input_file = working_dir + "/35-config.txt"
    print(config_dict(input_file))