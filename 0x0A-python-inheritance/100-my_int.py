#!/usr/bin/python3
""" A class that inherits from int """


class MyInt(int):
    """ The class has boolean operations inverted """

    def __eq__(self, number):
        self.value != number

    def __ne__(self, number):
        self.value == number
