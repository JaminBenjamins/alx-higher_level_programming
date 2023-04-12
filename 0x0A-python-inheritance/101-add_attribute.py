#!/usr/bin/python3
""" A functions that adds an attribute if possible """


def add_attribute(obj, attribute, value):
    """ Defining a function that  adds attribute
        Args:
            obj - the object to add attribute to
            attribute - the attribute of object
            value - the data to add
        Raises:
            TypeError - fi attributed can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
