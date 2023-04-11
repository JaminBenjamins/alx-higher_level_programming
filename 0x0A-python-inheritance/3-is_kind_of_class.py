#!/usr/bin/python3
""" Define a class and the one it s inherited from """


def is_kind_of_class(obj, a_class):
    """ Look up if an object is in anistance of current or inherited class

        Args:
            obj - object to check if it belongs to a class
            a_class - to che ck if obj attribute belongs

        Return: True if obje is part of the class
                False Otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
