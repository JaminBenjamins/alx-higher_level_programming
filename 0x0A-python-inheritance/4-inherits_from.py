#!/usr/bin/python3
""" A function that checks if an object belongs to the class it inherited """


def inherits_from(obj, a_class):
    """ Checks if an object is inherited from a class

        Args:
            obj - the attribute to check if it belongs to the class
            a_class - the class to check from

        Returns:
            True if object is a subclass of a_class
            False Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
