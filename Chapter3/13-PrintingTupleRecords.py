# Printing Tuple Records
#  - Create a function format_sort_records()
#  - Should take a list tuples ("first", "last", hours_to_arrive)
#  - Should return the output as a formatted string

import operator

def format_sort_records(people):
    list_of_people = []
    for person in sorted(people, key=operator.itemgetter(1,0)):
        list_of_people.append(f"{person[1]:10} {person[0]:10} {person[2]:5.2f}")
    
    return print("\n".join(list_of_people))


if __name__ == '__main__':
    PEOPLE = [('Donald', 'Trump', 7.85),
             ('Vladimir', 'Putin', 3.626),
             ('Jinping', 'Xi', 10.603)]
    format_sort_records(PEOPLE)