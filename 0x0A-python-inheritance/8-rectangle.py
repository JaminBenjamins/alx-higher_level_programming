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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


