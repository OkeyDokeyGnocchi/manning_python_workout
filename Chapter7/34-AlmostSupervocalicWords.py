# (Almost) Supervocalic Words
#  - Create a function get_sv()
#    - Takes a file full of words to check as inputs
#    - Returns a set of words are (almost) supervocalic
#      - This is words that have 'aeiou' in order in them, only once each
#      - This function just checks words have all 5 vowels

import os

VOWELS = {'a', 'e', 'i', 'o', 'u'}

def get_sv(in_file):
    # Needs to have .strip() b/c they keep the \n char
    return {word.strip() for word in open(in_file) if VOWELS < set(word.lower())}

if __name__ == '__main__':
    working_dir = os.path.dirname(__file__)
    input_file = working_dir + "/34-input.txt"
    print(get_sv(input_file))