# Pig Latin Translation of a File
#  - Create a function plfile()
#    - Takes a txt file as input
#    - Returns the input as Pig Latin

import os

def plword(word):
    if word.lower()[0] in "aeiou":
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'

def plfile(in_file):
    return ' '.join(plword(word) for line in open(input_file) for word in line.split())


if __name__ == '__main__':
    working_dir = os.path.dirname(__file__)
    input_file = working_dir + "/31-input.txt"
    print(plfile(input_file))