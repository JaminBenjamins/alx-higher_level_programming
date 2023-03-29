#!/usr/bin/python3
class Square:
    def __init__(self,size=0):
        self.size

    """ setting function for size """
    @property
    def size(self):
        self.__size

    """ setting properties for size """
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        return (self.size * self.size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
