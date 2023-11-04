# String Sort
# Create a function strsort()
#  - Should take in a string
#  - Should return the string sorted by unicode value

def strsort(user_string):
    user_string_list = sorted(user_string)

    return ''.join(user_string_list)

def strsort_extended(user_string):
    # Allow for splitting with whitespace before sorting

    return ','.join(sorted(user_string.split()))

def file_last_word(filename):
    # Should produce the last word alphabetically regardless of case
    word_list = []

    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                word_list.append(word)
    
    return sorted(word_list, key=str.lower)[-1]


if __name__ == '__main__':
    user_string = input("Enter the string to sort: ")
    print(strsort(user_string))
    print(strsort_extended(user_string))
    print(file_last_word("textfile.txt"))