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

    def to_json(self, attrs=None):
        """ Obtain dictionary representation of class 
            If attributs is a list of string only those values
            can be retrieved 
                
            Args:
                attrs - attribute to represent
        """
        if (type(attrs) == list and
                all(type(att) == str for att in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
    def relaod_from_json(self, json):
        """ Replace the attribuets of a class
            Args:
                The key/value pair to supersede attributes 
        """
        for i, j in json.items():
            setattr(self, i, j)
