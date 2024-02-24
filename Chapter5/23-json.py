# JSON
#  - Create a function print_scores
#    - Should take a directory path with scores json files in it
#    - Should return min score, max score, and average score for each subject

import glob
import json
import os

def print_scores(dir):
    score_dict = {}

    for file in glob.glob(f'{dir}/*.json'):
        score_dict[file] = {}

        with open(file) as f:
            for entry in json.load(f):
                for subject, score in entry.items():
                    score_dict[file].setdefault(subject, [])
                    score_dict[file][subject].append(score)
    
    for current_file in score_dict:
        print(current_file)
        for current_subject, current_scores in score_dict[current_file].items():
            lowest_score = min(current_scores)
            highest_score = max(current_scores)
            avg_score = sum(current_scores) / len(current_scores)

            print(f"{current_subject}: min {lowest_score}, max {highest_score}, average {avg_score}")



if __name__ == '__main__':
    working_dir = os.path.dirname(__file__)
    scores_dir = working_dir + "/scores"

    print_scores(scores_dir)