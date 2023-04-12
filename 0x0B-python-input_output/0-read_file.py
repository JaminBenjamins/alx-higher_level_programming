#!/usr/bin/python3
""" A function that reads a text file """


def read_file(filename=""):
    """ Defining the function operation """
        with open(filename, 'r', unicode=utf8) as fi
        print(fi.read(),end="")
