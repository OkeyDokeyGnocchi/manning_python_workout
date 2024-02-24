# Word count
#  - Create a function wordcount
#    - Should take a txt file
#    - Should return four lines of output:
#      - Number of characters (incl. whitespace)
#      - Number of words (sep. by whitespace)
#      - Number of lines
#      - Number of unique words

import os

def wordcount(file):
    counts = {
        "char": 0,
        "words": 0,
        "lines": 0
    }
    uniq_words = set()
    with open(file) as f:
        for line in f:
            counts["char"] += len(line)
            counts["words"] += len(line.split())
            counts["lines"] += 1
            uniq_words.update(line.split())
    
    return print(f"Characters: {counts['char']}\nWords: {counts['words']}\nLines: {counts['lines']}\nUnique Words: {len(uniq_words)}")



if __name__ == '__main__':
    text_file = os.path.dirname(__file__) + "/wcfile.txt"
    wordcount(text_file)