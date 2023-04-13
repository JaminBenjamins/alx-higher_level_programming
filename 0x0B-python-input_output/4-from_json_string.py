#!/usr/bin/python3
""" A function that convert JSON to string """
import json


def from_json_string(my_str):
    """ Return a strin object from JSON """
    return json.loads(my_str)
