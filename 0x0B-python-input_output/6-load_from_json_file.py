#!/usr/bin/python3
""" Define object creation from JSON file """
import json


def load_from_json_file(filename):
    """ Reading from a JSON file """
    with open(filename) as f:
        json.load(f)
