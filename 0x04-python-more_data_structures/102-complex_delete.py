#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value_check in list(a_dictionary.items()):
        if value_check == value:
            del a_dictionary[key]
    return a_dictionary
