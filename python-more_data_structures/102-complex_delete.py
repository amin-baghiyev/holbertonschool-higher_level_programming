#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (not a_dictionary):
        return (a_dictionary)
    keys = [key for key in a_dictionary if a_dictionary == value]
    for key in keys:
        del a_dictionary[key]
    return (a_dictionary)
