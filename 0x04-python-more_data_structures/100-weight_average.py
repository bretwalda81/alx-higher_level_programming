#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_score = 0
    total_scores = 0
    for tuple in my_list:
        weighted_score += tuple[0] * tuple[1]
        total_scores += tuple[1]
    return weighted_score / total_scores
