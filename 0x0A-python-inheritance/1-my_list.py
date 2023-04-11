#!/usr/bin/python3
""" A class inheriting from another class """


class MyList(list):
    """ Class my list inberits from list """

    def print_sorted(self):
        """ print a sorted list """
        
        my_list = self[:]
        my_list.sort()
        print("{}".format(my_list))
