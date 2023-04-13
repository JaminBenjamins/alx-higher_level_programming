#!/usr/bin/python3
""" A function tha writes obj to txt file using JSON """
import json


def save_to_json_file(my_obj, filename):
    """ Define JSON writing function """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
