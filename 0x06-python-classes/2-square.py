#!/usr/bin/python3
""" Defining a class """


class Square:
    """ Initializing a class """

    def __init__(self, size=0):
        """
            Initialize a square
            
            Args:
                size(int): Value of square
        """
        if not isinstance(size, int):
            raise TypeError("sizze must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size 
