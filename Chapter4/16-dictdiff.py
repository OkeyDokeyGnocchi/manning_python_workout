# DictDiff
#  - Create a function dictdiff(dict1, dict2)
#    - Should take two dictionaries as args
#    - Should produce a dictionary with differences between them
#    - This dictionary should have key:value (type list), where key is key and value is list of the conflicting values
#    - If no differences: produce {}
#    - If a key is missing, that should produce None

def dictdiff(dict1, dict2):
    differences = {}
    for k in dict1:
        if k in dict2:
            if dict1[k] != dict2[k]:
                differences[k]