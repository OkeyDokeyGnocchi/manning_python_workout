# Ubbi Dubbi
# Create a function ubbi_dubbi()
#  - Should take in an assumed English word (lowercase only)
#  - Should return the ubbi dubbi translation of the sentence
#  - Ubbi Dubbi is adding "ub" before all vowel sounds

def ubbi_dubbi(word):

    word_list = []

    for letter in word:
        if letter.lower() in 'aeiou':
            word_list.append(f'ub{letter}')
        else:
            word_list.append(letter)
    
    return ''.join(word_list)

if __name__ == '__main__':
    word = input("Please enter an English word: ")
    print(ubbi_dubbi(word))