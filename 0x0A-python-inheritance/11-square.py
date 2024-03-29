#!/usr/bin/python3
""" a class that inherits from another and prints """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ Inheriting attribuutes from a class
            Args:
                size - the size of square

            Return:
                The square description
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
