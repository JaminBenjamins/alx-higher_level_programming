#!/usr/bin/python3
""" a function that checks if an object belongs to a class """


def is_same_class(obj, a_class):
    """
        Args:
            obj - element to check if belongs to a_class
            a_class - the class to check from
        
        Return: True if object is instance of a class
                False Otherwise
    """
    if type(obj) == a_class:
        return True
    return False
