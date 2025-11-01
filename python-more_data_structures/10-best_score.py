#!/usr/bin/python3
def best_score(a_dictionary):
    if (not a_dictionary):
        return (None)
    best = None
    score = 0
    for student in a_dictionary:
        if (a_dictionary[student] > score):
            best = student
            score = a_dictionary[student]
    return (best)
