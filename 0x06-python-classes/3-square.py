#!/usr/bin/python3
""" Defining a class Square """

class Square:
    #Instatiating a class
    def __init__(self,size=0):
        """
            Initialising a new square

            Args: 
                size(int): size of a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size

    def area(self):
        """ Returns area of square """
        return (self.__size * self.__size)


