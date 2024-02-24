# Longest word per file
#  - Create a function find_longest_word
#    - Should take a txt file
#    - Should return longest word in the file
#  - Create a function find_all_longest_words
#    - Should take in directory name (containing text files)
#    - Should return a dictionary with key:value filename:longest_words

import os

def find_longest_word(file):
    current_longest = ""
    try:
        with open(file, encoding="utf8") as f:
            for line in f:
                for word in line.split():
                    # Added this to get rid of all the gutenberg links which made up most of the results
                    if not "gutenberg" in word:
                        if len(word) > len(current_longest):
                            current_longest = word
    except UnicodeDecodeError as e:
        print(f"Ignoring {file} due to error: {e}")
    
    return current_longest

def find_all_longest_words(dir):
    words_dict = {}
    for file in os.listdir(dir):
        file = os.path.join(dir, file)
        if os.path.isfile(file):
            words_dict[file] = find_longest_word(file)
    
    return words_dict



if __name__ == '__main__':
    file_dir = os.path.dirname(__file__) + "/21_files_dir"
    text_file = file_dir + "/43-0.txt"
    word = find_longest_word(text_file)
    print(word)

    print(find_all_longest_words(file_dir))