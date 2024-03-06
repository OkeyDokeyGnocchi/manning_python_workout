# Gematria Pt. 1
#  - Create a function gematria_dict()
#    - No input
#    - Returns a dict where 'a':1, 'b':2, etc.
# Gematria Pt. 2
#  - Create two new functions
#    - gematria_for()
#      - Takes a string (single word)
#      - Returns the gematria score for the word
#    - gematria_equal_words()
#      - Takes a string (single word)
#      - Returns a list of dict words with a matching gematria score

import os
import string

def gematria_dict(starting_num=1):
    return {key:val for val, key in enumerate(string.ascii_lowercase, starting_num)}

GEMATRIA_DICT = gematria_dict()

def config_dict(in_file):
    return {key:val for line in open(in_file) for key, val in zip(line.split("=")[0], line.split("=")[1])}

def gematria_for(word):
    # That default of 0 is required
    return sum(GEMATRIA_DICT.get(letter, 0) for letter in word.lower())

def gematria_equal_words(word, dictionary):
    word_score = gematria_for(word)
    return [select_word.strip() for select_word in open(dictionary) if gematria_for(select_word.lower()) == word_score]

if __name__ == '__main__':
    #print(gematria_dict())
    #print(gematria_dict(21))

    # Optional add-on for splitting input config file
    #working_dir = os.path.dirname(__file__)
    #input_file = working_dir + "/35-config.txt"
    #print(config_dict(input_file))

    working_dir = os.path.dirname(__file__)
    words_dict = working_dir + "/words_dict.txt"
    word = "cat"
    print(gematria_for(word))
    print(gematria_equal_words(word, words_dict))