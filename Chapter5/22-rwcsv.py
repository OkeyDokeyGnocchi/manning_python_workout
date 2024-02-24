# Reading and writing CSV
#  - Create a function passwd_to_csv
#    - Should have two arguments: (passwd_file, output_csv)
#    - Should take an /etc/passwd file
#    - Should return output csv with username and uuid seperated by \t

import csv
import os

def passwd_to_csv(passwd_file, output_csv):
    with open(passwd_file, "r") as pf:
        with open(output_csv, "w") as out_file:
            writer = csv.writer(out_file, delimiter="\t")
            for line in pf:
                if not line.startswith(("#", "\n")):
                    writer.writerow([line.split(":")[0], line.split(":")[2]])

def dict_to_csv(dictionary, output_csv):
    with open(output_csv, "w") as out_file:
        writer = csv.writer(out_file)
        for k,v in dictionary.items():
            writer.writerow([k, v, type(v).__name__])

if __name__ == '__main__':
    passwd_file = os.path.dirname(__file__) + "/etc-passwd"
    csv_file = os.path.dirname(__file__) + "/22-ouput.csv"

    passwd_to_csv(passwd_file, csv_file)

    val_dict = {
        "root": 0,
        "nobody": -2,
        "Stringman": "StringmanUuid"
    }
    dict_csv = os.path.dirname(__file__) + "/22-dict.csv"
    dict_to_csv(val_dict, dict_csv)