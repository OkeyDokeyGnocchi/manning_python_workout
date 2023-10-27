# Pig Latin
# Create a function pig_latin()
#  - Should take in an assumed English word (lowercase only)
#  - Should return the pig latin translation of the word

def pig_latin():
    word = input("Please enter an English word to translate: ")

    # Per the solution, the joins could have instead been f strings
    # e.g., f'{word[1:]}{word[0]ay}'
    if word.lower()[0] in "aeiou":
        print("w".join([word, "ay"]))
    else:
        print("".join([word[1:], word[0], "ay"]))


if __name__ == '__main__':
    pig_latin()