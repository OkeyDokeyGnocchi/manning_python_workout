# Most Repeating Word
#  - Create a function most_repeating_word()
#  - Should take a list of strings
#  - Should return the string with the most repeated letters

from collections import Counter

def most_repeating_word(word_list):
    current_highest = 0
    current_word = ""
    for word in word_list:
        if Counter(word).most_common(1)[0][1] > current_highest:
            current_word = word
            current_highest = Counter(word).most_common(1)[0][1]
    
    return print(f"{current_word}")

def most_repeated_vowel(word):
    counter = Counter(word)
    return max(counter[c] for c in 'aeiouAEIOU')

def most_repeating_word_vowels(word_list):
    return max(word_list, key=most_repeated_vowel)

if __name__ == '__main__':
    words = ['this', 'is', 'an', 'elementary', 'test', 'example']
    most_repeating_word(words)
    print(most_repeating_word_vowels(words))