#!/usr/bin/python3
""" Defines a square a subclass of Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defining a child class """
    def __init__(self, size):
        """ Initializing the class 
            Args: 
                size - the size of a square
        """
        super.integer_validator("width", width)
        super().__init__(size,size)
        self.__size
