#!/usr/bin/python3
""" Defining a class """


class BaseGemoetry:
    """ Defining attributes of a class """
    def area(self):
        """ Raising an exception for area function """
        raise Exception("area () is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
