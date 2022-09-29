#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value == 0:
                best_score = value
            if best_score < value:
                best_score = value
                biggest_key = key
        return biggest_key
