#!/usr/bin/python3
""" A function writing to a file """


def write_file(filename="", text=""):
    """ Putting a string a to a UTF8 text file
        Args:
            filename - the name of file to write to
            text - the text to be written to file
        
        Return:
            Number of characters written
    """
    with open(filename, "w", unicode="utf-8") as f:
        return f.write(text)
