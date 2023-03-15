#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """ function that multiplies value in a list by a constant """
    return list(map(lambda x: x * number, my_list))
