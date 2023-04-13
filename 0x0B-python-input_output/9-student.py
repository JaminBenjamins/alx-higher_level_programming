#!/usr/bin/python3
""" Defining a class """


class Student:
    """ An object attributing to a student """

    def __init__(self, first_name, last_name, age):
        """ Initializing the class
            Args:
                first_name - First name of student
                last_name - The last name of student
                age - The age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Obtain dictionary representation of class """
        return self.__dict__
