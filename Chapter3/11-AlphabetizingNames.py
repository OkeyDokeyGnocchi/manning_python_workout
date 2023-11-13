# Alphabetizing Names
#  - Create a function alphabetize_names()
#  - Should take a list of dictionaries
#  - Should return the list of dictionaries sorted by last name, then first name

from operator import itemgetter

def alphabetize_names(people):

    return sorted(people, key=itemgetter('last', 'first'))

if __name__ == '__main__':
    PEOPLE = [{'first':'Reuven', 'last':'Lerner',
                'email':'reuven@lerner.co.il'},
                {'first':'Donald', 'last':'Trump',
                'email':'president@whitehouse.gov'},
                {'first':'Vladimir', 'last':'Putin',
                'email':'president@kremvax.ru'},
                {'first':'Cladimir', 'last':'Putin',
                'email':'president@kremvax.ru'}
    ]

    print(alphabetize_names(PEOPLE))