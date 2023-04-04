#!/usr/bin/python3
""" Define a function adding two numbers """


def add_integer(a, b=98):
    """ Return sum of two digits 

    Float data types are type casted to integer type

    Raises:
        TypeError if value of parameters is not float or int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
