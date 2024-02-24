# Reading and writing CSV
#  - Create a function passwd_to_csv
#    - Should have two arguments: (passwd_file, output_csv)
#    - Should take an /etc/passwd file
#    - Should return output csv with username and uuid seperated by \t

import csv
import os

def passwd_to_csv(passwd_file, output_csv):
    with open(passwd_file, "r") as pf:
        with open(output_csv, "w") as of:
            writer = csv.writer(of, delimiter="\t")
            for line in pf:
                if not line.startswith(("#", "\n")):
                    writer.writerow([line.split(":")[0], line.split(":")[2]])


if __name__ == '__main__':
    passwd_file = os.path.dirname(__file__) + "/etc-passwd"
    csv_file = os.path.dirname(__file__) + "/22-ouput.csv"

    passwd_to_csv(passwd_file, csv_file)