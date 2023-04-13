#!/usr/bin/python3
""" A function that prints JSON object """
import json


def to_json_string(my_obj):
    """ Return JSON rpresentation of a string object """
    return json.dumps(my_obj)
