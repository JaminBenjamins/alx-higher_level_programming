#!/usr/bin/python3
""" Defining a function with serialized JSON object """


def class_to_json(obj):
    """ Return a dictionoary state of a simple data strucure """
    return obj.__dict__
