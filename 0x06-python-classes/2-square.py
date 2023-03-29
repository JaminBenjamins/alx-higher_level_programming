#!/usr/bin/python3
class Square:
    def __init__(self,size=0):
        if size is not isinstance:
            raise TypeError("sizze must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
       self.__size = size 
