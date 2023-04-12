#!/usr/bin/python3
""" Defines a square a subclass of Rectangle """
Square = __import__('9-rectangle').Square


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
