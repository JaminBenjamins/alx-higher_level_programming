#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())

    for value_key in a_dictionary:
        if list_key == a_dictionary.get(value_key):
            del a_dictionary[value_key]
    return a_dictionary
