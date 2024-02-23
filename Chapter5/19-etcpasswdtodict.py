# /etc/passwd to dict
#  - Create a function passwd_to_dict
#    - Should take an /etc/passwd file
#    - Should return dict with Username:uuid pairs

import os

def passwd_to_dict(pass_file):
    user_dict = {}
    with open(pass_file) as f:
        for line in f:
            if not line.startswith(("#", "\n")):
                user_dict[line.split(":")[0]] = line.split(":")[2]
    
    return user_dict

if __name__ == '__main__':
    passwd_file = os.path.dirname(__file__) + "/etc-passwd"
    print(passwd_to_dict(passwd_file))