#!/usr/bin/python3
""" Define a class Rectangle that inherits from another"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ Initializing a class 
            Args: 
                width - the width of rectangle
                height- height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        def area(self):
            """ Compute area of a rectangle """
            return self.__width * self.__height

        def __str__(self):
            """ Print area and string representation of class and attributes """
            rect = "[" + str(self.__class__.__name__) + "]"
            rect += str(self.__width) + "/" + str(self.__height)
            return rect
