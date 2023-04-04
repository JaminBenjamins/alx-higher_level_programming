#!/usr/bin/python3
""" Defining a class """


class Rectangle:
    """ Represent a Rectangle """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle

        Args: 
            width(int) - the width of a rectangle
            height(int) - the height of a rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get / Set width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get / Set height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Initializing a public attribute """
        return (self.__width * self.__height)

    def perimeter(self, value):
        """ returns the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Retrn a printable form of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                append("\n")
        return("".join(rect))

    def __repr__(self):
        """ Return string representation of a rectangle """
        rect = "Rectangle(" + str(self.__width)
        rect += "," + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ Print message for every deletion of a rectangle """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
