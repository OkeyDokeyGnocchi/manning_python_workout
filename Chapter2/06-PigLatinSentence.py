# Pig Latin
# Create a function pl_sentence()
#  - Should take in an assumed English sentence (lowercase only)
#  - Should return the pig latin translation of the sentence

def pig_latin(word):
    # Translate the word into pig latin
    if word.lower()[0] in "aeiou":
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'

def pl_sentence():
    # Get the user's input and create a blank list to break the sentence into
    sentence = input("Please provide sentence to translate: ")
    sentence_list = []

    # For each word in the split sentence, pig-latin-ify it
    for word in sentence.split():
        sentence_list.append(pig_latin(word))
    
    # Print the rejoined, translated sentence
    print(" ".join(sentence_list))

if __name__ == '__main__':
    pl_sentence()