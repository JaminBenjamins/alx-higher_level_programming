#!/usr/bin/python3
""" Defining a nae printing function """


def say_my_name(first_name, last_name=""):
    """
        Args:
            first_name(str) - First name to print
            last_name(str) - Last name to print
    """
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print("y name is {} {}".format(first_name, last_name))
